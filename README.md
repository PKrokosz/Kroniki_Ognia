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

Testy sprawdzają spójność nawigacji na wszystkich podstronach.

## Akceptacja ręczna
- Otwórz `index.html` i upewnij się, że wszystkie linki prowadzą do właściwych stron.
- Zweryfikuj responsywność nagłówka i nawigacji na szerokościach mobilnych.

## Status fazy
- Plan fazy 1 i zadania: `docs/plan.md`, `docs/tasks.md`.
- Bieżące notatki: `docs/notes.md`.

## Kolejne kroki (propozycja)
- Dodać automatyczny linting HTML/CSS (np. HTMLHint, Stylelint) i włączyć do CI.
- Przygotować komponentowe podejście (np. Eleventy) dla dalszej rozbudowy.
