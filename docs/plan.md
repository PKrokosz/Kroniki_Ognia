# Plan (v1)

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

## Cel fazy 2 — Mobilna mroczna atmosfera
- [Scope] Przygotowanie mobilnego skalowania nagłówka i kart, aby UX działał na ekranach < 600px.
- [Scope] Ujednolicenie palety kolorów na bardziej stonowaną, ponurą z zachowaniem czytelności tekstów.
- [Scope] Dodanie lekkich efektów ambientowych (warstwa tła, pulsujące żarzenie) bez zmiany narracji.
- [Non-Goals] Dynamiczne menu hamburger, pełne przebudowanie treści sekcji, nowe strony.

## Definicja ukończenia fazy 2 (DoD)
- `pytest` przechodzi z nowym testem responsywności.
- Na urządzeniach mobilnych nawigacja układa się w kolumnę, a karty mają zmniejszone paddingi.
- Paleta kolorów została zdesaturowana i udokumentowana w README.
- Akceptacyjne: `tests/test_responsive_theme.py::test_mobile_media_queries_present` oraz `tests/test_responsive_theme.py::test_ambient_effects_defined` są zielone.
