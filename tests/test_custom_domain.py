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


def test_dns_host_documented() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "pkr0kosz.github.io" in readme, (
        "README musi wskazywać właściwy host GitHub Pages (`pkr0kosz.github.io`) dla rekordu CNAME."
    )
    assert "www.larpkronikiognia.com" in readme, (
        "README powinno wspominać o opcjonalnej domenie lustrzanej `.com` i jej przekierowaniu."
    )
    assert "dig www.larpkronikiognia.com CNAME" in readme, (
        "README powinno instruować, jak zweryfikować konfigurację domeny `.com`."
    )

    notes = Path("docs/notes.md").read_text(encoding="utf-8")
    assert "5xWhy — Dlaczego weryfikacja DNS GitHub Pages się nie powiodła" in notes, (
        "Notatki muszą zawierać analizę 5xWhy dotyczącą błędu weryfikacji DNS na GitHub Pages."
    )
    assert "`pkr0kosz.github.io`" in notes, (
        "Notatki powinny podkreślać właściwą wartość rekordu CNAME (`pkr0kosz.github.io`)."
    )


def test_domain_verification_txt_documented() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "_gh-SilesianGames-o.www.larpkronikiognia.pl" in readme, (
        "README musi instruować o rekordzie TXT `_gh-SilesianGames-o.www.larpkronikiognia.pl` dla weryfikacji domeny organizacji."
    )
    assert "6224e5ae12" in readme, (
        "README powinno zawierać aktualny kod weryfikacyjny `6224e5ae12`, aby operator DNS nie musiał go szukać w historii."
    )
    assert "72" in readme, (
        "README musi przypominać o propagacji rekordu TXT do 72 godzin."
    )
    assert "7 dni" in readme, (
        "README musi wspominać o 7-dniowej ważności kodu weryfikacyjnego."
    )

    notes = Path("docs/notes.md").read_text(encoding="utf-8")
    assert "5xWhy — Weryfikacja domeny organizacji TXT" in notes, (
        "Notatki powinny dokumentować proces weryfikacji TXT formą 5xWhy."
    )
    assert "_gh-SilesianGames-o.www.larpkronikiognia.pl" in notes, (
        "Notatki muszą wymieniać hosta rekordu TXT, aby zachować pełny kontekst decyzji."
    )
    assert "6224e5ae12" in notes, (
        "Notatki muszą zawierać kod weryfikacyjny `6224e5ae12` w ramach dokumentacji operacyjnej."
    )
