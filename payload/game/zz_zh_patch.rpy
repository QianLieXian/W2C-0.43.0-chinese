# W2C 0.43.0 Simplified Chinese patch. No save variable or internal ID rewriting.
init 999 python:
    import json as _zh_json
    from functools import lru_cache as _zh_lru_cache
    if not getattr(persistent, "w2c_zh_patch_installed", False):
        preferences.language = "zh"
        persistent.w2c_zh_patch_installed = True
    with renpy.file("tl/zh/display_segments.json") as _zh_file:
        _zh_segments = _zh_json.loads(_zh_file.read().decode("utf-8"))
    _zh_previous_replace = config.replace_text

    @_zh_lru_cache(maxsize=4096)
    def _zh_segment_translate(text):
        direct = _zh_segments.get(text)
        if direct is not None:
            return direct
        stripped = text.strip()
        direct = _zh_segments.get(stripped)
        if direct is not None:
            return text[:len(text)-len(text.lstrip())] + direct + text[len(text.rstrip()):]
        return text

    def _zh_replace_text(text):
        if _zh_previous_replace is not None:
            text = _zh_previous_replace(text)
        if preferences.language == "zh":
            return _zh_segment_translate(text)
        return text

    config.replace_text = _zh_replace_text

translate zh style default:
    language "eastasian"
