@echo off
chcp 65001 >nul
cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0patch_apk.ps1" -ApkPath "%~1"
set "PATCH_RESULT=%errorlevel%"
echo.
pause
exit /b %PATCH_RESULT%
