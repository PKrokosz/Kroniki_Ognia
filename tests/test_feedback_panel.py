from pathlib import Path


def test_feedback_toggle_markup_present() -> None:
    html = Path("organizacja.html").read_text(encoding="utf-8")
    assert 'data-thread-key="' in html, "Karty wątków powinny posiadać identyfikator data-thread-key."
    assert 'class="rate-toggle"' in html, "Brak przycisku rozwijającego panel oceny."
    assert 'class="rate-panel"' in html, "Panel komentarza powinien być renderowany wraz z kartą."
    assert 'organizacja-feedback:' in html, "Brak prefiksu klucza localStorage dla komentarzy."


def test_feedback_styles_defined() -> None:
    css = Path("assets/styles.css").read_text(encoding="utf-8")
    assert ".rate-panel" in css, "Styl panelu komentarza musi być zdefiniowany."
    assert ".rate-toggle" in css, "Przycisk otwierający panel wymaga stylu."
    assert ".rate-save" in css and ".rate-clear" in css, "Przyciski akcji panelu wymagają dedykowanych styli."
