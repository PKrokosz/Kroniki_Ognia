# Plan (v2)

## Cel fazy 1 — Standaryzacja strony i pipeline'u
- [Scope] Ujednolicona nawigacja i styl wszystkich stron HTML, przygotowanie `index.html` dla GitHub Pages.
- [Scope] Ustanowienie dokumentacji procesowej (AGENTS, CONTEXT, plan, zadania, notatki) i workflow CI.
- [Non-Goals] Nowa zawartość fabularna, rozbudowane funkcje JS poza nawigacją.

## Definicja ukończenia (DoD)
- `ruff check .`, `mypy app.py`, `pytest` przechodzą zielono.
- Wszystkie strony korzystają ze wspólnego arkusza `assets/styles.css` i dzielonej nawigacji.
- Istnieje `index.html` jako strona startowa GitHub Pages.
- Dokumentacja (README, notes, tasks) odzwierciedla aktualny stan.
- Akceptacja: `tests/test_navigation.py::test_nav_links_consistent` przechodzi.

## Ryzyka
- Brak automatycznego lintowania HTML — do rozważenia w kolejnej fazie.
- Możliwe rozbieżności między istniejącym tekstem a nowym layoutem (ryzyko złamania zasady zachowania treści).

## Cel fazy 2 — Mobilna mroczna atmosfera
- [Scope] Przygotowanie mobilnego skalowania nagłówka i kart, aby UX działał na ekranach < 600px.
- [Scope] Ujednolicenie palety kolorów na bardziej stonowaną, ponurą z zachowaniem czytelności tekstów.
- [Scope] Dodanie ambientowych teł bazujących na fotografiach JPG (`img/`) wraz z animacją dryfu.
- [Scope] Sekcja visual key na landingu wykorzystująca fotografie z `img/` i prowadząca do kluczowych podstron.
- [Non-Goals] Dynamiczne menu hamburger, pełne przebudowanie treści sekcji, nowe strony.

## Definicja ukończenia fazy 2 (DoD)
- `pytest` przechodzi z testami responsywności oraz ambientu.
- Na urządzeniach mobilnych nawigacja układa się w kolumnę, a karty mają zmniejszone paddingi.
- Paleta kolorów została zdesaturowana i udokumentowana w README.
- Ambientowe warstwy tła mają opacity ≥ 0.45 i `z-index` ≥ -1, co chroni test `tests/test_ambient_backgrounds.py::test_ambient_layers_meet_visibility_thresholds`.
- Akceptacja: `tests/test_responsive_theme.py`, `tests/test_ambient_backgrounds.py`, `tests/test_visual_key.py`.

## Cel fazy 3 — Custom domain i hosting Pages
- [Scope] Zapewnienie testu kontrolującego brak pliku `CNAME` w repozytorium oraz kompletność dokumentacji ręcznej konfiguracji domeny.
- [Scope] Udokumentowanie kroków DNS i procedury weryfikacji w README oraz `docs/notes.md` wraz z logiem 5xWhy.
- [Scope] Przygotowanie checklisty do monitorowania dostępności i certyfikatu HTTPS.
- [Non-Goals] Automatyczne narzędzia monitoringu uptime, wdrożenia CD poza GitHub Pages, zakup certyfikatów zewnętrznych.

## Definicja ukończenia fazy 3 — Custom domain (DoD)
- `tests/test_custom_domain.py` potwierdza brak pliku `CNAME` i aktualną dokumentację hosta `pkr0kosz.github.io` (wraz z opcją `.com`).
- README opisuje kroki konfiguracji DNS i brak pliku `CNAME`; `docs/notes.md` zawiera log 5xWhy.
- `docs/tasks.md` zawiera checklistę custom domain i plan monitoringu certyfikatu.
- Akceptacja: ręczna weryfikacja `dig`/`curl` udokumentowana w README.

## Cel fazy 3 — Integracja bazy brainstormu
- [Scope] Udostępnić wspólny baner „flying object” kierujący do Notebook LM i archiwum Google Drive.
- [Scope] Zachować narracyjny klimat i dostępność (prefers-reduced-motion, aria-live, mobilny układ).
- [Non-Goals] Embedowanie Notebook LM, synchronizacja treści w czasie rzeczywistym.

## Definicja ukończenia fazy 3 — Integracja bazy brainstormu (DoD)
- `tests/test_notebook_banner.py` potwierdza obecność linków, ikon i klas banera.
- Baner Notebook LM widoczny i funkcjonalny na każdej podstronie repo.
- Dokumentacja (README, notes) opisuje CTA i sposób ręcznej weryfikacji.

## Cel fazy 4 — Pętle feedbacku uczestników
- [Scope] Umożliwić komentowanie wątków na stronie „Organizacja” poprzez panel „Oceń pomysł”.
- [Scope] Zapewnić obsługę `localStorage`, komunikaty statusu oraz responsywną stylistykę.
- [Non-Goals] Synchronizacja komentarzy między urządzeniami, moderacja online, backend.

## Definicja ukończenia fazy 4 — Pętle feedbacku (DoD)
- `tests/test_feedback_panel.py` potwierdza obecność komponentu i styli.
- Panel komentarzy domyślnie zwinięty, obsługuje `localStorage` i komunikaty statusu.
- README oraz notatki dokumentują sposób użycia panelu i testy.

## Cel fazy 4 — Rejestr pomysłów uczestników
- [Scope] Udostępnić na stronie głównej formularz „Dodaj pomysł” z walidacją i informacją zwrotną.
- [Scope] Zapisać zgłoszenia w trwałej bazie danych oraz równoległym pliku tekstowym do audytu narracyjnego.
- [Scope] Zapewnić backend Flask wraz z testem kontraktowym i dokumentacją procesu.
- [Non-Goals] Publiczne wyświetlanie listy pomysłów, moderacja treści, uwierzytelnianie użytkowników.

## Definicja ukończenia fazy 4 — Rejestr pomysłów (DoD)
- `tests/test_idea_submission.py` i `tests/test_api.py` potwierdzają zapis zgłoszenia i kontrakt API.
- Formularz korzysta z fetch, komunikuje status przez `aria-live` i wykorzystuje `data-api` + `wireBackendForms`.
- README, notes oraz ADR dokumentują architekturę formularza i kroki uruchomienia backendu.

## Cel fazy 5 — Tunelowany backend Pages ↔ Flask
- [Scope] Konfiguracja frontu do wczytywania `BACKEND_URL` z `config.json` i ustawiania `form.action` po stronie klienta.
- [Scope] Dodanie smoke testów i skryptu CLI do walidacji tunelu.
- [Scope] Wymuszenie limitu 10/min na `POST /api/ideas` (Flask-Limiter) oraz kontrola CORS.
- [Scope] Zapewnienie health-checka JSON raportującego gotowość storage.
- [Non-Goals] Pełna autoryzacja żądań, zarządzanie tajnymi tokenami, publikacja listy pomysłów w UI.

## Definicja ukończenia fazy 5 (DoD)
- `tests/test_api.py` obejmuje smoke dla `/api/ideas` i `/api/health`.
- `config.json` jest serwowany zarówno z katalogu głównego, jak i `public/` (`tests/test_config_json.py`).
- `scripts/smoke.sh` opisany w README umożliwia walidację tunelu.
- README zawiera sekcję „Dev: Quick Tunnel → lokalny Flask” prowadzącą przez uruchomienie tunelu.
- CORS i rate limit skonfigurowane w `app.py`; ADR/notes zawierają analizę 5xWhy tunelu.
- Health-check i walidacja JSON są chronione testami (`tests/test_api.py`).

## Cel fazy 6 — Kuracja treści kafelków
- [Scope] Udostępnić edycję tekstów kafelków przez zakładki po prawej stronie oraz pamięć w `localStorage`.
- [Scope] Zapewnić fallback UI informujący o blokadzie zapisu przy wyłączonym `localStorage`.
- [Scope] Ujednolicić logikę edycji w dedykowanym module JS z testami regresji i dokumentacją procesu.
- [Non-Goals] Synchronizacja zmian między urządzeniami, wersjonowanie edytowanych treści, backendowy zapis kafelków.

## Definicja ukończenia fazy 6 — Kuracja treści kafelków (DoD)
- `assets/editable-tiles.js` dodaje zakładki edycji do wszystkich kafelków tekstowych i obsługuje zapis w `localStorage`.
- Fallback przy braku `localStorage` komunikuje niedostępność edycji i blokuje tryb zapisu.
- README i notes opisują sposób edycji oraz log zdarzeń 5xWhy; test `tests/test_editable_tiles.py` pilnuje obecności modułu i styli.
