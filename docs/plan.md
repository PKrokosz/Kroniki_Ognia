# Plan (v1)

## Cel fazy 1 — Standaryzacja strony i pipeline'u
- [Scope] Ujednolicona nawigacja i styl wszystkich stron HTML, przygotowanie index.html dla GitHub Pages.
- [Scope] Ustanowienie dokumentacji procesowej (AGENTS, CONTEXT, plan, zadania, notatki) i workflow CI.
- [Non-Goals] Nowa zawartość fabularna, rozbudowane funkcje JS poza nawigacją.

## Definicja ukończenia (DoD)
- Lint, typecheck, test: `ruff check .`, `mypy app.py`, `pytest` zielone; kolejne linty front-endowe zaplanujemy w następnych fazach.
- Wszystkie strony korzystają ze wspólnego arkusza `assets/styles.css` i dzielonej nawigacji.
- Istnieje `index.html` jako strona startowa GitHub Pages.
- Dokumentacja (README, notes, tasks) odzwierciedla aktualny stan.
- Akceptacyjne: test `tests/test_navigation.py::test_nav_links_consistent` przechodzi.

## Ryzyka
- Brak automatycznego lintowania HTML — do rozważenia w kolejnej fazie.
- Możliwe rozbieżności między istniejącym tekstem a nowym layoutem (ryzyko złamania zasady zachowania treści).

## Cel fazy 2 — Mobilna mroczna atmosfera
- [Scope] Przygotowanie mobilnego skalowania nagłówka i kart, aby UX działał na ekranach < 600px.
- [Scope] Ujednolicenie palety kolorów na bardziej stonowaną, ponurą z zachowaniem czytelności tekstów.
- [Scope] Dodanie lekkich efektów ambientowych (warstwa tła, pulsujące żarzenie) bez zmiany narracji.
- [Scope] Warstwowe tła z galerii `img/` — trzy rozmyte, delikatnie przesuwające się obrazy na każdej podstronie.
- [Scope] Sekcja visual key na landingu wykorzystująca fotografie z `img/` i prowadząca do kluczowych podstron.
- [Non-Goals] Dynamiczne menu hamburger, pełne przebudowanie treści sekcji, nowe strony.

## Definicja ukończenia fazy 2 (DoD)
- `pytest` przechodzi z nowym testem responsywności.
- Na urządzeniach mobilnych nawigacja układa się w kolumnę, a karty mają zmniejszone paddingi.
- Paleta kolorów została zdesaturowana i udokumentowana w README.
- Ambientowe warstwy tła pozostają widoczne ponad innymi efektami (warstwy mają opacity ≥ 0.45, animacja dryfu zauważalna przy horyzontalnym ruchu).
- Akceptacyjne: `tests/test_responsive_theme.py::test_mobile_media_queries_present`, `tests/test_responsive_theme.py::test_ambient_effects_defined` oraz `tests/test_ambient_backgrounds.py` są zielone.
- Akceptacyjne: `tests/test_visual_key.py::test_visual_key_section_present` potwierdza sekcję ekspozycji.

## Cel fazy 3 — Custom domain i hosting Pages
- [Scope] Zapewnienie automatycznego testu kontrolującego brak pliku `CNAME` w repozytorium oraz kompletność dokumentacji ręcznej konfiguracji domeny.
- [Scope] Udokumentowanie kroków DNS oraz procedury weryfikacji i audytu w README/dokumentacji, z jednoznacznym wskazaniem hosta `pkr0kosz.github.io`.
- [Scope] Udokumentowanie kroków DNS oraz procedury weryfikacji i audytu w README/dokumentacji.
- [Scope] Przygotowanie checklisty do monitorowania dostępności i certyfikatu HTTPS (kontynuacja w kolejnych zadaniach).
- [Non-Goals] Automatyczne narzędzia monitoringu uptime, wdrożenia CD poza GitHub Pages, zakup certyfikatów zewnętrznych.

## Definicja ukończenia fazy 3 (DoD)
- `pytest` obejmuje test `tests/test_custom_domain.py` potwierdzający brak śledzonego pliku `CNAME` i obecność dokumentacji.
- README opisuje kroki konfiguracji DNS, jednoznacznie wskazuje host `pkr0kosz.github.io`, a `docs/notes.md` zawiera log 5xWhy dla decyzji o przeniesieniu `CNAME` do ustawień Pages.
- `docs/tasks.md` zawiera checklistę z ukończonym zadaniem dokumentacji custom domain i planem dalszych kroków dla monitoringu.
- Akceptacyjne: ręczna weryfikacja `dig`/`curl` odnotowana w README.
- README opisuje kroki konfiguracji DNS, a `docs/notes.md` zawiera log 5xWhy dla decyzji o przeniesieniu `CNAME` do ustawień Pages.
- `docs/tasks.md` zawiera checklistę z ukończonym zadaniem dokumentacji custom domain i planem dalszych kroków dla monitoringu.
- Akceptacyjne: ręczna weryfikacja `dig`/`curl` odnotowana w README.
## Cel fazy 3 — Integracja bazy brainstormu
- [Scope] Udostępnić szybkie przejście do Notebook LM jako źródła prawdy dla wiedzy z burzy mózgów.
- [Scope] Zachować narracyjny klimat poprzez motyw "flying object" i animowanego zwiadowcę.
- [Scope] Zapewnić dostępność CTA (prefers-reduced-motion, mobilny układ) oraz automatyczną weryfikację testami.
- [Scope] Rozszerzyć baner o dodatkowe CTA do archiwum Google Drive, zachowując wspólną stylistykę i bezpieczeństwo linków.
- [Non-Goals] Embedowanie pełnego Notebook LM, synchronizacja treści w czasie rzeczywistym.

## Definicja ukończenia fazy 3 (DoD)
- `pytest` obejmuje test `tests/test_notebook_banner.py::test_notebook_banner_present_with_link` i przechodzi zielono.
- `pytest` obejmuje test `tests/test_notebook_banner.py::test_notebook_banner_includes_drive_archive_link` potwierdzający CTA do Google Drive.
- Baner Notebook LM jest widoczny i funkcjonalny na każdej podstronie repo.
- Dokumentacja (README, notes) opisuje nowe CTA i wskazuje sposób ręcznej weryfikacji.
- Akceptacyjne: kliknięcie banera otwiera wskazany notebook, a motyw "flying object" jest zachowany w tekście.

## Cel fazy 4 — Pętle feedbacku uczestników
- [Scope] Umożliwić komentowanie każdego wątku na stronie "Organizacja" poprzez lekki panel z przyciskiem "Oceń pomysł".
- [Scope] Zabezpieczyć doświadczenie mobilne i estetykę panelu w ramach istniejącej palety.
- [Scope] Wprowadzić testy regresyjne chroniące strukturę danych, styl i integrację z `localStorage`.
- [Non-Goals] Współdzielenie komentarzy między urządzeniami, moderacja online, backend.

## Definicja ukończenia fazy 4 (DoD)
- `pytest tests/test_feedback_panel.py` przechodzi i potwierdza obecność komponentu.
- Panel komentarzy domyślnie jest zwinięty, obsługuje `localStorage` i komunikaty statusu.
- README oraz notatki dokumentują sposób użycia panelu i testy.
- Akceptacyjne: ręczne otwarcie panelu pozwala zapisać komentarz, który utrzymuje się po odświeżeniu przeglądarki.
## Cel fazy 4 — Rejestr pomysłów uczestników
- [Scope] Udostępnić na stronie głównej formularz "Dodaj pomysł" z walidacją i informacją zwrotną.
- [Scope] Zapisać zgłoszenia w trwałej bazie danych oraz równoległym pliku tekstowym do audytu narracyjnego.
- [Scope] Zapewnić backend Flask (`app.py`) wraz z testem kontraktowym i dokumentacją procesu w README oraz docs/.
- [Non-Goals] Publiczne wyświetlanie listy pomysłów, moderacja treści, uwierzytelnianie użytkowników.

## Definicja ukończenia fazy 4 (DoD)
- `pytest` obejmuje test API rejestrujący pomysł i przechodzi zielono.
- Formularz na stronie głównej przekazuje komunikat powodzenia/błędu z użyciem `aria-live` i korzysta z fetch.
- README, notes oraz ADR dokumentują architekturę formularza i kroki uruchomienia backendu.
- Akceptacyjne: ręczne złożenie pomysłu zapisuje rekord w SQLite oraz dopisuje linię w `data/ideas.txt`.

## Cel fazy 5 — Tunelowany backend Pages ↔ Flask
- [Scope] Konfiguracja frontu do wczytywania `BACKEND_URL` z `public/config.json` i ustawiania `form.action` po stronie klienta.
- [Scope] Zapewnienie nagłówków CORS tylko dla hostów GitHub Pages i tunelu `https://api-kroniki.<MOJA-DOMENA>`.
- [Scope] Dodanie smoke testów i skryptu CLI do walidacji tunelu (pytest + `scripts/smoke.sh`).
- [Scope] Ustanowienie limitu `10/min` na `POST /api/ideas` (Flask-Limiter) z dokumentacją w README.
- [Non-Goals] Pełna autoryzacja żądań, zarządzanie tajnymi tokenami, publikacja listy pomysłów w UI.

## Definicja ukończenia fazy 5 (DoD)
- `pytest` obejmuje smoke `tests/test_api.py` oraz zaktualizowane testy kontraktowe.
- `config.json` jest serwowany zarówno z katalogu głównego, jak i z `public/`, zawiera produkcyjny adres tunelu bez końcowego ukośnika i jest udokumentowany w README.
- Skrypt `scripts/smoke.sh` przyjmuje URL tunelu i zwraca odpowiedź JSON; README opisuje jego użycie.
- CORS i rate limit są skonfigurowane w `app.py`, a ADR/notes zawierają analizę 5xWhy dla tunelu.
