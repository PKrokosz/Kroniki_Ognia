# ADR 0004 — Warstwowe, animowane tła z galerii `img/`

## Status
Zaakceptowano — Faza 2

## Kontekst
Witryna posiadała jedynie statyczne gradienty, które nie wykorzystywały istniejącej biblioteki zdjęć w katalogu `img/`. Zlecenie wymagało zblurowanych, płynnych teł, które delikatnie przesuwają się horyzontalnie podczas przeglądania stron. Jednocześnie musieliśmy zachować lekki hosting GitHub Pages (brak JS przy pierwszej iteracji), dostępność (`prefers-reduced-motion`) i spójność z testami wizualnymi.

## Decyzja
- Każda strona otrzymuje kontener `.ambient-background` z trzema warstwami `.ambient-layer--1..3`, renderowanym tuż po otwarciu `<body>`.
- `assets/styles.css` definiuje rozmycie, mieszanie kolorów (`mix-blend-mode: screen`) oraz animację `ambientDrift`, która przesuwa obrazy w poziomie z różnymi prędkościami.
- Mapowanie stron na pliki graficzne jest jawne w CSS i walidowane testem `tests/test_ambient_backgrounds.py`.
- Blok `@media (prefers-reduced-motion: reduce)` wyłącza animację zarówno dla gradientów, jak i nowych warstw.

## Konsekwencje
- Warstwa wizualna wykorzystuje zasoby `img/` bez powielania plików i zachowuje klimat płomiennego klasztoru.
- Testy `pytest` pilnują, że każda podstrona ma komplet trzech obrazów i że animacje respektują preferencje ruchu.
- W dokumentacji `docs/tasks.md` pojawia się kontynuacyjne zadanie rozszerzenia efektu o progresywne sterowanie prędkością (np. via IntersectionObserver) w przyszłej iteracji.
- Wymóg widoczności (opacity ≥ 0.45, `z-index` nad pseudo-elementami) jest na stałe wpisany w `AGENTS.md` i README jako kryterium akceptacji wizualnej.
- Dodanie nowych stron wymaga dopisania klas `page-*` i aktualizacji mapy obrazów, co zostało udokumentowane w `AGENTS.md`.
