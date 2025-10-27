from pathlib import Path

import pytest


@pytest.fixture(scope="module")
def stylesheet_text() -> str:
    return Path("assets/styles.css").read_text(encoding="utf-8")


def _extract_block(text: str, header: str) -> str:
    start = text.find(header)
    if start == -1:
        return ""

    brace_index = text.find("{", start)
    if brace_index == -1:
        return ""

    depth = 0
    for index in range(brace_index, len(text)):
        char = text[index]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[start : index + 1]

    return ""


def test_mobile_media_queries_present(stylesheet_text: str) -> None:
    header = "@media (max-width: 600px)"
    block = _extract_block(stylesheet_text, header)
    assert block, "Brak dedykowanego bloku @media dla nagłówka mobilnego."
    assert "flex-direction: column;" in block, "Nagłówek nie przełącza się na układ kolumnowy."
    assert "padding: 20px;" in block, "Karty powinny mieć zmniejszony padding na urządzeniach mobilnych."


def test_ambient_effects_defined(stylesheet_text: str) -> None:
    assert "body::before" in stylesheet_text, "Oczekiwano warstwy ambientowej dla ciała strony."
    assert "@keyframes emberPulse" in stylesheet_text, "Brak animacji żarzenia tła."
    assert ".page-hero::after" in stylesheet_text, "Sekcja bohatera powinna mieć dodatkową warstwę graficzną."


def test_cards_grid_auto_fit(stylesheet_text: str) -> None:
    block = _extract_block(stylesheet_text, ".cards-grid")
    assert block, "Brak definicji siatki kart w arkuszu stylów."
    assert "repeat(auto-fit" in block, "Siatka kart powinna korzystać z repeat(auto-fit, ...)."
    assert "--card-min-width" in block, "Siatka kart wymaga zmiennej --card-min-width do sterowania szerokością kafelka."


def test_cards_grid_columns_capped(stylesheet_text: str) -> None:
    base_block = _extract_block(stylesheet_text, ".cards-grid")
    assert "--cards-max-columns" in base_block, "Brakuje zmiennej ograniczającej liczbę kolumn."
    assert "max-width:" in base_block and "var(--cards-max-columns" in base_block, (
        "Siatka powinna ograniczać maksymalną szerokość zależnie od liczby kolumn."
    )

    columns_two = _extract_block(stylesheet_text, ".cards-grid.columns-2")
    assert "--cards-max-columns: 2" in columns_two, "Wariant columns-2 powinien blokować układ do dwóch kolumn."


def test_visual_key_images_blurred(stylesheet_text: str) -> None:
    block = _extract_block(stylesheet_text, ".visual-key__tile img")
    assert block, "Brak definicji obrazów visual key w arkuszu stylów."
    assert "position: absolute" in block, "Obrazy visual key powinny wypełniać kafelek jako tło."
    assert "filter: blur" in block, "Obrazy visual key muszą być rozmyte dla efektu tła."
    assert "opacity:" in block, "Obrazy visual key powinny mieć kontrolowaną przezroczystość."


def test_home_hero_uses_gallery_images(stylesheet_text: str) -> None:
    block = _extract_block(stylesheet_text, ".page-home .page-hero")
    assert block, "Brak dedykowanej sekcji tła dla strony głównej."
    for image in ("img/1.jpg", "img/4.jpg", "img/7.jpg"):
        assert image in block, f"Tło strony głównej powinno wykorzystywać {image}."
