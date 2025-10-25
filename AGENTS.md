# AGENTS

Repo owner directives:
- CTO persona governs process. Maintain pipeline across roles (Architect → Implementer → Tester → Dokumentalista).
- Preserve narrative content: do not rewrite in-universe texts beyond structural/stylistic adjustments. Formatting and wrapping is allowed, but keep wording intact unless fixing typos.
- Every touched area must include acceptance criteria in docs/tasks.md and be reflected in plan/notes/README updates.
- For UI work create/maintain shared assets (e.g., `assets/`) instead of page-specific inline duplication.
- Keep navigation consistent across all HTML pages (include top nav linking to each document and GitHub Pages index).
- Tests, lint, and documentation updates are mandatory companions to feature work.
- Expand this AGENTS file when new patterns or decisions emerge.

Documentation scope:
- `docs/` contains phase plans, notes, ADRs; keep them synchronized with repository state.
- `CONTEXT.md` lists truth sources and active decisions.
- `.codex/prompts/*.md` store role prompts; follow naming `NN_name.md`.

Coding standards:
- Prefer semantic HTML5 elements, accessible markup, and responsive design.
- Place shared styling in `assets/styles.css`; load via relative paths.
- No binary assets; use text/SVG only.
- Tests live under `tests/` and must be runnable with `pytest`.

Commit/PR standards:
- Use Conventional Commits.
- Run required commands (lint/typecheck/test) before commit; record outcomes in README and final report.
