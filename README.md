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

Testy sprawdzają spójność nawigacji na wszystkich podstronach, obecność mobilnych styli i ambientowych efektów w `assets/styles.css` (`tests/test_responsive_theme.py`), a także to, że konfiguracja domeny jest udokumentowana jako proces ręczny w ustawieniach GitHub Pages (`tests/test_custom_domain.py`).
Testy kontrolują integralność banera kierującego do bazy wiedzy Notebook LM (`tests/test_notebook_banner.py`) oraz nowego panelu komentarzy przy wątkach (`tests/test_feedback_panel.py`).

## Akceptacja ręczna
- Otwórz `index.html` i upewnij się, że wszystkie linki prowadzą do właściwych stron.
- Zweryfikuj responsywność nagłówka i nawigacji na szerokościach mobilnych (układ kolumnowy, zmniejszone paddingi kart).
- Oceń nową, stonowaną paletę i subtelny efekt pulsującego tła w kontekście narracji projektu.
- Kliknij baner Notebook LM i sprawdź, czy otwiera się właściwy notebook z bazą wiedzy brainstormu.

## Konfiguracja domeny `www.larpkronikiognia.pl`
1. **GitHub Pages (repozytorium):** w ustawieniach Pages wskaż domenę `www.larpkronikiognia.pl`. Repozytorium nie przechowuje pliku `CNAME`; GitHub Pages zapisze go automatycznie w gałęzi serwującej stronę.
2. **Rekordy DNS dla poddomeny:** w panelu operatora domeny dodaj rekord `CNAME` dla hosta `www`, wskazujący na adres GitHub Pages organizacji/profilu (np. `larpkronikiognia.github.io`). Wartość możesz potwierdzić w ustawieniach Pages.
3. **Rekordy dla domeny głównej:** aby `larpkronikiognia.pl` przekierowywała na `www`, dodaj rekordy `A` na adresy `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` (zalecane przez GitHub) lub skorzystaj z `ALIAS/ANAME`, jeśli dostawca je udostępnia.
4. **HTTPS:** po propagacji DNS (zwykle do 24h) wymuś opcję „Enforce HTTPS” w ustawieniach Pages.
5. **Weryfikacja:** sprawdź poprawność przez `dig www.larpkronikiognia.pl CNAME` oraz `curl -I https://www.larpkronikiognia.pl` — oba polecenia powinny wskazywać na GitHub Pages i zwracać status 200. Repozytorium nie przechowuje pliku `CNAME`, więc po każdej zmianie domeny potwierdź w ustawieniach Pages, że wpis został zapisany.

## Konfiguracja domeny `www.larpkronikiognia.pl`
1. **GitHub Pages (repozytorium):** w ustawieniach Pages wskaż domenę `www.larpkronikiognia.pl`. Repozytorium nie przechowuje pliku `CNAME`; GitHub Pages zapisze go automatycznie w gałęzi serwującej stronę.
2. **Rekordy DNS dla poddomeny:** w panelu operatora domeny dodaj rekord `CNAME` dla hosta `www`, wskazujący na właściwy adres GitHub Pages profilu `pkr0kosz.github.io`. GitHub wymaga dokładnie takiej wartości; alternatywne warianty (`larpkronikiognia.github.io`) spowodują błąd weryfikacji jak na zrzucie ekranu w Issues.
3. **Opcjonalna domena lustrzana:** jeżeli posiadasz także `www.larpkronikiognia.com`, dodaj identyczny rekord `CNAME` na `pkr0kosz.github.io` i ustaw przekierowanie 301 z `.com` do `.pl`, aby uniknąć duplikacji treści.
4. **Rekordy dla domeny głównej:** aby `larpkronikiognia.pl` przekierowywała na `www`, dodaj rekordy `A` na adresy `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` (zalecane przez GitHub) lub skorzystaj z `ALIAS/ANAME`, jeśli dostawca je udostępnia.
5. **HTTPS:** po propagacji DNS (zwykle do 24h) wymuś opcję „Enforce HTTPS” w ustawieniach Pages.
6. **Weryfikacja:** sprawdź poprawność przez `dig www.larpkronikiognia.pl CNAME` oraz `curl -I https://www.larpkronikiognia.pl` — oba polecenia powinny wskazywać na GitHub Pages i zwracać status 200. Repozytorium nie przechowuje pliku `CNAME`, więc po każdej zmianie domeny potwierdź w ustawieniach Pages, że wpis został zapisany. Dla domeny `.com` powtórz kontrolę (`dig www.larpkronikiognia.com CNAME`).

## Aktualizacja fazy 2
- Paleta kolorów została przygaszona i oparta na barwach ziemistych; akcenty złamane bursztynem nadają bardziej ponury ton.
- Dodano ambientową warstwę tła (`body::before`) oraz delikatny efekt świetlny w sekcji hero (`.page-hero::after`).
- Wprowadzono dedykowany blok `@media (max-width: 600px)` poprawiający skalowanie strony na smartfonach.

## Aktualizacja fazy 3
- Pojawił się baner "flying object" kierujący do Notebook LM z bazą wiedzy po burzy mózgów, spójny na wszystkich podstronach.
- Animowana ikona zwiadowcy zachowuje klimat ognia, a preferencje ograniczonego ruchu wyłączają animację.
- Test `tests/test_notebook_banner.py` pilnuje obecności linku, etykiety ARIA oraz zabezpieczeń `rel="noopener"`.

## Aktualizacja fazy 4
- Sekcja "Organizacja" oferuje panel komentarza przy każdym wątku — rozwijany przyciskiem "Oceń pomysł" i zapisujący notatki w `localStorage`.
- Styl panelu wpisuje się w bursztynową paletę repozytorium i respektuje układ mobilny.
- Test `tests/test_feedback_panel.py` pilnuje obecności znaczników danych oraz styli komponentu.

## Status fazy
- Plan fazy 1 i zadania: `docs/plan.md`, `docs/tasks.md`.
- Bieżące notatki: `docs/notes.md`.

## Kolejne kroki (propozycja)
- Dodać automatyczny linting HTML/CSS (np. HTMLHint, Stylelint) i włączyć do CI.
- Przygotować komponentowe podejście (np. Eleventy) dla dalszej rozbudowy.
