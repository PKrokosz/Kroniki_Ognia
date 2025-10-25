# AGENTS

Repo owner directives:
- CTO persona governs process. Maintain pipeline across roles (Architect → Implementer → Tester → Dokumentalista).
- Preserve narrative content: do not rewrite in-universe texts beyond structural/stylistic adjustments. Formatting and wrapping is allowed, but keep wording intact unless fixing typos.
- Every touched area must include acceptance criteria in docs/tasks.md and be reflected in plan/notes/README updates.
- For UI work create/maintain shared assets (e.g., `assets/`) instead of page-specific inline duplication.
- Keep navigation consistent across all HTML pages (include top nav linking to each document and GitHub Pages index).
- Utrzymuj na każdej stronie baner "flying object" kierujący do Notebook LM, włączając animowaną ikonę oraz tekst o zwiadowcy.
- Tests, lint, and documentation updates are mandatory companions to feature work.
- Expand this AGENTS file when new patterns or decisions emerge.
- Custom domain `www.larpkronikiognia.pl` konfigurujemy w ustawieniach GitHub Pages; repozytorium nie przechowuje pliku `CNAME`.
- Testy dotyczące domeny muszą sprawdzać, że dokumentacja opisuje ręczne ustawienie `CNAME`, brak pliku w repo i wskazuje host `pkr0kosz.github.io` (plus ewentualną domenę `.com`).
- Testy dotyczące domeny muszą sprawdzać, że dokumentacja opisuje ręczne ustawienie `CNAME` i brak pliku w repo.
- Formularze interaktywne muszą komunikować status użytkownikowi (`aria-live`) i korzystać z fetch do backendu działającego na
  tym samym hostie. Endpoints HTTP obsługuje `app.py`; dbamy o JSON-owe odpowiedzi i kody statusów (201 dla sukcesu,
  400 dla walidacji).
- Storage dla nowych funkcji trafia do katalogu `data/` (tworzonego dynamicznie). Repozytorium śledzi jedynie pliki konfiguracyjne
  i `.gitignore`, bez binarnych artefaktów baz danych.

Documentation scope:
- `docs/` contains phase plans, notes, ADRs; keep them synchronized with repository state.
- `CONTEXT.md` lists truth sources and active decisions.
- `.codex/prompts/*.md` store role prompts; follow naming `NN_name.md`.

Coding standards:
- Prefer semantic HTML5 elements, accessible markup, and responsive design.
- Place shared styling in `assets/styles.css`; load via relative paths.
- No binary assets; use text/SVG only.
- Tests live under `tests/` and must be runnable with `pytest`.
- Maintain a subdued, ember-toned palette (earthy browns, muted golds) and reuse the ambient overlay/hero patterns when rozbudowywanie UI.
- Zachowuj responsywne bloki @media <= 600px tak, by nawigacja przechodziła w układ kolumnowy; nowe komponenty muszą respektować mobilny padding.
- Panel komentarzy "Oceń pomysł" w `organizacja.html` musi pozostać domyślnie zwinięty, obsługiwać `localStorage` z czytelnym komunikatem statusu oraz być testowany w `tests/test_feedback_panel.py`.
- Interaktywne komponenty front-endowe wymagają obsługi braku `localStorage` (fallback komunikatu) i aktualizacji dokumentacji w README oraz `docs/notes.md`.

Commit/PR standards:
- Use Conventional Commits.
- Run required commands (lint/typecheck/test) before commit; record outcomes in README and final report.
