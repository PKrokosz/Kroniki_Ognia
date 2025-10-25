# Kontekst

Źródła prawdy:
- `docs/plan.md`
- `docs/tasks.md`
- `AGENTS.md`
- `docs/notes.md`
- Bieżące ADR w `docs/adr/`
- Backend Flask (`app.py`) realizuje formularz „Dodaj pomysł”; dane trafiają do katalogu `data/`.
- `config.json` (w katalogu głównym i `public/`) wskazuje adres tunelu backendu, wykorzystywany przez JS frontu.
- Workflow `.github/workflows/ci.yml` uruchamia `pytest`, `ruff`, `mypy` jako bloker PR.

Zasady:
- Brak odwołań do historii czatu.
- Aktualizacje repo muszą odzwierciedlać stan planu i zadań.
- Paleta i ambient opisane w `AGENTS.md` są kanoniczne; `tests/test_responsive_theme.py` oraz `tests/test_ambient_backgrounds.py` pilnują responsywności i widoczności (opacity ≥ 0.45, `z-index` ≥ -1).
- Wielowarstwowe tła korzystają z katalogu `img/`; ich mapowanie chroni `tests/test_ambient_backgrounds.py`.
- Baner Notebook LM jest obowiązkowy na każdej stronie; jego obecność i CTA do Google Drive weryfikuje `tests/test_notebook_banner.py`.
- Panel "Oceń pomysł" na `organizacja.html` musi obsługiwać `localStorage` (test `tests/test_feedback_panel.py`).
- Formularz „Dodaj pomysł” wymaga działającego endpointu `/api/ideas`; kontrakt pilnuje `tests/test_idea_submission.py` oraz `tests/test_api.py`.
- Endpoint `/api/ideas` jest chroniony nagłówkiem `X-API-Key` (domyślnie `dev-key`) i przekazuje zgłoszenia do n8n (domyślnie `http://localhost:5678/webhook-test/f11f16e1-4e7e-4fa6-b99e-bf1e47f02a50`, z aliasem payloadu `pomysł`).
- Smoke `tests/test_api.py` oraz `scripts/smoke.sh` gwarantują, że `POST /api/ideas` zwraca `{ "status": "ok" }`, a `/api/health` raportuje gotowość storage.
- Dokumentacja pozostaje zwięzła i bez duplikatów nagłówków; `tests/test_documentation.py` pilnuje spójności README.
- Kafelki tekstowe na wszystkich stronach udostępniają edycję treści przez zakładkę sterowaną `assets/editable-tiles.js`; działanie wymaga `localStorage`, a fallback informuje o blokadzie zapisu.
