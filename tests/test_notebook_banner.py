from html.parser import HTMLParser
from pathlib import Path
from typing import TypedDict

REPO_ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = [
    REPO_ROOT / "index.html",
    REPO_ROOT / "cechy.html",
    REPO_ROOT / "draft_planu.html",
    REPO_ROOT / "imersja_mechanika.html",
    REPO_ROOT / "organizacja.html",
]

NOTEBOOK_URL = "https://notebooklm.google.com/notebook/cf797fdc-a8c2-44eb-b933-5ca5a3216674"
GOOGLE_DRIVE_URL = "https://drive.google.com/drive/folders/1ra1Qt97ojx5oc_De8R3ubHayC_gnKLRO?usp=sharing"
ARIA_LABEL = "Notebook LM — baza wiedzy z brainstormu"


class LinkInfo(TypedDict):
    href: str | None
    target: str | None
    rel: str | None
    class_list: list[str]


class BannerParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_banner = False
        self.banner_depth = 0
        self.banner_found = False
        self.banner_aria_label: str | None = None
        self.links: list[LinkInfo] = []
        self.banner_text: list[str] = []
        self.drive_icon_present = False

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
                    LinkInfo(
                        href=attrs_dict.get("href"),
                        target=attrs_dict.get("target"),
                        rel=attrs_dict.get("rel"),
                        class_list=(attrs_dict.get("class") or "").split(),
                    )
                )
            if tag == "svg" and attrs_dict.get("data-icon") == "google-drive":
                self.drive_icon_present = True

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


def test_notebook_banner_includes_drive_archive_link():
    for html_file in HTML_FILES:
        parser = BannerParser()
        parser.feed(html_file.read_text(encoding="utf-8"))

        drive_links = [link for link in parser.links if link.get("href") == GOOGLE_DRIVE_URL]
        assert drive_links, f"Brak linku do archiwum Google Drive w {html_file.name}"
        for drive_link in drive_links:
            assert "notebook-banner__link--drive" in drive_link.get("class_list", []), (
                f"Link do Google Drive wymaga klasy notebook-banner__link--drive w {html_file.name}"
            )
            assert drive_link.get("target") == "_blank", (
                f"Link do Google Drive wymaga target=_blank w {html_file.name}"
            )
            rel = (drive_link.get("rel") or "").split()
            assert "noopener" in rel, f"Link do Google Drive wymaga rel=noopener w {html_file.name}"
        assert parser.drive_icon_present, f"Brak ikony Google Drive w banerze w {html_file.name}"
