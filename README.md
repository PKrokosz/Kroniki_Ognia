# Kroniki Ognia — Strona Projektowa

Statyczna witryna dokumentująca projekt LARP "Kroniki Ognia". Repozytorium gromadzi stronę główną i podstrony tematyczne wraz z backendem Flask obsługującym formularz zgłaszania pomysłów.

## Struktura
- `index.html` — landing page GitHub Pages.
- `cechy.html`, `draft_planu.html`, `imersja_mechanika.html`, `organizacja.html` — podstrony tematyczne.
- `assets/styles.css` — wspólny arkusz stylów oraz definicje ambientowych teł.
- `assets/editable-tiles.js` — zakładki edycji treści kafelków z pamięcią w `localStorage`.
- `assets/js/backend-config.js` — moduł konfigurujący formularze pod adres tunelu backendu.
- `assets/idea-form.js` — walidacja formularza „Dodaj pomysł” i komunikaty dla użytkownika.
- `assets/visual-key.js` — interakcje sekcji visual key „Próby Płomienia”.
- `docs/` — planowanie faz, zadania, notatki i ADR-y.
- `.codex/` — presety ról Codex.
- `tests/` — testy automatyczne (pytest).
- `.nojekyll` — wymusza statyczne serwowanie plików bez ingerencji Jekylla na GitHub Pages.

## Uruchomienie lokalne
Strony to statyczne pliki HTML. Wystarczy otworzyć plik w przeglądarce lub użyć prostego serwera:

```bash
python -m http.server 8000
```

## Backend formularza „Dodaj pomysł”
Formularz na stronie głównej komunikuje się z lekkim backendem Flask zapisującym wpisy do SQLite oraz dziennika tekstowego. Moduł `assets/js/backend-config.js` odczytuje `config.json` i przypisuje docelowy adres każdemu formularzowi oznaczonemu `data-api`.

Payload ma schemat `{ "title": str, "content": str, "tags": [str]? }`. Każde zgłoszenie trafia do `data/ideas.sqlite3` i `data/ideas.txt` oraz zwraca odpowiedź `201` z `{ "id": "...", "status": "ok", "record_id": "..." }` (gdzie `id` to klucz idempotencji, a `record_id` pochodzi z SQLite). Endpoint `POST /api/ideas` wymaga nagłówka `Content-Type: application/json`, odrzuca payloady większe niż 5 KB i waliduje poprawność JSON-u. W razie błędu zwraca komunikat JSON z kodem 4xx (415 dla błędnego typu, 413 dla zbyt dużego ładunku, 400 dla błędnego JSON-u).

Endpoint `GET /api/health` raportuje gotowość storage (`data/`, SQLite oraz dziennik tekstowy). Limit 10 zgłoszeń na minutę chroni przed floodem, a CORS dopuszcza wyłącznie `https://pkrokosz.github.io`, `https://pkrokosz.github.io/Kroniki_Ognia` oraz `https://*.trycloudflare.com` i explicitnie pozwala na nagłówki `Authorization` oraz `X-API-Key` w preflight.

### Prosty klucz API i forwarding do n8n

- Każde wywołanie `POST /api/ideas` musi przekazać nagłówek `Authorization: Bearer <klucz>` (domyślnie `dev-key`). Dla kompatybilności utrzymujemy także `X-API-Key` — backend honoruje oba warianty, jednak front wysyła je równolegle.
- Formularz front-endowy pobiera wartość klucza z atrybutu `data-api-key` (fallback do `dev-key`) i dołącza ją automatycznie w `assets/idea-form.js` jako `Authorization: Bearer ...` oraz `X-API-Key`.
- Backend domyślnie wysyła każde zgłoszenie na webhook `http://localhost:5678/webhook-test/f11f16e1-4e7e-4fa6-b99e-bf1e47f02a50`. W środowisku produkcyjnym nadpisz go zmienną `N8N_WEBHOOK_URL`; nagłówek autoryzacji `Bearer` jest dołączany tylko wtedy, gdy ustawisz `N8N_TOKEN`.
- Payload do n8n zawiera `event_id` (unikalny klucz idempotencji), dane zgłoszenia oraz metadane klienta (`ip`, `User-Agent`). Dla kompatybilności z lokalnym scenariuszem dodano również sekcję `pomysł` z polskimi polami (`tytuł`, `treść`, `tagi`).
- Po udanym zapisie front-end inicjuje dodatkowe `fetch` pod `https://juaateipzyafdyrf2kdgdlyh.hooks.n8n.cloud/webhook/_health`, przekazując blok `idea` oraz pole `source: "github-pages"` – to natychmiastowy forwarding do produkcyjnego n8n.

```bash
pip install -r requirements.txt
flask --app app run
```

> Domyślnie dane trafiają do `data/ideas.sqlite3` i `data/ideas.txt`. Ścieżkę można nadpisać zmienną `IDEAS_DATA_DIR`.

## Run with tunnel
Statyczny front na GitHub Pages ładuje adres backendu z `config.json` serwowanego wraz z witryną (osiągalnego zarówno pod `/config.json`, jak i `/Kroniki_Ognia/config.json`). Plik `public/config.json` pozostaje referencją w repozytorium i musi być zsynchronizowany.

```json
{
  "BACKEND_URL": "https://humor-classroom-archived-hereby.trycloudflare.com"
}
```

> co robi: wskazuje publiczny adres tunelu bez końcowego ukośnika. Obie kopie `config.json` należy aktualizować jednocześnie, aby testy nie zablokowały wdrożenia.

Po wdrożeniu tunelu front ustawi `form.action` na `${BACKEND_URL}/api/ideas` i wyśle `fetch` do backendu.

### Smoke test tunelu

```bash
# co robi: smoke z publicznego URL (tunel Quick Tunnel)
./scripts/smoke.sh https://humor-classroom-archived-hereby.trycloudflare.com
```

Skrypt wysyła testowy POST i wypisuje odpowiedź JSON.

### Dev: Quick Tunnel → lokalny Flask

```bash
flask run --port 5000                                   # co robi: start backendu lokalnie
cloudflared tunnel --url http://127.0.0.1:5000          # co robi: wystawia publiczny URL *.trycloudflare.com
# Skopiuj URL i ustaw w config.json:
# { "BACKEND_URL": "https://humor-classroom-archived-hereby.trycloudflare.com" }
```

## Hosting GitHub Pages bez Jekylla
- Plik `.nojekyll` w katalogu głównym zapobiega uruchamianiu silnika Jekyll.
- Dzięki temu GitHub Pages serwuje wszystkie zasoby (np. katalog `assets/` i `tests/`) dokładnie tak, jak w repozytorium.
- Test `tests/test_nojekyll.py` pilnuje obecności pliku i wzmianki w README.

## Testy
```bash
pip install -r requirements.txt
ruff check .
mypy app.py
pytest
```

Pakiet testów obejmuje:
- `tests/test_navigation.py` — spójność nawigacji i modułu konfiguracji backendu.
- `tests/test_responsive_theme.py` — media queries dla mobile oraz ambientowe efekty.
- `tests/test_ambient_backgrounds.py` — mapowanie zdjęć JPG, animację `prefers-reduced-motion` oraz widoczność warstw (opacity ≥ 0.45, `z-index` ≥ -1).
- `tests/test_visual_key.py` — sekcję visual key z obrazami `img/1.jpg`, `img/4.jpg`, `img/7.jpg`.
- `tests/test_notebook_banner.py` — baner „flying object” z linkami do Notebook LM i Google Drive.
- `tests/test_config_json.py` — synchronizację `config.json` w katalogu głównym i `public/`.
- `tests/test_idea_submission.py` i `tests/test_api.py` — zapis zgłoszeń, limity oraz health-check.
- `tests/test_feedback_panel.py` — panel „Oceń pomysł” i obsługę `localStorage`.
- `tests/test_custom_domain.py` — dokumentację custom domain i brak pliku `CNAME`.
- `tests/test_documentation.py` — unikalność nagłówków w README, aby uniknąć duplikatów sekcji.

## Kontrola jakości kodu

Nowe narzędzia w `requirements.txt` umożliwiają lokalne uruchomienie lintów i statycznej analizy:

```bash
pip install -r requirements.txt  # instaluje m.in. ruff, mypy i paczki stubów
ruff check .                     # szybki lint Pythona
mypy app.py                      # statyczne typowanie backendu Flask
```

Workflow `.github/workflows/codex.yml` uruchamia `ruff`, `mypy` oraz `pytest` przy każdym pull requeście.

## Aktualne usprawnienia
### Layout responsywny kart i visual key
- Siatki `.cards-grid` korzystają z `repeat(auto-fit, minmax(...))` sterowanego zmienną `--card-min-width`, dzięki czemu karty zachowują proporcje na wąskich i szerokich ekranach.
- Tekst w kartach i sekcjach ma wymuszone `overflow-wrap:anywhere`, co eliminuje problem z nadmiernie długimi słowami i nierównym zawijaniem.
- Kafelki sekcji „Próby Płomienia” renderują fotografie jako rozmyte tła (`filter: blur(...)`) z półprzezroczystym overlayem, pozostawiając czytelny tekst figcaption.

### Ambient i warstwa wizualna
- Podniesiono widoczność animowanych teł: `opacity` warstw osiąga ≥ 0.45, a filtr `saturate(1.35) brightness(1.12)` eksponuje fotografie z `img/`.
- `ambient-background` posiada `z-index: -1`, dzięki czemu dryfujące warstwy znajdują się ponad innymi efektami tła i są weryfikowane testem `tests/test_ambient_backgrounds.py::test_ambient_layers_meet_visibility_thresholds`.

### Higiena dokumentacji
- Zredukowano duplikaty w README, planie, zadaniach, notatkach i CONTEXT — nagłówki są unikalne i odzwierciedlają aktualny stan repozytorium.
- Dodano test `tests/test_documentation.py`, który blokuje ponowne pojawienie się zduplikowanych nagłówków README.
- Rozszerzono strażnika dokumentacji o katalog `docs/adr/`, dzięki czemu każdy ADR musi mieć unikalny tytuł pilnowany przez `tests/test_documentation.py::test_adr_headings_unique`.

### Infrastruktura CI
- Workflow `codex.yml` wykonuje `ruff check .`, `mypy app.py` i `pytest`, aby spełnić wymagania CTO persony dotyczące lintów oraz analizy typów.

### Edycja kafelków
- Każdy kafelek tekstowy (`.plan-card`, `.feature-card`, `.tool-card`, `.card-popiol`, `.focus-card`, `.timeline-card`) otrzymał zakładkę „Edytuj” po prawej krawędzi.
- Po otwarciu zakładki zawartość kafelka przechodzi w tryb `contenteditable`; zapis utrwala zmiany w `localStorage`, a komunikat `aria-live` potwierdza operację.
- Brak dostępu do `localStorage` blokuje edycję i wyświetla globalne powiadomienie o konieczności odblokowania pamięci przeglądarki.
- Test `tests/test_editable_tiles.py` pilnuje obecności modułu JS na każdej stronie i obecności styli dla zakładki oraz fallbacku.

## Aktualizacja fazy 1
- Ujednolicona nawigacja i styl wszystkich stron HTML; test `tests/test_navigation.py` pilnuje spójności.
- Przygotowano `index.html` jako landing page dla GitHub Pages.
- Ustanowiono dokumentację procesową (AGENTS, CONTEXT, plan, zadania, notatki) i workflow CI.

## Aktualizacja fazy 2
- Paleta została przygaszona, a ambientowe efekty rozszerzono o trzywarstwowe tła z katalogu `img/`.
- Blok `@media (max-width: 600px)` zapewnia komfortową nawigację na urządzeniach mobilnych.
- Sekcja visual key „Próby Płomienia” łączy narrację z obrazami `img/1.jpg`, `img/4.jpg`, `img/7.jpg` i udostępnia przycisk autoodtwarzania respektujący `prefers-reduced-motion`.

## Aktualizacja fazy 3
- Dodano baner „flying object” prowadzący do Notebook LM i archiwum Google Drive; test `tests/test_notebook_banner.py` pilnuje ikon i linków.
- W repo znajduje się `.nojekyll`, a README dokumentuje jego rolę.
- Dokumentacja custom domain wskazuje host `pkr0kosz.github.io`, ręczną konfigurację w ustawieniach Pages oraz brak pliku `CNAME` w repo.

## Aktualizacja fazy 4
- Strona „Organizacja” oferuje panel komentarza „Oceń pomysł” zapisujący notatki w `localStorage`.
- Landing posiada formularz „Dodaj pomysł” z walidacją i fetch; backend zapisuje dane do SQLite i pliku tekstowego.

## Aktualizacja fazy 5
- Moduł `assets/js/backend-config.js` scala pobieranie `BACKEND_URL` i przypisuje akcje formularzom oznaczonym `data-api`.
- Skrypt `scripts/smoke.sh` pomaga szybko zweryfikować tunel produkcyjny.
- Endpoint `/api/health` raportuje gotowość storage i jest chroniony testem `tests/test_api.py::test_health_ok`.
- Formularz „Dodaj pomysł” wysyła równocześnie nagłówki `Authorization: Bearer <klucz>` i `X-API-Key`, a backend honoruje oba warianty.
- Po sukcesie zapisu front-end wykonuje dodatkowy webhook na produkcyjny adres n8n Cloud, co pilnuje redundancji w razie awarii tunelu.

## Akceptacja ręczna
- Otwórz `index.html` i sprawdź, że wszystkie linki prowadzą do właściwych stron.
- Zweryfikuj responsywność nagłówka i nawigacji na szerokościach mobilnych.
- Oceń stonowaną paletę, pulsujące tło oraz trzywarstwowe galerie obrazów — powinny być wyraźnie widoczne i dryfować horyzontalnie.
- Kliknij baner Notebook LM oraz CTA Google Drive, aby upewnić się, że otwierają właściwe zasoby.
- Uruchom backend (`flask --app app run`), wprowadź pomysł w sekcji „Dodaj pomysł” i sprawdź, że otrzymasz potwierdzenie oraz nowe wpisy w katalogu `data/`.
- Przejdź przez sekcję visual key i potwierdź, że kafelki reagują na focus/hover, a przycisk „Odtwórz sekwencję” komunikuje status.

## Konfiguracja domeny `www.larpkronikiognia.pl`
1. **GitHub Pages:** w ustawieniach Pages wskaż domenę `www.larpkronikiognia.pl`. Repozytorium nie przechowuje pliku `CNAME`; GitHub utworzy go automatycznie w gałęzi serwującej stronę.
2. **Rekordy DNS:** dodaj rekord `CNAME` dla hosta `www`, wskazujący na `pkr0kosz.github.io`. Opcjonalnie skonfiguruj domenę lustrzaną `www.larpkronikiognia.com` z przekierowaniem 301 na `.pl`.
3. **Domena główna:** aby `larpkronikiognia.pl` kierowała na `www`, dodaj rekordy `A` na adresy `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` lub użyj `ALIAS/ANAME`.
4. **HTTPS:** po propagacji DNS (zwykle do 24h) wymuś opcję „Enforce HTTPS” w ustawieniach Pages.
5. **Weryfikacja:** sprawdź konfigurację poleceniami `dig www.larpkronikiognia.pl CNAME` oraz `curl -I https://www.larpkronikiognia.pl`. Dla domeny `.com` powtórz `dig www.larpkronikiognia.com CNAME`.

## Sekcja visual key „Próby Płomienia”
- Trzy kafelki narracyjne prowadzą do kluczowych podstron repozytorium.
- Każdy kafelek wykorzystuje fotografie `img/1.jpg`, `img/4.jpg`, `img/7.jpg` i CTA zachęcające do eksploracji świata, narzędzi i planu dnia.
- Przycisk „Odtwórz sekwencję” respektuje `prefers-reduced-motion` i komunikuje status przez `aria-live`.

## Status fazy
- Plan i zadania: `docs/plan.md`, `docs/tasks.md`.
- Bieżące notatki: `docs/notes.md`.
- Decyzje architektoniczne: `docs/adr/`.
