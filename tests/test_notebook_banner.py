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

NOTEBOOK_URL = "https://notebooklm.google.com/notebook/cf797fdc-a8c2-44eb-b933-5ca5a3216674"
ARIA_LABEL = "Notebook LM — baza wiedzy z brainstormu"


class BannerParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_banner = False
        self.banner_depth = 0
        self.banner_found = False
        self.banner_aria_label: str | None = None
        self.links: list[dict[str, str | None]] = []
        self.banner_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]):
        attrs_dict = dict(attrs)
        class_value = attrs_dict.get("class") or ""
        if tag == "div" and "notebook-banner" in class_value.split():
            self.in_banner = True
            self.banner_depth = 1
            self.banner_found = True
            self.banner_aria_label = attrs_dict.get("aria-label")
            return
        if self.in_banner:
            self.banner_depth += 1
            if tag == "a":
                self.links.append(
                    {
                        "href": attrs_dict.get("href"),
                        "target": attrs_dict.get("target"),
                        "rel": attrs_dict.get("rel"),
                    }
                )

    def handle_endtag(self, tag: str):
        if self.in_banner:
            self.banner_depth -= 1
            if self.banner_depth == 0:
                self.in_banner = False

    def handle_data(self, data: str):
        if self.in_banner:
            text = data.strip()
            if text:
                self.banner_text.append(text)


def test_notebook_banner_present_with_link():
    for html_file in HTML_FILES:
        parser = BannerParser()
        parser.feed(html_file.read_text(encoding="utf-8"))

        assert parser.banner_found, f"Brak bloku notebook-banner w {html_file.name}"
        assert parser.banner_aria_label == ARIA_LABEL, f"Niepoprawne aria-label w {html_file.name}"
        assert any(link.get("href") == NOTEBOOK_URL for link in parser.links), (
            f"Brak linku do Notebook LM w {html_file.name}"
        )
        assert any("Latający zwiadowca" in fragment for fragment in parser.banner_text), (
            f"Brak narracyjnego komunikatu o latającym zwiadowcy w {html_file.name}"
        )
        for link in parser.links:
            if link.get("href") == NOTEBOOK_URL:
                assert link.get("target") == "_blank", f"Link Notebook LM wymaga target=_blank w {html_file.name}"
                rel = (link.get("rel") or "").split()
                assert "noopener" in rel, f"Link Notebook LM wymaga rel=noopener w {html_file.name}"
