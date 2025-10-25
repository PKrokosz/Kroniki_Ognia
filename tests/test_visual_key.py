from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from typing import TypedDict

REPO_ROOT = Path(__file__).resolve().parents[1]
INDEX_HTML = REPO_ROOT / "index.html"

EXPECTED_TILES: dict[str, dict[str, str]] = {
    "visual-key__tile--ember": {"image": "img/1.jpg", "link": "cechy.html"},
    "visual-key__tile--glow": {"image": "img/4.jpg", "link": "imersja_mechanika.html"},
    "visual-key__tile--flame": {"image": "img/7.jpg", "link": "draft_planu.html"},
}


# Aktualizacja: jawnie typujemy strukturę kafelków na potrzeby `mypy .`.
class VisualKeyTile(TypedDict, total=False):
    classes: list[str]
    image: str | None
    alt: str | None
    link: str | None


class AutoplayButton(TypedDict, total=False):
    type: str | None
    data: str | None


class VisualKeyParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_section = False
        self.section_depth = 0
        self.section_found = False
        self.tiles: list[VisualKeyTile] = []
        self.current_tile: VisualKeyTile | None = None
        self.autoplay_button: AutoplayButton | None = None
        self.status_roles: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]):
        attrs_dict = dict(attrs)
        class_value = attrs_dict.get("class") or ""
        class_list = class_value.split()

        if tag == "section" and "visual-key" in class_list:
            self.in_section = True
            self.section_found = True
            self.section_depth = 1
            return

        if self.in_section:
            self.section_depth += 1
            if tag == "figure" and "visual-key__tile" in class_list:
                tile: VisualKeyTile = {
                    "classes": class_list,
                    "image": None,
                    "alt": None,
                    "link": None,
                }
                self.tiles.append(tile)
                self.current_tile = tile
            elif tag == "img" and self.current_tile is not None:
                self.current_tile["image"] = attrs_dict.get("src")
                self.current_tile["alt"] = attrs_dict.get("alt")
            elif tag == "a" and self.current_tile is not None:
                self.current_tile["link"] = attrs_dict.get("href")
            elif tag == "button" and "visual-key__autoplay" in class_list:
                self.autoplay_button = {
                    "type": attrs_dict.get("type"),
                    "data": attrs_dict.get("data-visual-key-autoplay"),
                }
            elif tag == "p" and "visual-key__status" in class_list:
                role = attrs_dict.get("role")
                if role:
                    self.status_roles.append(role)

    def handle_endtag(self, tag: str):
        if self.in_section:
            self.section_depth -= 1
            if tag == "figure":
                self.current_tile = None
            if self.section_depth == 0:
                self.in_section = False


def test_visual_key_section_present():
    parser = VisualKeyParser()
    parser.feed(INDEX_HTML.read_text(encoding="utf-8"))

    assert parser.section_found, "Sekcja visual key musi być obecna na stronie głównej."
    assert len(parser.tiles) == 3, "Sekcja visual key powinna zawierać trzy kafelki narracyjne."

    for tile in parser.tiles:
        classes = tile.get("classes") or []
        modifier = next((cls for cls in classes if cls.startswith("visual-key__tile--")), None)
        assert modifier, "Każdy kafelek visual key wymaga klasy wariantu narracyjnego."
        assert modifier in EXPECTED_TILES, f"Nieoczekiwany wariant kafelka: {modifier}"

        expected = EXPECTED_TILES[modifier]
        assert tile.get("image") == expected["image"], (
            f"Kafelek {modifier} powinien używać obrazu {expected['image']} z repozytorium."
        )
        assert tile.get("link") == expected["link"], (
            f"Kafelek {modifier} powinien linkować do {expected['link']}."
        )
        alt = tile.get("alt") or ""
        assert alt.strip(), f"Kafelek {modifier} wymaga opisu alt dla dostępności."

    assert parser.autoplay_button is not None, "Sekcja visual key wymaga przycisku autoodtwarzania."
    assert parser.autoplay_button.get("type") == "button", "Przycisk autoodtwarzania musi mieć type=button."
    assert parser.autoplay_button.get("data") is not None, "Przycisk autoodtwarzania wymaga atrybutu data-visual-key-autoplay."
    assert "status" in parser.status_roles, "Sekcja visual key wymaga elementu status z aria-live."
