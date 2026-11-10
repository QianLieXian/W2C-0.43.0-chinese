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
        if " - " in text and text.split(" - ",1)[0] in ("Home", "School", "Office Building", "Neighbor's", "Grandma's"):
            return "－".join(_zh_segment_translate(part) for part in text.split(" - "))
        for suffix, replacement in ((" parents' bedroom", "父母的卧室"), ("'s bedroom", "的卧室"), ("'s Bedroom", "的卧室"), ("'s Room", "的房间"), ("'s Office", "的诊所")):
            if text.endswith(suffix):
                return text[:-len(suffix)] + replacement
        return text

    def _zh_replace_text(text):
        if _zh_previous_replace is not None:
            text = _zh_previous_replace(text)
        if preferences.language == "zh":
            return _zh_segment_translate(text)
        return text

    def _zh_format_display(template, fields):
        text = renpy.translate_string(template)
        for key, value in fields:
            text = text.replace(key, value)
        return text

    config.replace_text = _zh_replace_text

translate zh style default:
    language "eastasian"
