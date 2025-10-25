# 0002 — Custom domain dla GitHub Pages

## Status
Zaakceptowane — Faza 3

## Kontekst
Projekt "Kroniki Ognia" jest publikowany jako statyczna witryna na GitHub Pages. Zespół chce używać domeny `www.larpkronikiognia.pl`, aby komunikacja marketingowa była spójna z identyfikacją LARP-u. Dotychczas brakowało formalnego zapisu decyzji oraz automatycznego zabezpieczenia przed zmianą konfiguracji.

## Decyzja
- Utrzymujemy plik `CNAME` w repozytorium z wpisem `www.larpkronikiognia.pl` zakończonym znakiem nowej linii.
- Dodajemy test `tests/test_custom_domain.py`, który blokuje merge, jeśli wpis w `CNAME` jest niepoprawny lub brak w nim nowej linii.
- README dokumentuje wymagane rekordy DNS (`CNAME` dla `www`, rekordy `A` dla domeny głównej) oraz kroki weryfikacji (`dig`, `curl`).

## Konsekwencje
- Propagacja DNS może wymagać do 24 godzin; zmiany w repozytorium należy planować z uwzględnieniem tego czasu.
- Test jednostkowy chroni przed przypadkowym usunięciem pliku `CNAME`, ale nie zastąpi monitoringu certyfikatu — kolejne zadanie przewiduje implementację automatycznych kontroli HTTPS.
- Dokumentacja w README ułatwia onboarding nowych osób i upraszcza audyt CTO persony.
