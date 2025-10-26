## Faza 1 — Standaryzacja
- [x] Zadanie 1: Utworzyć wspólną nawigację i arkusz stylów dla wszystkich stron HTML — Test: `pytest tests/test_navigation.py::test_nav_links_consistent`
- [x] Zadanie 2: Przygotować `index.html` z przeglądem i linkami — Test: ręczna weryfikacja ładowania (opis w README)
- [x] Zadanie 3: Skonfigurować pipeline dokumentacyjny i CI (`docs/*`, `.codex`, workflow) — Test: `pytest`
- [x] Zadanie 4: Rozszerzyć toolchain backendu o `ruff` i `mypy` — Test: `ruff check .`, `mypy app.py`
- [x] Zadanie 5: Oczyścić dokumentację z duplikatów i dodać strażnika nagłówków README — Test: `pytest tests/test_documentation.py`
- [x] Zadanie 5a: Rozszerzyć strażnika dokumentacji o `docs/` (plan, notes, tasks, CONTEXT) — Test: `pytest tests/test_documentation.py::test_docs_headings_unique`
- [x] Zadanie 5b: Rozszerzyć walidację nagłówków na katalog `docs/adr/` (tytuły ADR muszą być unikalne) — Test: `pytest tests/test_documentation.py::test_adr_headings_unique`
- [ ] Zadanie 6: Dodać lokalny alias (np. `make lint`) agregujący `ruff`, `mypy`, `pytest` — Test: do zaprojektowania (`tests/test_cli_tasks.py::test_make_lint_runs_tools`)
- [ ] Zadanie 7: Zautomatyzować kontrolę `.gitignore` w CI — Test: do zdefiniowania (`tests/test_gitignore_guard.py`)

## Faza 2 — Mobilna mroczna atmosfera
- [x] Zadanie 1: Przeskalować nagłówek i karty pod ekrany < 600px — Test: `pytest tests/test_responsive_theme.py::test_mobile_media_queries_present`
- [x] Zadanie 2: Przyciemnić paletę i dodać ambientowe efekty — Test: `pytest tests/test_responsive_theme.py::test_ambient_effects_defined`
- [x] Zadanie 3: Zaprojektować rozmyte, animowane tła z trzema obrazami na podstronę — Test: `pytest tests/test_ambient_backgrounds.py`
- [x] Zadanie 4: Zapewnić widoczność warstw ambient (opacity ≥ 0.45, `z-index` ≥ -1) — Test: `pytest tests/test_ambient_backgrounds.py::test_ambient_layers_meet_visibility_thresholds`
- [x] Zadanie 5: Wprowadzić sekcję visual key z trzema progami narracyjnymi i testem — Test: `pytest tests/test_visual_key.py::test_visual_key_section_present`
- [x] Zadanie 8: Ustandaryzować siatki kart poprzez `repeat(auto-fit, minmax(...))` i `--card-min-width` — Test: `pytest tests/test_responsive_theme.py::test_cards_grid_auto_fit`
- [x] Zadanie 9: Zamienić fotografie visual key na rozmyte tła z kontrolą opacity — Test: `pytest tests/test_responsive_theme.py::test_visual_key_images_blurred`
- [ ] Zadanie 6: Sterować prędkością warstw tła zależnie od scrolla (`prefers-reduced-motion`, IntersectionObserver) — Test: do zaprojektowania (`tests/test_ambient_backgrounds.py::test_scroll_speed_variant`)
- [ ] Zadanie 7: Zaprojektować tryb akcentowy zwiększający ekspozycję warstw w sekcjach CTA — Test: do zaprojektowania (`tests/test_ambient_backgrounds.py::test_section_accent_visibility`)

## Faza 3 — Custom domain i hosting Pages
- [x] Zadanie 1: Udokumentować ręczną konfigurację custom domain bez pliku `CNAME` — Test: `pytest tests/test_custom_domain.py::test_manual_custom_domain_documented`
- [x] Zadanie 1a: Zabezpieczyć repo przed przypadkowym dodaniem `CNAME` — Test: `pytest tests/test_custom_domain.py::test_cname_managed_via_github_settings`
- [x] Zadanie 1b: Ustalić właściwy rekord `CNAME` na `pkr0kosz.github.io` (wraz z opcją `.com`) — Test: `pytest tests/test_custom_domain.py::test_dns_host_documented`
- [x] Zadanie 2: Dodać `.nojekyll` i test weryfikujący statyczne serwowanie GitHub Pages — Test: `pytest tests/test_nojekyll.py::test_nojekyll_file_present`
- [ ] Zadanie 3: Przygotować automatyczną weryfikację certyfikatu HTTPS — Test: do zaprojektowania (`tests/test_https_monitoring.py::test_certificate_expiry`)
- [ ] Zadanie 4: Zautomatyzować sprawdzanie wpisu custom domain przez API GitHub Pages — Test: do zaprojektowania (`tests/test_pages_domain_status.py::test_custom_domain_sync`)

## Faza 3 — Integracja bazy wiedzy
- [x] Zadanie 1: Dodać baner "flying object" prowadzący do Notebook LM — Test: `pytest tests/test_notebook_banner.py::test_notebook_banner_present_with_link`
- [x] Zadanie 1b: Rozszerzyć baner o link do archiwum Google Drive i ikonę — Test: `pytest tests/test_notebook_banner.py::test_notebook_banner_includes_drive_archive_link`
- [ ] Zadanie 2: Streścić kluczowe wnioski z Notebook LM na stronie i dodać test spójności — Test: do zdefiniowania (`tests/test_notebook_summary.py`)
- [ ] Zadanie 3: Przygotować health-check spójności zasobów Google Drive (API lub manualny workflow) — Test: do zaprojektowania (`tests/test_drive_inventory.py`)

## Faza 4 — Pętle feedbacku
- [x] Zadanie 1: Udostępnić panel "Oceń pomysł" z lokalnym zapisem komentarzy — Test: `pytest tests/test_feedback_panel.py::test_feedback_toggle_markup_present`
- [x] Zadanie 1a: Zapewnić style i układ mobilny panelu komentarzy — Test: `pytest tests/test_feedback_panel.py::test_feedback_styles_defined`
- [ ] Zadanie 2: Zaplanować synchronizację komentarzy między urządzeniami (eksport/import JSON) — Test: `pytest tests/test_feedback_panel.py::test_feedback_export_placeholder`

## Faza 4 — Rejestr pomysłów
- [x] Zadanie 1: Formularz "Dodaj pomysł" z walidacją i fetch — Test: `pytest tests/test_idea_submission.py::test_submit_idea_persists`
- [x] Zadanie 2: Backend Flask zapisujący do SQLite i pliku — Test: `pytest tests/test_idea_submission.py::test_submit_idea_persists`
- [ ] Zadanie 3: Udostępnić panel przeglądania zgłoszonych pomysłów z filtrowaniem — Test: do zaplanowania (`tests/test_idea_listing.py`)

## Faza 5 — Tunel backendu
- [x] Zadanie 1: Wczytać `BACKEND_URL` z `public/config.json` i ustawiać `form.action` dynamicznie — Test: `pytest tests/test_api.py::test_post_ideas_smoke`
- [x] Zadanie 1c: Udostępnić `config.json` w katalogu głównym repozytorium — Test: `pytest tests/test_config_json.py::test_root_and_public_configs_match`
- [x] Zadanie 2: Dostosować backend do schematu `{title, content, tags}` z CORS i rate limitem 10/min — Test: `pytest tests/test_idea_submission.py::test_submit_idea_persists`
- [x] Zadanie 3: Dodać `scripts/smoke.sh` oraz sekcję README „Run with tunnel” — Test: `pytest tests/test_api.py::test_post_ideas_smoke`
- [x] Zadanie 3b: Dodać `GET /api/health` i test zdrowia backendu — Test: `pytest tests/test_api.py::test_health_ok`
- [x] Zadanie 4: Utwardzić walidację JSON (`Content-Type`, limit 5 KB, błąd parsowania) — Test: `pytest tests/test_api.py::test_post_ideas_rejects_non_json_content_type`
- [x] Zadanie 10: Wysłać zgłoszenia do n8n z kluczem `X-API-Key` — Test: `pytest tests/test_api.py::test_post_ideas_forwards_to_n8n`
- [x] Zadanie 10b: Dodać alias `pomysł` w payloadzie forwardingowym i domyślny webhook dev — Test: `pytest tests/test_api.py::test_post_ideas_forwards_to_n8n`
- [x] Zadanie 10c: Wysłać po stronie frontu bezpośredni webhook produkcyjny n8n Cloud — Test: `pytest tests/test_frontend_forwarding.py::test_production_webhook_forwarding_script`
- [ ] Zadanie 10d: Monitorować odpowiedź webhooka n8n Cloud i logować statusy w konsoli (bez blokowania UX) — Test: do zaprojektowania (`tests/test_frontend_forwarding.py::test_production_webhook_monitoring_placeholder`)
- [x] Zadanie 11: Rozszerzyć CORS o nagłówki autoryzacji i dodać test preflight — Test: `pytest tests/test_api.py::test_cors_allows_authorization_and_api_key_headers`
- [x] Zadanie 12: Dołączyć nagłówek `Authorization: Bearer` w formularzu i backendzie — Test: `pytest tests/test_api.py::test_post_ideas_smoke`
- [ ] Zadanie 13: Przenieść klucz API do zaszyfrowanego storage i dodać rotację tokenów — Test: do zaprojektowania (`tests/test_api.py::test_api_key_rotation_schedule`)
- [ ] Zadanie 5: Przygotować skrypt synchronizujący `config.json` między katalogiem głównym a `public/` — Test: do zaprojektowania (`tests/test_config_json.py::test_sync_script`)
- [ ] Zadanie 6: Zintegrować monitor health-checka z alertem (np. cron + webhook) — Test: do zaprojektowania (`tests/test_tunnel_health.py::test_health_alert_workflow`)
- [ ] Zadanie 7: Zautomatyzować smoke tunelu z użyciem GitHub Actions cron i raportu w issues — Test: do zaprojektowania (`tests/test_tunnel_health.py::test_cron_monitoring`)
- [ ] Zadanie 8: Zasymulować w testach front-endowych niedostępność `config.json` i wymusić komunikat fallback w UI — Test: do implementacji (`tests/test_navigation.py::test_backend_config_error_state`)
- [ ] Zadanie 9: Zautomatyzować test E2E łączący Quick Tunnel z frontem (`wireBackendForms` + fetch) — Test: do zaprojektowania (`tests/test_tunnel_e2e.py::test_submit_via_configured_form`)

## Faza 6 — Kuracja treści kafelków
- [x] Zadanie 1: Udostępnić zakładki edycji treści kafelków z zapisem w `localStorage` — Test: `pytest tests/test_editable_tiles.py::test_editable_tiles_module_loaded`
- [x] Zadanie 1a: Zaprojektować fallback UI przy braku `localStorage` i udokumentować proces — Test: `pytest tests/test_editable_tiles.py::test_editable_tiles_fallback_documented`
- [ ] Zadanie 2: Zasymulować synchronizację edytowanych kafelków przez eksport JSON (proof-of-concept) — Test: do zaplanowania (`tests/test_editable_tiles.py::test_tile_export_placeholder`)
