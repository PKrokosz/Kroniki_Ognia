# AGENTS

Repo owner directives:
- CTO persona governs process. Maintain pipeline across roles (Architect → Implementer → Tester → Dokumentalista).
- Preserve narrative content: do not rewrite in-universe texts beyond structural/stylistic adjustments. Formatting and wrapping is allowed, but keep wording intact unless fixing typos.
- Every touched area must include acceptance criteria in docs/tasks.md and be reflected in plan/notes/README updates.
- For UI work create/maintain shared assets (e.g., `assets/`) instead of page-specific inline duplication.
- Keep navigation consistent across all HTML pages (include top nav linking to each document and GitHub Pages index).
- Utrzymuj na każdej stronie baner "flying object" kierujący do Notebook LM, włączając animowaną ikonę oraz tekst o zwiadowcy; baner musi także zawierać CTA do archiwum Google Drive z ikoną (`data-icon="google-drive"`) i klasą `notebook-banner__link--drive`.
- Tests, lint, and documentation updates are mandatory companions to feature work.
- CI `ci` workflow instaluje i uruchamia `pytest`, `ruff` oraz `mypy`; każda zmiana w Pythonie musi przechodzić ten zestaw lokalnie przed PR.
- Expand this AGENTS file when new patterns or decisions emerge.
- Custom domain `www.larpkronikiognia.pl` konfigurujemy w ustawieniach GitHub Pages; repozytorium nie przechowuje pliku `CNAME`.
- Testy dotyczące domeny muszą sprawdzać, że dokumentacja opisuje ręczne ustawienie `CNAME`, brak pliku w repo i wskazuje host `pkr0kosz.github.io` (plus ewentualną domenę `.com`).
- Testy dotyczące domeny muszą sprawdzać, że dokumentacja opisuje ręczne ustawienie `CNAME` i brak pliku w repo.
- Formularze interaktywne muszą komunikować status użytkownikowi (`aria-live`) i korzystać z fetch do backendu działającego na
  tym samym hostie. Endpoints HTTP obsługuje `app.py`; dbamy o JSON-owe odpowiedzi i kody statusów (201 dla sukcesu,
  400 dla walidacji).
- Formularze integrujące backend muszą ładować moduł `assets/js/backend-config.js`, oznaczać endpoint `data-api` i polegać na
  `wireBackendForms` do ustawienia `form.action`.
- Backend `app.py` utrzymuje endpoint `GET /api/health` (JSON `{ "status": "ok" }`) oraz restrykcyjną walidację `POST /api/ideas`
  (`Content-Type: application/json`, limit 5 KB, poprawne JSON-y). Aktualizacje muszą zachować te kontrakty i testy.
- Storage dla nowych funkcji trafia do katalogu `data/` (tworzonego dynamicznie). Repozytorium śledzi jedynie pliki konfiguracyjne
  i `.gitignore`, bez binarnych artefaktów baz danych.
- `public/config.json` przechowuje `BACKEND_URL` tunelu backendu; brak tego pliku lub klucza traktujemy jako błąd krytyczny.
- Katalog główny repozytorium musi zawierać bliźniaczy `config.json`; oba pliki pozostają w 100% zsynchronizowane i są chronione testami.
- Katalog główny repozytorium musi zawierać pusty plik `.nojekyll`, a README dokumentuje, że dzięki niemu GitHub Pages nie uruchamia Jekylla; testy powinny to kontrolować.
- `scripts/smoke.sh` jest kanonicznym narzędziem do sprawdzania tunelu `https://api-kroniki.<MOJA-DOMENA>` i musi odzwierciedlać aktualny kontrakt API.
- `/api/health` raportuje gotowość storage w JSON (baza + dziennik) i jest chroniony testem `tests/test_api.py::test_health_ok`; przy rozbudowie rozszerz payload, zachowując istniejące pola.

Documentation scope:
- `docs/` contains phase plans, notes, ADRs; keep them synchronized with repository state.
- `CONTEXT.md` lists truth sources and active decisions.
- `.codex/prompts/*.md` store role prompts; follow naming `NN_name.md`.
- README i kluczowe dokumenty (`docs/plan.md`, `docs/tasks.md`, `docs/notes.md`, `CONTEXT.md`) muszą mieć unikalne nagłówki — kontroluje to `tests/test_documentation.py`.

Coding standards:
- Prefer semantic HTML5 elements, accessible markup, and responsive design.
- Place shared styling in `assets/styles.css`; load via relative paths.
- No binary assets; use text/SVG only.
- Tests live under `tests/` and must be runnable with `pytest`.
- Backend zmiany muszą utrzymać zielone `ruff check .` oraz `mypy app.py` przed commitem.
- Maintain a subdued, ember-toned palette (earthy browns, muted golds) and reuse the ambient overlay/hero patterns when rozbudowywanie UI.
- Zachowuj responsywne bloki @media <= 600px tak, by nawigacja przechodziła w układ kolumnowy; nowe komponenty muszą respektować mobilny padding.
- Ambient backgrounds korzystają z kontenera `.ambient-background` z trzema warstwami `.ambient-layer--1..3` na każdej stronie. Każda strona wykorzystuje obrazy z `img/` (około trzy na widok); aktualizacje wymagają synchronizacji z testem `tests/test_ambient_backgrounds.py` i mapą w `assets/styles.css`. Zachowaj widoczne nasycenie (opacity warstw ≥ 0.45) i upewnij się, że znajdują się nad innymi efektami (`z-index` ≥ -1).
- Panel komentarzy "Oceń pomysł" w `organizacja.html` musi pozostać domyślnie zwinięty, obsługiwać `localStorage` z czytelnym komunikatem statusu oraz być testowany w `tests/test_feedback_panel.py`.
- Interaktywne komponenty front-endowe wymagają obsługi braku `localStorage` (fallback komunikatu) i aktualizacji dokumentacji w README oraz `docs/notes.md`.
- Ambient backgrounds korzystają z kontenera `.ambient-background` z trzema warstwami `.ambient-layer--1..3` na każdej stronie. Każda strona wykorzystuje obrazy z `img/` (około trzy na widok); aktualizacje wymagają synchronizacji z testem `tests/test_ambient_backgrounds.py` i mapą w `assets/styles.css`.
- Sekcja visual key „Próby Płomienia” na `index.html` utrzymuje trzy kafelki (`visual-key__tile--ember`, `--glow`, `--flame`) z obrazami `img/1.jpg`, `img/4.jpg`, `img/7.jpg`, CTA do `cechy.html`, `imersja_mechanika.html`, `draft_planu.html` oraz przycisk `data-visual-key-autoplay` respektujący `prefers-reduced-motion`. Zmiany wymagają aktualizacji `assets/visual-key.js`, styli i testu `tests/test_visual_key.py`.

Commit/PR standards:
- Use Conventional Commits.
- Run required commands (lint/typecheck/test) before commit; record outcomes in README and final report.
