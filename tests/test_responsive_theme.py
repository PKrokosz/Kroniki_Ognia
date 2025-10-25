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
