## Faza 1 — Standaryzacja
- [x] Zadanie 1: Utworzyć wspólną nawigację i arkusz stylów dla wszystkich stron HTML — Test: `pytest tests/test_navigation.py::test_nav_links_consistent`
- [x] Zadanie 2: Przygotować `index.html` z przeglądem i linkami — Test: ręczna weryfikacja ładowania (opis w README)
- [x] Zadanie 3: Skonfigurować pipeline dokumentacyjny i CI (`docs/*`, `.codex`, workflow) — Test: sprawdzenie obecności plików + `pytest`

## Faza 2 — Mobilna mroczna atmosfera
- [x] Zadanie 1: Przeskalować nagłówek i karty pod ekrany < 600px — Test: `pytest tests/test_responsive_theme.py::test_mobile_media_queries_present`
- [x] Zadanie 2: Przyciemnić paletę i dodać ambientowe efekty — Test: `pytest tests/test_responsive_theme.py::test_ambient_effects_defined`

## Faza 3 — Custom domain i hosting Pages
- [x] Zadanie 1: Ustabilizować plik `CNAME` i dodać test regresji — Test: `pytest tests/test_custom_domain.py::test_cname_points_to_custom_domain`
- [ ] Zadanie 2: Przygotować automatyczną weryfikację certyfikatu HTTPS — Test: `pytest tests/test_https_monitoring.py::test_certificate_expiry` (do implementacji)
