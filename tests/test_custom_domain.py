from pathlib import Path


def test_cname_points_to_custom_domain() -> None:
    cname_path = Path("CNAME")
    assert cname_path.exists(), "Brak pliku CNAME wymaganego przez GitHub Pages."
    content = cname_path.read_text(encoding="utf-8").strip()
    assert content == "www.larpkronikiognia.pl", (
        "Plik CNAME powinien wskazywać na www.larpkronikiognia.pl"
    )


def test_cname_has_trailing_newline() -> None:
    """GitHub Pages zaleca zakończenie pliku CNAME znakiem nowej linii."""
    content = Path("CNAME").read_bytes()
    assert content.endswith(b"\n"), "Plik CNAME powinien kończyć się znakiem nowej linii."
