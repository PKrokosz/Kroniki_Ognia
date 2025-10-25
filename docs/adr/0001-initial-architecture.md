# ADR 0001 — Ujednolicenie statycznej witryny

## Status
Zaakceptowane

## Kontekst
Repozytorium zawierało niezależne pliki HTML stylowane ad-hoc z osadzonym Tailwind CDN. Brakowało wspólnego układu, nawigacji oraz pliku startowego dla GitHub Pages. Nie istniały procesy dokumentacyjne ani testowe.

## Decyzja
- Tworzymy wspólny arkusz stylów `assets/styles.css` obejmujący paletę kolorów, typografię i komponenty (nawigacja, sekcje, karty).
- Każda strona HTML wykorzystuje współdzielony nagłówek nawigacyjny i footer, zachowując dotychczasową treść.
- Dodajemy `index.html` jako stronę główną kierującą do pozostałych dokumentów.
- Konfigurujemy dokumentację procesu (`docs/`, `.codex/`), testy (`pytest`) i CI (GitHub Actions) dla przyszłych faz.

## Konsekwencje
- Ułatwiona dalsza rozbudowa witryny przy zachowaniu spójnego wyglądu.
- Konieczność utrzymywania arkusza stylów i nawigacji przy każdej nowej stronie.
- Możliwość dalszej automatyzacji (lintowanie HTML) w kolejnych fazach.
