from pathlib import Path


def test_cname_points_to_custom_domain() -> None:
    cname_path = Path("CNAME")
    assert cname_path.exists(), "Brak pliku CNAME wymaganego przez GitHub Pages."
    content = cname_path.read_text(encoding="utf-8")
    assert content == "www.larpkronikiognia.pl\n", (
        "Plik CNAME powinien zawierać wyłącznie www.larpkronikiognia.pl zakończone nową linią"
    )


def test_cname_has_trailing_newline() -> None:
    """GitHub Pages zaleca zakończenie pliku CNAME znakiem nowej linii."""
    content = Path("CNAME").read_bytes()
    assert content.endswith(b"\n"), "Plik CNAME powinien kończyć się znakiem nowej linii."
