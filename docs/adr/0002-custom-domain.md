# 0002 — Custom domain dla GitHub Pages

## Status
Zaakceptowane — Faza 3

## Kontekst
Projekt "Kroniki Ognia" jest publikowany jako statyczna witryna na GitHub Pages. Zespół chce używać domeny `www.larpkronikiognia.pl`, aby komunikacja marketingowa była spójna z identyfikacją LARP-u. Dotychczas brakowało formalnego zapisu decyzji oraz automatycznego zabezpieczenia przed zmianą konfiguracji.

## Decyzja
- Konfigurujemy custom domain `www.larpkronikiognia.pl` wyłącznie poprzez ustawienia GitHub Pages; plik `CNAME` nie jest śledzony w repozytorium.
- Dodajemy test `tests/test_custom_domain.py`, który pilnuje braku pliku `CNAME` oraz obecności dokumentacji opisującej ręczną konfigurację domeny.
- README dokumentuje wymagane rekordy DNS (`CNAME` dla `www`, rekordy `A` dla domeny głównej) oraz kroki weryfikacji (`dig`, `curl`) wraz z przypomnieniem o potwierdzeniu wpisu w ustawieniach Pages.

## Konsekwencje
- Propagacja DNS może wymagać do 24 godzin; zmiany w repozytorium należy planować z uwzględnieniem tego czasu.
- Test jednostkowy chroni przed przypadkowym przywróceniem pliku `CNAME` oraz dba o aktualność dokumentacji; nadal potrzebujemy automatycznego monitoringu certyfikatu HTTPS.
- Dokumentacja w README ułatwia onboarding nowych osób i upraszcza audyt CTO persony.
