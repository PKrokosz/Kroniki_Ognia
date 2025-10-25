# ADR 0005 — Tunelowany backend dla formularza "Dodaj pomysł"

## Status
Zaakceptowane — Faza 5

## Kontekst
- Statyczny front hostowany na GitHub Pages potrzebuje komunikacji z backendem Flask uruchamianym lokalnie i wystawianym przez tunel `https://api-kroniki.<MOJA-DOMENA>`.
- Dotychczasowy kod zakładał backend pod `/api/ideas` w tym samym originie i nie obsługiwał CORS ani zewnętrznej konfiguracji.
- Formularz gromadził tylko pole `idea`, przez co backend nie rozróżniał tytułu, treści i tagów, utrudniając dalsze planowanie katalogowania pomysłów.

## Decyzja
- Front ładuje konfigurację z `public/config.json`, korzysta z `getBackendUrl()` i ustawia `form.action` na `${BACKEND_URL}/api/ideas`.
- Backend Flask przyjmuje schemat JSON `{"title": str, "content": str, "tags": [str]?}`, zapisuje dane w SQLite (zachowując kolumnę `idea` dla kompatybilności) i zwraca `201` z `{ "id": "...", "status": "ok" }`.
- CORS ograniczony jest do `https://<twoje-pages>.github.io`, `https://<custom-domain-pages>` oraz `https://api-kroniki.<MOJA-DOMENA>`.
- Włączono `Flask-Limiter` z limitem `10/min` na `POST /api/ideas` oraz dodano smoke testy: `tests/test_api.py` i `scripts/smoke.sh`.

## Konsekwencje
- `public/config.json` staje się wymaganym artefaktem konfiguracyjnym i musi być aktualizowany przy każdej zmianie tunelu.
- Formularz zyskał dodatkowe pola, co wymagało aktualizacji styli i testów `tests/test_idea_submission.py`.
- CI (`.github/workflows/ci.yml`) uruchamia pytest z nowymi zależnościami (`Flask-Cors`, `Flask-Limiter`).
- Kolejny krok: zautomatyzować smoke tunelu w GitHub Actions (zadanie otwarte w `docs/tasks.md`).
