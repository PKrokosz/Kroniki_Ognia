# Kontekst

Źródła prawdy:
- `docs/plan.md`
- `docs/tasks.md`
- `AGENTS.md`
- `docs/notes.md`
- Bieżące ADR w `docs/adr/`
- Backend Flask (`app.py`) realizuje formularz „Dodaj pomysł”; dane trafiają do katalogu `data/`.
- `public/config.json` wskazuje adres tunelu backendu, wykorzystywany przez JS frontu.

Zasady:
- Brak odwołań do historii czatu.
- Aktualizacje repo muszą odzwierciedlać stan planu i zadań.
- Paleta i ambient opisane w AGENTS.md są kanoniczne; `tests/test_responsive_theme.py` chroni responsywność i warstwę wizualną.
- Wielowarstwowe tła korzystają ze zdjęć w `img/` i są mapowane w `assets/styles.css`; regresje wychwyci `tests/test_ambient_backgrounds.py`.
- Baner Notebook LM jest elementem obowiązkowym na każdej stronie; jego obecność sprawdza `tests/test_notebook_banner.py`.
- Panel "Oceń pomysł" na stronie `organizacja.html` musi zachować obsługę `localStorage` i markup kontrolowany przez `tests/test_feedback_panel.py`.
- Formularz „Dodaj pomysł” wymaga działającego endpointu `/api/ideas`; kontrakt chroni `tests/test_idea_submission.py`.
- Smoke `tests/test_api.py` gwarantuje, że `POST /api/ideas` zwraca `{ "status": "ok" }`, a `scripts/smoke.sh` pozwala sprawdzić tunel ręcznie.
