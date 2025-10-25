# Plan (v0)

## Cel fazy 1 — Standaryzacja strony i pipeline'u
- [Scope] Ujednolicona nawigacja i styl wszystkich stron HTML, przygotowanie index.html dla GitHub Pages.
- [Scope] Ustanowienie dokumentacji procesowej (AGENTS, CONTEXT, plan, zadania, notatki) i workflow CI.
- [Non-Goals] Nowa zawartość fabularna, rozbudowane funkcje JS poza nawigacją.

## Definicja ukończenia (DoD)
- Lint, typecheck, test: `pytest` zielony, dodatkowe linty TBD w kolejnych fazach.
- Wszystkie strony korzystają ze wspólnego arkusza `assets/styles.css` i dzielonej nawigacji.
- Istnieje `index.html` jako strona startowa GitHub Pages.
- Dokumentacja (README, notes, tasks) odzwierciedla aktualny stan.
- Akceptacyjne: test `tests/test_navigation.py::test_nav_links_consistent` przechodzi.

## Ryzyka
- Brak automatycznego lintowania HTML — do rozważenia w kolejnej fazie.
- Możliwe rozbieżności między istniejącym tekstem a nowym layoutem (ryzyko złamania zasady zachowania treści).
