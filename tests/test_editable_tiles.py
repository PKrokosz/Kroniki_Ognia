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


def test_editable_tiles_module_removed():
    for html_file in HTML_FILES:
        parser = ScriptParser()
        parser.feed(html_file.read_text(encoding="utf-8"))
        assert (
            "assets/editable-tiles.js" not in parser.scripts
        ), f"Strona {html_file.name} nadal ładuje wyłączoną zakładkę edycji"


def test_editable_tiles_styles_removed():
    css = CSS_FILE.read_text(encoding="utf-8")
    forbidden_snippets = [
        ".tile-edit-tab",
        ".tile-edit-panel",
        ".tile-editable__content",
    ]
    for snippet in forbidden_snippets:
        assert (
            snippet not in css
        ), f"assets/styles.css nadal zawiera styl {snippet}, mimo usunięcia zakładki edycji"


def test_no_residual_positioning_rules():
    css = CSS_FILE.read_text(encoding="utf-8")
    assert "right: clamp" not in css, "Pozostały reguły pozycjonujące zakładkę edycji."
    assert "transform: rotate(90deg)" not in css, "Pozostały obroty zakładki edycji."


def test_no_padding_reserved_for_edit_panel():
    css = CSS_FILE.read_text(encoding="utf-8")
    assert "padding-inline-end" not in css, "Pozostawiono odsunięcie pod panel edycji."
    assert "margin-right: 260px" not in css, "Pozostawiono margines dla panelu edycji."


def test_editable_tiles_module_deleted():
    assert not JS_FILE.exists(), "Plik assets/editable-tiles.js powinien zostać usunięty"
