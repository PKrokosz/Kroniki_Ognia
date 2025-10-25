# Kroniki Ognia — Strona Projektowa

Statyczna witryna dokumentująca projekt LARP "Kroniki Ognia". Repozytorium zawiera stronę główną oraz szczegółowe podstrony z analizą fabularną i organizacyjną.

## Struktura
- `index.html` — landing page GitHub Pages.
- `cechy.html`, `draft_planu.html`, `imersja_mechanika.html`, `organizacja.html` — podstrony tematyczne.
- `assets/styles.css` — wspólny arkusz stylów.
- `assets/js/backend-config.js` — moduł konfigurujący formularze pod adres tunelu backendu.
- `docs/` — planowanie faz, zadania, notatki, ADR.
- `.codex/` — presety ról Codex.
- `tests/` — testy automatyczne (pytest).

## Uruchomienie lokalne
Strony to statyczne pliki HTML. Wystarczy otworzyć dowolny plik w przeglądarce lub użyć prostego serwera:

```bash
python -m http.server 8000
```

## Backend formularza „Dodaj pomysł”
Formularz na stronie głównej komunikuje się z lekkim backendem Flask zapisującym wpisy do SQLite oraz dziennika tekstowego. Wspólny moduł `assets/js/backend-config.js` odczytuje `config.json` i przypisuje docelowy adres każdemu formularzowi oznaczonemu `data-api`.

Payload ma schemat `{"title": str, "content": str, "tags": [str]?}`. Każde zgłoszenie trafia do `data/ideas.sqlite3` i `data/ideas.txt` oraz zwraca odpowiedź `201` z `{ "id": "...", "status": "ok" }`.

```bash
pip install -r requirements.txt
flask --app app run
```

> Domyślnie dane trafiają do `data/ideas.sqlite3` i `data/ideas.txt`. Ścieżkę można nadpisać zmienną `IDEAS_DATA_DIR`.
> Endpoint `POST /api/ideas` posiada limit 10 zgłoszeń na minutę z jednego adresu IP oraz nagłówki CORS dla GitHub Pages i tunelu.

## Run with tunnel

Statyczny front na GitHub Pages ładuje adres backendu z `config.json` serwowanego wraz z witryną (osiągalnego zarówno pod `/config.json`, jak i `/Kroniki_Ognia/config.json`). Plik `public/config.json` pozostaje referencją do utrzymania konfiguracji w repozytorium i musi pozostawać zsynchronizowany.

```json
{
  "BACKEND_URL": "https://random-words-1234.trycloudflare.com"
}
```

> co robi: wskazuje publiczny adres tunelu bez końcowego ukośnika. Obie kopie `config.json` należy aktualizować jednocześnie, aby testy nie zablokowały wdrożenia.

Po wdrożeniu tunelu backend Flask powinien być osiągalny pod podanym adresem. Formularz ustawi `form.action` oraz wywoła `fetch` na `${BACKEND_URL}/api/ideas`.

### Smoke test tunelu

```bash
# co robi: smoke z publicznego URL (tunnel)
./scripts/smoke.sh https://api-kroniki.<MOJA-DOMENA>
```

Skrypt wysyła testowy POST i wypisuje odpowiedź JSON.

## Testy
```bash
pip install -r requirements.txt
pytest
```

Testy sprawdzają spójność nawigacji na wszystkich podstronach, obecność mobilnych styli i ambientowych efektów w `assets/styles.css` (`tests/test_responsive_theme.py`), a także to, że konfiguracja domeny jest udokumentowana jako proces ręczny w ustawieniach GitHub Pages (`tests/test_custom_domain.py`).
Testy sprawdzają spójność nawigacji na wszystkich podstronach, obecność mobilnych styli i ambientowych efektów w `assets/styles.css` (`tests/test_responsive_theme.py`), integralność banera kierującego do bazy wiedzy Notebook LM (`tests/test_notebook_banner.py`), trójwarstwowe tła wykorzystujące zdjęcia z katalogu `img/` (`tests/test_ambient_backgrounds.py`) oraz zapis formularza „Dodaj pomysł” zarówno w bazie, jak i w pliku (`tests/test_idea_submission.py`). `tests/test_navigation.py::test_backend_config_script_present_on_form_pages` pilnuje dołączania modułu konfiguracji backendu wszędzie tam, gdzie pojawia się formularz.
Testy sprawdzają spójność nawigacji na wszystkich podstronach, obecność mobilnych styli i ambientowych efektów w `assets/styles.css` (`tests/test_responsive_theme.py`), integralność banera kierującego do bazy wiedzy Notebook LM (`tests/test_notebook_banner.py`), trójwarstwowe tła wykorzystujące zdjęcia z katalogu `img/` (`tests/test_ambient_backgrounds.py`), zgodność plików konfiguracyjnych (`tests/test_config_json.py`) oraz zapis formularza „Dodaj pomysł” zarówno w bazie, jak i w pliku (`tests/test_idea_submission.py`).
Testy kontrolują integralność banera kierującego do bazy wiedzy Notebook LM (`tests/test_notebook_banner.py`) oraz nowego panelu komentarzy przy wątkach (`tests/test_feedback_panel.py`).
Testy sprawdzają spójność nawigacji na wszystkich podstronach, obecność mobilnych styli i ambientowych efektów w `assets/styles.css` (`tests/test_responsive_theme.py`), integralność banera kierującego do bazy wiedzy Notebook LM (`tests/test_notebook_banner.py`) oraz zapis formularza „Dodaj pomysł” zarówno w bazie, jak i w pliku (`tests/test_idea_submission.py`).
Testy sprawdzają spójność nawigacji na wszystkich podstronach, obecność mobilnych styli i ambientowych efektów w `assets/styles.css` (`tests/test_responsive_theme.py`), integralność banera kierującego do bazy wiedzy Notebook LM (`tests/test_notebook_banner.py`), trójwarstwowe tła wykorzystujące zdjęcia z katalogu `img/` (`tests/test_ambient_backgrounds.py`) oraz zapis formularza „Dodaj pomysł” zarówno w bazie, jak i w pliku (`tests/test_idea_submission.py`).
Smoke `tests/test_api.py` używa wbudowanego klienta Flask, by upewnić się, że `POST /api/ideas` zwraca `{ "status": "ok" }`.

## Akceptacja ręczna
- Otwórz `index.html` i upewnij się, że wszystkie linki prowadzą do właściwych stron.
- Zweryfikuj responsywność nagłówka i nawigacji na szerokościach mobilnych (układ kolumnowy, zmniejszone paddingi kart).
- Oceń nową, stonowaną paletę, subtelny efekt pulsującego tła i wielowarstwowe galerie obrazów przesuwające się horyzontalnie. Sprawdź, czy warstwy tła są widoczne, delikatnie świecą i wolno dryfują na szerokość.
- Oceń nową, stonowaną paletę, subtelny efekt pulsującego tła i wielowarstwowe galerie obrazów przesuwające się horyzontalnie.
- Kliknij baner Notebook LM i sprawdź, czy otwiera się właściwy notebook z bazą wiedzy brainstormu.
- Uruchom backend (`flask --app app run`), wprowadź pomysł w sekcji „Dodaj pomysł” i sprawdź, że otrzymasz potwierdzenie, a w katalogu `data/` pojawiły się wpisy w SQLite i `ideas.txt`.

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
- Każda podstrona posiada trzywarstwowe, rozmyte galerie obrazów z katalogu `img/`, które płynnie przesuwają się horyzontalnie i respektują `prefers-reduced-motion`. Warstwy mają wzmocnioną ekspozycję (większa jasność i saturacja), aby animacja była zauważalna, lecz nadal subtelna.
- Każda podstrona posiada trzywarstwowe, rozmyte galerie obrazów z katalogu `img/`, które płynnie przesuwają się horyzontalnie i respektują `prefers-reduced-motion`.
- Wprowadzono dedykowany blok `@media (max-width: 600px)` poprawiający skalowanie strony na smartfonach.

## Aktualizacja fazy 3
- Pojawił się baner "flying object" kierujący do Notebook LM z bazą wiedzy po burzy mózgów, spójny na wszystkich podstronach.
- Animowana ikona zwiadowcy zachowuje klimat ognia, a preferencje ograniczonego ruchu wyłączają animację.
- Ten sam zwiadowca prowadzi teraz także do archiwum Google Drive z zasobami wizualnymi; ikonę w barwach Google umieściliśmy przy CTA.
- Test `tests/test_notebook_banner.py` pilnuje obecności linków (Notebook LM oraz Google Drive), etykiety ARIA, klas stylujących i zabezpieczeń `rel="noopener"`.

## Aktualizacja fazy 4
- Sekcja "Organizacja" oferuje panel komentarza przy każdym wątku — rozwijany przyciskiem "Oceń pomysł" i zapisujący notatki w `localStorage`.
- Styl panelu wpisuje się w bursztynową paletę repozytorium i respektuje układ mobilny.
- Test `tests/test_feedback_panel.py` pilnuje obecności znaczników danych oraz styli komponentu.

## Aktualizacja fazy 5
- Moduł `assets/js/backend-config.js` scala pobieranie `BACKEND_URL` i przypisuje akcje wszystkim formularzom oznaczonym `data-api`.
- `assets/idea-form.js` korzysta z modułu współdzielonego cache i skupia się wyłącznie na walidacji oraz komunikatach dla użytkownika.
- `tests/test_navigation.py::test_backend_config_script_present_on_form_pages` zabezpiecza dołączanie modułu na stronach z formularzami.

## Status fazy
- Plan fazy 1 i zadania: `docs/plan.md`, `docs/tasks.md`.
- Bieżące notatki: `docs/notes.md`.

## Kolejne kroki (propozycja)
- Dodać automatyczny linting HTML/CSS (np. HTMLHint, Stylelint) i włączyć do CI.
- Przygotować komponentowe podejście (np. Eleventy) dla dalszej rozbudowy.
- Zaprojektować widok prezentujący zgłoszone pomysły wraz z moderacją i eksportem.
