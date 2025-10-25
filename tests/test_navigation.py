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

EXPECTED_LINKS = [
    ("index.html", "🏠 Strona główna"),
    ("cechy.html", "🔥 Cechy świata"),
    ("draft_planu.html", "🧭 Draft planu"),
    ("imersja_mechanika.html", "✨ Imersja i mechanika"),
    ("organizacja.html", "🏛️ Organizacja"),
]


class NavParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_nav = False
        self.current_href: str | None = None
        self.links: list[tuple[str, str]] = []
        self.stylesheet_linked = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]):
        attrs_dict = dict(attrs)
        if tag == "link" and attrs_dict.get("rel") == "stylesheet" and attrs_dict.get("href") == "assets/styles.css":
            self.stylesheet_linked = True
        if tag == "nav" and "site-nav" in (attrs_dict.get("class") or ""):
            self.in_nav = True
        if self.in_nav and tag == "a":
            self.current_href = attrs_dict.get("href")

    def handle_endtag(self, tag: str):
        if tag == "nav" and self.in_nav:
            self.in_nav = False
        if tag == "a":
            self.current_href = None

    def handle_data(self, data: str):
        if self.in_nav and self.current_href:
            text = data.strip()
            if text:
                self.links.append((self.current_href, text))


def test_navigation_links_consistent():
    for html_file in HTML_FILES:
        parser = NavParser()
        parser.feed(html_file.read_text(encoding="utf-8"))
        assert parser.stylesheet_linked, f"Brak odnośnika do assets/styles.css w {html_file.name}"
        assert parser.links == EXPECTED_LINKS, (
            f"Niespójna nawigacja w {html_file.name}: {parser.links}"
        )
