param([string]$ApkPath)
$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = New-Object System.Text.UTF8Encoding
Add-Type -AssemblyName System.IO.Compression.FileSystem
$root = $PSScriptRoot
$tools = Join-Path $root 'tools'
$output = Join-Path $root 'output'
$manifest = Get-Content -LiteralPath (Join-Path $root 'manifest.json') -Raw -Encoding UTF8 | ConvertFrom-Json
function Get-CheckedFile([string]$Url, [string]$Path, [string]$Hash) {
    if (!(Test-Path -LiteralPath $Path) -or (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash -ne $Hash) {
        Write-Host ('正在下载：' + [IO.Path]::GetFileName($Path))
        [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
        Invoke-WebRequest -Uri $Url -OutFile ($Path + '.download') -UseBasicParsing
        if ((Get-FileHash -LiteralPath ($Path + '.download') -Algorithm SHA256).Hash -ne $Hash) { throw '下载文件校验失败，请重试。' }
        Move-Item -LiteralPath ($Path + '.download') -Destination $Path -Force
    }
}
try {
    if (!$ApkPath) {
        foreach ($candidate in @((Join-Path $root 'W2C-0.43.0-android.apk'), (Join-Path (Split-Path $root -Parent) 'W2C-0.43.0-android.apk'))) {
            if (Test-Path -LiteralPath $candidate) { $ApkPath = $candidate; break }
        }
    }
    if (!$ApkPath -or !(Test-Path -LiteralPath $ApkPath -PathType Leaf)) { throw '请将原版 W2C-0.43.0-android.apk 放在补丁文件夹里，或拖到 BAT 上。' }
    $ApkPath = (Resolve-Path -LiteralPath $ApkPath).Path
    Write-Host '正在校验原版 APK……'
    if ((Get-FileHash -LiteralPath $ApkPath -Algorithm SHA256).Hash -ne $manifest.input_sha256) { throw '原版 APK 不匹配。本补丁仅适用于指定的 W2C 0.43.0 安卓原包。' }
    foreach ($file in $manifest.files) {
        $path = Join-Path $root $file.path
        if (!(Test-Path -LiteralPath $path) -or (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash -ne $file.sha256) { throw ('补丁文件损坏或缺失：' + $file.path) }
    }
    New-Item -ItemType Directory -Path $tools, $output -Force | Out-Null
    $java = Get-ChildItem -LiteralPath $tools -Filter java.exe -File -Recurse | Where-Object { $_.Directory.Name -eq 'bin' } | Select-Object -First 1
    if (!$java) {
        $jreZip = Join-Path $tools 'java17.zip'
        Get-CheckedFile $manifest.java.url $jreZip $manifest.java.sha256
        Expand-Archive -LiteralPath $jreZip -DestinationPath (Join-Path $tools 'java') -Force
        $java = Get-ChildItem -LiteralPath (Join-Path $tools 'java') -Filter java.exe -File -Recurse | Select-Object -First 1
        if (!$java) { throw 'Java 解压失败。' }
    }
    $signer = Join-Path $tools 'uber-apk-signer.jar'
    Get-CheckedFile $manifest.signer.url $signer $manifest.signer.sha256
    # Pin the same public patch certificate across computers; never inspect a user's signing keys.
    $jar = [IO.Compression.ZipFile]::OpenRead($signer)
    try {
        $entry = $jar.GetEntry('debug.keystore')
        if (!$entry) { throw '签名工具中没有预置测试证书。' }
        [IO.Compression.ZipFileExtensions]::ExtractToFile($entry, (Join-Path $tools 'patch.keystore'), $true)
    } finally { $jar.Dispose() }
    $unsigned = Join-Path $output 'W2C-0.43.0-zh-unsigned.apk'
    if ($ApkPath -eq $unsigned) { throw '输入文件不能是输出临时包。' }
    Write-Host '正在合并汉化补丁……'
    Copy-Item -LiteralPath $ApkPath -Destination $unsigned -Force
    $zip = [IO.Compression.ZipFile]::Open($unsigned, [IO.Compression.ZipArchiveMode]::Update, [Text.Encoding]::UTF8)
    try {
        foreach ($entry in @($zip.Entries)) {
            if ($entry.FullName.StartsWith('assets/x-game/x-tl/x-zh/') -or $entry.FullName -match '^META-INF/[^/]+\.(SF|RSA|DSA|EC|MF)$') { $entry.Delete() }
        }
        foreach ($file in $manifest.files) {
            if (!$file.apk_entry) { continue }
            $existing = $zip.GetEntry($file.apk_entry)
            if ($existing) { $existing.Delete() }
            [IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, (Join-Path $root $file.path), $file.apk_entry, [IO.Compression.CompressionLevel]::Optimal) | Out-Null
        }
    } finally { $zip.Dispose() }
    Write-Host '正在对齐、签名并验证 APK……'
    $signDir = Join-Path $output ('signed-' + [Guid]::NewGuid().ToString('N'))
    & $java.FullName '-Dfile.encoding=UTF-8' '-Dsun.stdout.encoding=UTF-8' '-Dsun.stderr.encoding=UTF-8' '-jar' $signer '-a' $unsigned '-o' $signDir '--allowResign' '--ksDebug' (Join-Path $tools 'patch.keystore')
    if ($LASTEXITCODE -ne 0) { throw 'APK 签名失败，请查看上方错误。' }
    $signed = Get-ChildItem -LiteralPath $signDir -Filter '*-aligned-debugSigned.apk' -File | Select-Object -First 1
    if (!$signed) { throw '未找到签名后的 APK。' }
    $final = Join-Path $output 'W2C-0.43.0-zh-android.apk'
    Move-Item -LiteralPath $signed.FullName -Destination $final -Force
    & $java.FullName '-Dfile.encoding=UTF-8' '-Dsun.stdout.encoding=UTF-8' '-Dsun.stderr.encoding=UTF-8' '-jar' $signer '-a' $final '-y'
    if ($LASTEXITCODE -ne 0) { throw '最终 APK 签名或对齐校验未通过。' }
    $check = [IO.Compression.ZipFile]::OpenRead($final)
    try {
        foreach ($file in $manifest.files) {
            if (!$file.apk_entry) { continue }
            $entry = $check.GetEntry($file.apk_entry)
            if (!$entry) { throw ('APK 内缺少：' + $file.apk_entry) }
            $stream = $entry.Open()
            $sha = [Security.Cryptography.SHA256]::Create()
            try { $hash = [BitConverter]::ToString($sha.ComputeHash($stream)).Replace('-', '') }
            finally { $stream.Dispose(); $sha.Dispose() }
            if ($hash -ne $file.sha256) { throw ('APK 内文件校验失败：' + $file.apk_entry) }
        }
    } finally { $check.Dispose() }
    (Get-FileHash -LiteralPath $final -Algorithm SHA256).Hash + '  ' + [IO.Path]::GetFileName($final) | Set-Content -LiteralPath (Join-Path $output 'SHA256.txt') -Encoding ASCII
    Write-Host ('完成：' + $final) -ForegroundColor Green
    Write-Host '原版 APK 已保留。安装前先备份存档；汉化版签名与原版不同。'
    exit 0
} catch {
    Write-Host ('失败：' + $_.Exception.Message) -ForegroundColor Red
    exit 1
}
