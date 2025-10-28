from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = {
    REPO_ROOT / "index.html": "page-home",
    REPO_ROOT / "cechy.html": "page-cechy",
    REPO_ROOT / "draft_planu.html": "page-draft",
    REPO_ROOT / "imersja_mechanika.html": "page-imersja",
    REPO_ROOT / "mindmap.html": "page-mindmap",
    REPO_ROOT / "organizacja.html": "page-organizacja",
}

PAGE_LAYER_IMAGES = {
    "page-home": ["../img/1.jpg", "../img/2.jpg", "../img/3.jpg"],
    "page-cechy": ["../img/4.jpg", "../img/5.jpg", "../img/6.jpg"],
    "page-draft": ["../img/7.jpg", "../img/8.jpg", "../img/2.jpg"],
    "page-imersja": ["../img/3.jpg", "../img/6.jpg", "../img/9.jpg"],
    "page-mindmap": ["../img/8.jpg", "../img/9.jpg", "../img/6.jpg"],
    "page-organizacja": ["../img/1.jpg", "../img/4.jpg", "../img/5.jpg"],
}


class AmbientParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.body_classes: set[str] = set()
        self.background_present = False
        self._in_background = False
        self._background_depth = 0
        self.layer_modifiers: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]):
        attrs_dict = dict(attrs)
        if tag == "body":
            classes = (attrs_dict.get("class") or "").split()
            self.body_classes.update(filter(None, classes))
        if tag == "div":
            classes = (attrs_dict.get("class") or "").split()
            if "ambient-background" in classes:
                self.background_present = True
                self._in_background = True
                self._background_depth = 1
                return
            if self._in_background:
                self._background_depth += 1
                if "ambient-layer" in classes:
                    for class_name in classes:
                        if class_name.startswith("ambient-layer--"):
                            self.layer_modifiers.add(class_name)

    def handle_endtag(self, tag: str):
        if tag == "div" and self._in_background:
            self._background_depth -= 1
            if self._background_depth == 0:
                self._in_background = False


def test_html_contains_layered_backgrounds():
    for html_file, expected_body_class in HTML_FILES.items():
        parser = AmbientParser()
        parser.feed(html_file.read_text(encoding="utf-8"))
        assert expected_body_class in parser.body_classes, (
            f"Brak klasy body {expected_body_class} w {html_file.name}"
        )
        assert parser.background_present, f"Brak kontenera ambient-background w {html_file.name}"
        assert parser.layer_modifiers == {
            "ambient-layer--1",
            "ambient-layer--2",
            "ambient-layer--3",
        }, f"Niepełny zestaw warstw ambient w {html_file.name}: {parser.layer_modifiers}"


def test_css_defines_three_images_per_page():
    css = (REPO_ROOT / "assets" / "styles.css").read_text(encoding="utf-8")
    assert "@keyframes ambientDrift" in css, "Brak animacji ambientDrift w arkuszu stylów"
    for page_class, image_paths in PAGE_LAYER_IMAGES.items():
        for index, image in enumerate(image_paths, start=1):
            selector = rf"\.{page_class} \.ambient-layer--{index}"
            assert re.search(selector, css), f"Brak selektora {selector} w styles.css"
            pattern = rf"\.{page_class} \.ambient-layer--{index}\s*{{[^}}]*background-image:\s*url\(['\"]?{re.escape(image)}['\"]?\);"
            assert re.search(pattern, css, flags=re.MULTILINE | re.DOTALL), (
                f"Brak przypisanego obrazu {image} dla {page_class} warstwa {index}"
            )


def test_reduced_motion_disables_layer_animation():
    css = (REPO_ROOT / "assets" / "styles.css").read_text(encoding="utf-8")
    marker = "@media (prefers-reduced-motion: reduce)"
    start = css.find(marker)
    assert start != -1, "Brak bloku prefers-reduced-motion"
    depth = 0
    snippet_chars: list[str] = []
    for char in css[start:]:
        snippet_chars.append(char)
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                break
    snippet = "".join(snippet_chars)
    assert ".ambient-layer" in snippet, (
        "Blok prefers-reduced-motion nie wyłącza animacji warstw ambient"
    )


def test_ambient_layers_meet_visibility_thresholds():
    css = (REPO_ROOT / "assets" / "styles.css").read_text(encoding="utf-8")
    background_block = re.search(r"\.ambient-background\s*{[^}]*}", css, flags=re.DOTALL)
    assert background_block, "Brak reguły .ambient-background"
    z_index_match = re.search(r"z-index:\s*(-?\d+)", background_block.group(0))
    assert z_index_match, "Brak z-index dla .ambient-background"
    assert int(z_index_match.group(1)) >= -1, "ambient-background powinien mieć z-index ≥ -1"

    selectors = [
        r"\.ambient-layer\s*{[^}]*}",
        r"\.ambient-layer:nth-child\(2\)\s*{[^}]*}",
        r"\.ambient-layer:nth-child\(3\)\s*{[^}]*}",
    ]
    for selector in selectors:
        block = re.search(selector, css, flags=re.DOTALL)
        assert block, f"Brak reguły dopasowanej do {selector}"
        opacity_match = re.search(r"opacity:\s*([0-9.]+)", block.group(0))
        assert opacity_match, f"Brak opacity w regule {selector}"
        opacity_value = float(opacity_match.group(1))
        assert opacity_value >= 0.45, (
            f"Warstwa ambient w {selector} ma zbyt niską przezroczystość ({opacity_value})"
        )
