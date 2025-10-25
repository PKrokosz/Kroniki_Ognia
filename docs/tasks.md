## Faza 1 — Standaryzacja
- [x] Zadanie 1: Utworzyć wspólną nawigację i arkusz stylów dla wszystkich stron HTML — Test: `pytest tests/test_navigation.py::test_nav_links_consistent`
- [x] Zadanie 2: Przygotować `index.html` z przeglądem i linkami — Test: ręczna weryfikacja ładowania (opis w README)
- [x] Zadanie 3: Skonfigurować pipeline dokumentacyjny i CI (`docs/*`, `.codex`, workflow) — Test: sprawdzenie obecności plików + `pytest`

## Faza 2 — Mobilna mroczna atmosfera
- [x] Zadanie 1: Przeskalować nagłówek i karty pod ekrany < 600px — Test: `pytest tests/test_responsive_theme.py::test_mobile_media_queries_present`
- [x] Zadanie 2: Przyciemnić paletę i dodać ambientowe efekty — Test: `pytest tests/test_responsive_theme.py::test_ambient_effects_defined`

## Faza 3 — Custom domain i hosting Pages
- [x] Zadanie 1: Udokumentować ręczną konfigurację custom domain bez pliku `CNAME` — Test: `pytest tests/test_custom_domain.py::test_manual_custom_domain_documented`
- [x] Zadanie 1a: Zabezpieczyć repo przed przypadkowym dodaniem `CNAME` — Test: `pytest tests/test_custom_domain.py::test_cname_managed_via_github_settings`
- [ ] Zadanie 2: Przygotować automatyczną weryfikację certyfikatu HTTPS — Test: `pytest tests/test_https_monitoring.py::test_certificate_expiry` (do implementacji)
- [ ] Zadanie 3: Zautomatyzować sprawdzanie wpisu custom domain przez API GitHub Pages — Test: `pytest tests/test_pages_domain_status.py::test_custom_domain_sync` (do zaprojektowania)
## Faza 3 — Integracja bazy wiedzy
- [x] Zadanie 1: Dodać baner "flying object" prowadzący do Notebook LM — Test: `pytest tests/test_notebook_banner.py::test_notebook_banner_present_with_link`
- [ ] Zadanie 2: Streścić kluczowe wnioski z Notebook LM na stronie i dodać test spójności — Test: do zdefiniowania (planowane `tests/test_notebook_summary.py`)

## Faza 4 — Rejestr pomysłów
- [x] Zadanie 1: Formularz "Dodaj pomysł" z walidacją i fetch — Test: ręczna weryfikacja + `pytest tests/test_idea_submission.py::test_submit_idea_persists`
- [x] Zadanie 2: Backend Flask zapisujący do SQLite i pliku — Test: `pytest tests/test_idea_submission.py::test_submit_idea_persists`
- [ ] Zadanie 3 (kontynuacja): Udostępnić panel przeglądania zgłoszonych pomysłów z filtrowaniem — Test: do zaplanowania (`tests/test_idea_listing.py`)
