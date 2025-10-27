from html.parser import HTMLParser
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = [
    REPO_ROOT / "index.html",
    REPO_ROOT / "cechy.html",
    REPO_ROOT / "draft_planu.html",
    REPO_ROOT / "imersja_mechanika.html",
    REPO_ROOT / "organizacja.html",
]
CSS_FILE = REPO_ROOT / "assets" / "styles.css"
JS_FILE = REPO_ROOT / "assets" / "editable-tiles.js"
README_FILE = REPO_ROOT / "README.md"
NOTES_FILE = REPO_ROOT / "docs" / "notes.md"


class ScriptParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.scripts: list[str | None] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]):
        if tag != "script":
            return
        attrs_dict = dict(attrs)
        self.scripts.append(attrs_dict.get("src"))


def _extract_block(css: str, selector: str) -> str:
    start = css.find(selector)
    if start == -1:
        return ""

    brace_index = css.find("{", start)
    if brace_index == -1:
        return ""

    depth = 0
    for index in range(brace_index, len(css)):
        char = css[index]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return css[start : index + 1]
    return ""


def test_editable_tiles_module_loaded():
    for html_file in HTML_FILES:
        parser = ScriptParser()
        parser.feed(html_file.read_text(encoding="utf-8"))
        assert (
            "assets/editable-tiles.js" in parser.scripts
        ), f"Brak modułu editable-tiles na stronie {html_file.name}"


def test_editable_tiles_styles_defined():
    css = CSS_FILE.read_text(encoding="utf-8")
    required_snippets = [
        ".tile-edit-tab",
        ".tile-edit-panel",
        ".tile-edit-notice",
    ]
    for snippet in required_snippets:
        assert snippet in css, f"Brak definicji stylu {snippet} w assets/styles.css"


def test_editable_tab_positioned_within_card():
    css = CSS_FILE.read_text(encoding="utf-8")
    assert ".tile-edit-tab" in css, "Brak sekcji stylującej przycisk edycji."
    assert "right: clamp" in css, "Zakładka edycji powinna być zakotwiczona wewnątrz kafelka."
    assert "transform: rotate(90deg)" in css, "Zachowaj estetykę obróconej zakładki."


def test_tile_editable_content_has_padding():
    css = CSS_FILE.read_text(encoding="utf-8")
    assert ".tile-editable__content" in css, "Brak definicji treści kafelka."
    assert "padding-inline-end" in css, "Treść kafelka powinna omijać zakładkę edycji."


def test_editable_tiles_fallback_documented():
    js_content = JS_FILE.read_text(encoding="utf-8")
    assert (
        "Edycja kafelków jest wyłączona" in js_content
    ), "Brak komunikatu fallbacku w assets/editable-tiles.js"

    readme_content = README_FILE.read_text(encoding="utf-8")
    assert (
        "Brak dostępu do `localStorage` blokuje edycję" in readme_content
    ), "README nie opisuje zachowania bez localStorage"

    notes_content = NOTES_FILE.read_text(encoding="utf-8")
    assert (
        "brak dostępu komunikowany jest w UI" in notes_content
    ), "docs/notes.md nie odnotowuje fallbacku UI"
