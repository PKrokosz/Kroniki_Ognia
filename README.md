# Kroniki Ognia — Strona Projektowa

Statyczna witryna dokumentująca projekt LARP "Kroniki Ognia". Repozytorium zawiera stronę główną oraz szczegółowe podstrony z analizą fabularną i organizacyjną.

## Struktura
- `index.html` — landing page GitHub Pages.
- `cechy.html`, `draft_planu.html`, `imersja_mechanika.html`, `organizacja.html` — podstrony tematyczne.
- `assets/styles.css` — wspólny arkusz stylów.
- `docs/` — planowanie faz, zadania, notatki, ADR.
- `.codex/` — presety ról Codex.
- `tests/` — testy automatyczne (pytest).

## Uruchomienie lokalne
Strony to statyczne pliki HTML. Wystarczy otworzyć dowolny plik w przeglądarce lub użyć prostego serwera:

```bash
python -m http.server 8000
```

## Testy
```bash
pip install -r requirements.txt
pytest
```

Testy sprawdzają spójność nawigacji na wszystkich podstronach, obecność mobilnych styli i ambientowych efektów w `assets/styles.css` (`tests/test_responsive_theme.py`), a także integralność banera kierującego do bazy wiedzy Notebook LM (`tests/test_notebook_banner.py`).

## Akceptacja ręczna
- Otwórz `index.html` i upewnij się, że wszystkie linki prowadzą do właściwych stron.
- Zweryfikuj responsywność nagłówka i nawigacji na szerokościach mobilnych (układ kolumnowy, zmniejszone paddingi kart).
- Oceń nową, stonowaną paletę i subtelny efekt pulsującego tła w kontekście narracji projektu.
- Kliknij baner Notebook LM i sprawdź, czy otwiera się właściwy notebook z bazą wiedzy brainstormu.

## Aktualizacja fazy 2
- Paleta kolorów została przygaszona i oparta na barwach ziemistych; akcenty złamane bursztynem nadają bardziej ponury ton.
- Dodano ambientową warstwę tła (`body::before`) oraz delikatny efekt świetlny w sekcji hero (`.page-hero::after`).
- Wprowadzono dedykowany blok `@media (max-width: 600px)` poprawiający skalowanie strony na smartfonach.

## Aktualizacja fazy 3
- Pojawił się baner "flying object" kierujący do Notebook LM z bazą wiedzy po burzy mózgów, spójny na wszystkich podstronach.
- Animowana ikona zwiadowcy zachowuje klimat ognia, a preferencje ograniczonego ruchu wyłączają animację.
- Test `tests/test_notebook_banner.py` pilnuje obecności linku, etykiety ARIA oraz zabezpieczeń `rel="noopener"`.

## Status fazy
- Plan fazy 1 i zadania: `docs/plan.md`, `docs/tasks.md`.
- Bieżące notatki: `docs/notes.md`.

## Kolejne kroki (propozycja)
- Dodać automatyczny linting HTML/CSS (np. HTMLHint, Stylelint) i włączyć do CI.
- Przygotować komponentowe podejście (np. Eleventy) dla dalszej rozbudowy.
