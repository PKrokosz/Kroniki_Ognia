# ADR 0003 — Formularz "Dodaj pomysł" z backendem Flask

## Status
Zaakceptowano — Faza 4

## Kontekst
Strona projektu była dotąd statyczna. Użytkownicy nie mogli zgłaszać własnych pomysłów ani budować backlogu inspiracji. Zlecenie
wymagało stałego zapisu przesłanych treści zarówno w bazie danych, jak i w pliku tekstowym dla zespołu narracyjnego. Konieczna
była technologia, która zagra z istniejącym stosem Pythona, testami `pytest` oraz ograniczeniami repozytorium (brak binarnych
plików w kontroli wersji).

## Decyzja
- Implementujemy lekki backend HTTP w Flask (`app.py`) z endpointem `POST /api/ideas` przyjmującym treść pomysłu w JSON lub
  formularzu `application/x-www-form-urlencoded`.
- Utrzymujemy dane w lokalnej bazie SQLite (`data/ideas.sqlite3`) oraz równoległym dzienniku tekstowym (`data/ideas.txt`).
- Formularz na stronie głównej komunikuje status przez `aria-live` i korzysta z fetch, aby złożyć request do tego endpointu.
- W testach używamy `create_app` z możliwością wskazania katalogu tymczasowego, co pozwala na izolację danych i brak kolizji z
  produkcyjnym storage.

## Konsekwencje
- Repozytorium pozostaje lekkie — katalog `data/` posiada `.gitignore`, a pliki SQLite powstają tylko w środowisku uruchomieniowym.
- Do listy zależności trafia Flask; README dokumentuje nowy sposób uruchomienia backendu wraz z formularzem.
- Dalsze prace (planowane `tests/test_idea_listing.py`) mogą rozszerzyć API o pobieranie zgłoszeń bez łamania obecnej architektury.
- Wymagana jest obserwacja bezpieczeństwa treści (np. filtrowanie XSS) przy kolejnych iteracjach, jeśli pomysły będą wyświetlane
  publicznie.
