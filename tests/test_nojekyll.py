"""Tests ensuring GitHub Pages serves the site statically without Jekyll."""
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_nojekyll_file_present():
    file_path = ROOT / ".nojekyll"
    assert file_path.exists(), "Brak pliku .nojekyll blokującego Jekylla na GitHub Pages"
    assert file_path.read_text(encoding="utf-8") == "", ".nojekyll powinien być pustym plikiem sterującym hostingiem"


def test_readme_documents_nojekyll():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert ".nojekyll" in readme, "README musi wymieniać plik .nojekyll jako element struktury"
    assert "Jekyll" in readme, "README powinno tłumaczyć powód blokady Jekylla"
