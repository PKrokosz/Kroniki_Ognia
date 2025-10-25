from pathlib import Path


def test_cname_managed_via_github_settings() -> None:
    cname_path = Path("CNAME")
    assert not cname_path.exists(), (
        "Repozytorium nie powinno przechowywać pliku CNAME — konfigurujemy domenę w ustawieniach GitHub Pages."
    )


def test_manual_custom_domain_documented() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "Repozytorium nie przechowuje pliku `CNAME`" in readme, (
        "README musi opisywać ręczne ustawienie custom domain w GitHub Pages bez śledzenia pliku CNAME."
    )

    notes = Path("docs/notes.md").read_text(encoding="utf-8")
    assert "5xWhy — Dlaczego nie trzymamy CNAME" in notes, (
        "Notatki powinny dokumentować decyzję 5xWhy o rezygnacji z pliku CNAME w repozytorium."
    )
