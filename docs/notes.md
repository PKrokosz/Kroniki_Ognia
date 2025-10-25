# Notatki (Faza 1)
- Repo zawiera strony HTML z bogatą treścią narracyjną; wszystkie korzystają ze wspólnej nawigacji i arkusza `assets/styles.css`.
- `index.html` pełni rolę landingu dla GitHub Pages.
- Pipeline CI rozszerzono o `ruff` i `mypy`, a dokumentacja (`AGENTS.md`, `CONTEXT.md`, `docs/plan.md`, `docs/tasks.md`) stanowi źródło prawdy.
- `.gitignore` obejmuje cache testów, środowiska i logi, aby repo pozostawało wolne od artefaktów lokalnych.

## 5xWhy — Higiena `.gitignore`
1. Dlaczego potrzebujemy rozszerzyć `.gitignore`?
   - (A) Aby uniknąć przypadkowego commitowania wirtualnych środowisk.
   - (B) Aby zmniejszyć szum przy code review i CI.
   - (C) Aby uspójnić repo z wytycznymi CTO persony.
   **Decyzja:** A jako fundament operacyjny, wzmocniony dyscypliną review z (B).
2. Dlaczego należy objąć cache testów i typowania?
   - (A) `.pytest_cache` i `.mypy_cache` szybko rosną i są zależne od środowiska.
   - (B) Pozwalają zachować powtarzalność wyników CI.
   - (C) Ułatwiają onboarding nowych agentów poprzez czyste checkouty.
   **Decyzja:** A jako ochrona przed inflacją repo, z dodatkiem onboardingowym z (C).
3. Dlaczego warto ignorować katalogi edytorów (`.idea/`, `.vscode/`)?
   - (A) Każdy agent korzysta z innej konfiguracji IDE.
   - (B) Pliki te często zawierają ścieżki lokalne i sekrety.
   - (C) Zmiany w tych plikach utrudniają code review.
   **Decyzja:** A jako gwarancja neutralności narzędzi, poszerzona o bezpieczeństwo z (B).
4. Dlaczego wpisy dla logów i plików `.env` są krytyczne?
   - (A) Zapobiegają wyciekowi danych konfiguracyjnych lub tokenów.
   - (B) Minimalizują konflikty podczas debugowania.
   - (C) Wspierają pipeline bezpieczeństwa repo.
   **Decyzja:** A jako ochrona tajemnic, wzmocniona bezpieczeństwem z (C).
5. Dlaczego potrzebny jest kolejny krok automatyzujący walidację `.gitignore`?
   - (A) Manualna kontrola może zostać pominięta w przyszłych iteracjach.
   - (B) Automatyzacja pozwoli szybciej wykrywać regresje.
   - (C) Wzmacnia kulturę narzędziową przed MVP.
   **Decyzja:** B jako impuls do CI, uzupełniony o kulturę narzędziową z (C).

# Notatki (Faza 2)
- Paleta barw została przygaszona wokół barw ziemistych; dodano ambientową warstwę tła i animację pulsującą przy zachowaniu czytelności tekstów.
- Nawigacja na urządzeniach mobilnych przechodzi w układ kolumnowy, a karty otrzymują mniejsze paddingi.
- Sekcja visual key „Próby Płomienia” łączy narrację z obrazami `img/1.jpg`, `img/4.jpg`, `img/7.jpg` i oferuje przycisk autoodtwarzania respektujący `prefers-reduced-motion`.
- Ambientowe galerie korzystają z zasobów `img/` i dryfują horyzontalnie, respektując `prefers-reduced-motion`.

## 5xWhy — Widoczność ambientowych warstw (aktualizacja)
1. Dlaczego zwiększamy jasność i saturację warstw?
   - (A) Aby obrazy były zauważalne mimo rozmycia i nakładających się efektów.
   - (B) Aby zachować spójność kolorystyczną z narracją o żarze i płomieniach.
   - (C) Aby umożliwić wyróżnienie sekcji CTA bez dodatkowych elementów.
   **Decyzja:** A jako główna potrzeba, uzupełniona o narrację z (B).
2. Dlaczego wymagamy opacity ≥ 0.45?
   - (A) Niższe wartości powodowały, że zdjęcia znikały pod pseudo-elementami.
   - (B) Ułatwia to testowanie poprzez jasny próg liczbowy.
   - (C) Pozwala łączyć ambient z tekstem bez utraty czytelności.
   **Decyzja:** A jako wymóg jakości, wzmocniony testowalnością z (B).
3. Dlaczego `ambient-background` potrzebuje `z-index` ≥ -1?
   - (A) Musi znajdować się nad `body::before`, aby obrazy były widoczne.
   - (B) Ułatwia przyszłe rozszerzenia o dodatkowe efekty.
   - (C) Zapobiega konfliktom z innymi pseudo-elementami.
   **Decyzja:** A jako warunek widoczności, rozszerzony o elastyczność z (B).
4. Dlaczego filtr `saturate(1.35) brightness(1.12)` jest preferowany?
   - (A) Zwiększa czytelność detali na ciemnym tle.
   - (B) Nadaje ambientowi charakter rozżarzonego płomienia.
   - (C) Minimalizuje konieczność manualnej edycji zdjęć.
   **Decyzja:** A jako wsparcie UX, doprawione estetyką z (B).
5. Dlaczego test automatyczny kontroluje próg widoczności?
   - (A) Zapobiega nieświadomemu obniżeniu opacity podczas kolejnych zmian.
   - (B) Przygotowuje grunt pod przyszłe warianty animacji.
   - (C) Daje szybki feedback w CI.
   **Decyzja:** C jako natychmiastowy feedback, rozszerzony o ochronę jakości z (A).

## 5xWhy — Standaryzacja kart i rozmytych teł (2024-09)
1. Dlaczego karty rozchodziły się przy zmianie szerokości okna?
   - (A) Siatka korzystała ze sztywnej liczby kolumn niezależnie od viewportu.
   - (B) Dodatkowe klasy utilitarne (np. `lg:grid-cols-2`) nie miały wsparcia w arkuszu stylów.
   - (C) Długie słowa w narracji rozszerzały kontenery ponad przewidzianą szerokość.
   **Decyzja:** A jako główny problem konstrukcyjny, uzupełniony o kontrolę zawijania z (C).
2. Dlaczego przechodzimy na `repeat(auto-fit, minmax(...))` sterowany zmienną `--card-min-width`?
   - (A) Auto-fit automatycznie dopasowuje liczbę kolumn do dostępnej przestrzeni bez łamania layoutu.
   - (B) Zmienna pozwala skalować szerokość w zależności od sekcji (2/3/4 kolumny) bez duplikowania reguł.
   - (C) Rozwiązanie jest kompatybilne z istniejącym testem mobile i nie wymaga refaktoringu HTML.
   **Decyzja:** A jako fundament responsywności, rozszerzony o parametryzację z (B).
3. Dlaczego wymuszamy `overflow-wrap:anywhere` i `hyphens:auto` na treściach kart?
   - (A) Polskie słowa i nazwy rytuałów bywają długie i powodowały horyzontalne przewijanie.
   - (B) Hyphenation zachowuje rytm tekstu, co wspiera klimat narracyjny.
   - (C) Ułatwia to zachowanie równych wysokości kafelków przy mieszanych typach treści.
   **Decyzja:** A jako ochrona layoutu, doprawiona klimatem z (B).
4. Dlaczego obrazy visual key stały się rozmytym tłem wypełniającym kafelek?
   - (A) Warstwa tła utrzymuje klimat „żaru” niezależnie od wysokości tekstu.
   - (B) Rozmycie pozwala czytelnie nałożyć figcaption bez dodatkowych blendów.
   - (C) Zmniejsza to zależność od manualnego kadrowania JPG w `img/`.
   **Decyzja:** A jako kluczowe doświadczenie wizualne, wzmocnione czytelnością z (B).
5. Dlaczego dodajemy testy pilnujące auto-fit i rozmytych tł?
   - (A) Bez testów łatwo powrócić do sztywnych kolumn przy kolejnej iteracji.
   - (B) Testy kodują nowe kontrakty CTO persony i blokują regresje responsywności.
   - (C) Automatyczny strażnik skraca feedback podczas review i CI.
   **Decyzja:** B jako forma kontraktu, rozszerzona o szybki feedback z (C).

# Notatki (Faza 3)
- Baner „flying object” prowadzi do Notebook LM i archiwum Google Drive; animacja respektuje `prefers-reduced-motion`.
- Test `tests/test_notebook_banner.py` kontroluje linki, atrybuty bezpieczeństwa i klasę CTA Google Drive.
- Dokumentacja custom domain wskazuje host `pkr0kosz.github.io` (opcjonalnie `.com`), brak pliku `CNAME` oraz kroki `dig`/`curl`.
- Plik `.nojekyll` utrzymuje statyczne serwowanie zasobów na GitHub Pages.

## 5xWhy — Dlaczego nie trzymamy CNAME
1. Dlaczego rezygnujemy z pliku `CNAME` w repo?
   - (A) GitHub Pages zarządza plikiem automatycznie i nadpisze go przy publikacji.
   - (B) Ręczne commitowanie `CNAME` utrudnia zmianę domeny bez historii rewizji.
   - (C) Brak pliku wymusza sprawdzenie ustawień Pages przed wdrożeniem.
   **Decyzja:** A jako kontrakt platformy, uzupełniony kontrolą z (C).
2. Dlaczego to ważne dla pipeline'u?
   - (A) Automatyczne zarządzanie ogranicza konflikty merge.
   - (B) Pozwala utrzymać czyste diffy przy aktualizacji domen.
   - (C) Zapewnia jasny podział odpowiedzialności między repo a konfiguracją Pages.
   **Decyzja:** C jako klarowna odpowiedzialność, wsparte czystym diffem z (B).
3. Dlaczego dokumentujemy decyzję w notesach?
   - (A) Nowi agenci muszą wiedzieć, gdzie modyfikować domenę.
   - (B) Pomaga w audycie CTO persony.
   - (C) Stanowi podstawę do przyszłego monitoringu certyfikatów.
   **Decyzja:** A jako onboarding, doprawione audytem z (B).
4. Dlaczego test automatyczny ma pilnować braku `CNAME`?
   - (A) Chroni przed przypadkowym dodaniem pliku przez edytory statyczne.
   - (B) Umożliwia szybkie wykrycie regresji w PR.
   - (C) Zapobiega konflikcie z ustawieniami Pages.
   **Decyzja:** A jako ochrona przed regresją, rozszerzona o szybki feedback z (B).
5. Dlaczego README musi wspominać o ręcznej konfiguracji?
   - (A) README to podstawowy przewodnik dla właściciela domeny.
   - (B) Ułatwia komunikację z osobami spoza zespołu developerskiego.
   - (C) Zapobiega duplikacji instrukcji w innych dokumentach.
   **Decyzja:** A jako kanał właścicielski, wzmocniony dostępnością z (B).

## 5xWhy — Dlaczego weryfikacja DNS GitHub Pages się nie powiodła
1. Dlaczego poprzednia weryfikacja DNS zakończyła się błędem?
   - (A) Rekord `CNAME` wskazywał na `larpkronikiognia.github.io` zamiast `pkr0kosz.github.io`.
   - (B) Propagacja DNS nie zakończyła się przed ponowną próbą.
   - (C) W panelu Pages pozostawiono stary wpis domeny.
   **Decyzja:** A jako kluczowy błąd adresu, uzupełniony cierpliwością z (B).
2. Dlaczego właściwy host to `pkr0kosz.github.io`?
   - (A) Projekty użytkownika GitHub Pages zawsze wskazują na `<login>.github.io`.
   - (B) Nazwa repozytorium nie determinuje hosta DNS.
   - (C) GitHub dokumentuje tę regułę w ustawieniach Pages.
   **Decyzja:** A jako reguła platformy, wsparte dokumentacją z (C).
3. Dlaczego test sprawdza również domenę `.com`?
   - (A) Domena lustrzana wymaga takiej samej konfiguracji.
   - (B) Przekierowanie 301 zapobiega duplikacji treści.
   - (C) Zapewnia plan awaryjny w razie problemów z `.pl`.
   **Decyzja:** B jako ochrona SEO, z redundancją z (C).
4. Dlaczego notatki dokumentują proces diagnostyczny?
   - (A) Pozwala odtworzyć kroki w przypadku kolejnej awarii.
   - (B) Tworzy bazę wiedzy dla osób konfigurujących DNS.
   - (C) Ułatwia rozmowę z supportem GitHub.
   **Decyzja:** A jako instrukcja recovery, wzmocniona bazą wiedzy z (B).
5. Dlaczego należy wykonywać `dig` i `curl` po każdej zmianie?
   - (A) `dig` potwierdza propagację rekordu DNS.
   - (B) `curl` weryfikuje certyfikat HTTPS i status 200.
   - (C) Zestaw narzędzi tworzy log audytowy.
   **Decyzja:** A jako weryfikacja DNS, połączona z testem HTTPS z (B).

# Notatki (Faza 4)
- Strona „Organizacja” zawiera panel komentarzy „Oceń pomysł” z lokalnym zapisem (`localStorage`) i komunikatami statusu.
- Formularz „Dodaj pomysł” korzysta z fetch, waliduje tytuł/treść i komunikuje status przez `aria-live`.
- Backend zapisuje dane w SQLite i pliku tekstowym, a testy API pilnują limitów, walidacji i logowania.

# Notatki (Faza 5)
- Front wczytuje `BACKEND_URL` z `config.json`, dzięki czemu GitHub Pages współpracuje z tunelem Flask.
- Duplikat `config.json` w katalogu głównym eliminuje 404 podczas serwowania strony spod `/Kroniki_Ognia/`.
- `scripts/smoke.sh` umożliwia szybki smoke test tunelu.
- Endpoint `/api/health` raportuje gotowość storage i jest sprawdzany przez `tests/test_api.py`.
- README zawiera sekcję „Dev: Quick Tunnel → lokalny Flask” z krokami konfiguracji tunelu.
- `POST /api/ideas` wymaga nagłówka `X-API-Key` (domyślnie `dev-key`) i potrafi przekazać zdarzenie do n8n w tle.
- Forwarding n8n ma domyślny adres developerski (`http://localhost:5678/webhook-test/f11f16e1-4e7e-4fa6-b99e-bf1e47f02a50`) oraz alias payloadu `pomysł` dla lokalnych scenariuszy.
- Workflow `ci.yml` uruchamia `pytest`, `ruff` i `mypy` przy każdym PR.
- Test preflight CORS pilnuje, że nagłówek `X-API-Key` przechodzi z GitHub Pages na tunelowany backend.

## 5xWhy — Dlaczego dokumentujemy Quick Tunnel w README
1. Dlaczego potrzebna jest sekcja krok po kroku?
   - (A) Agent backendowy musi szybko odtworzyć tunel bez wertowania notatek.
   - (B) Nowi wolontariusze frontu chcą samodzielnie potwierdzić konfigurację.
   - (C) CI wymaga jasnego punktu odniesienia dla smoke testu.
   **Decyzja:** A jako krytyczna instrukcja operacyjna, uzupełniona onboardingiem z (B).
2. Dlaczego kopiujemy przykładowy URL tunelu?
   - (A) Zapobiega literówkom w `config.json` przy ręcznej edycji.
   - (B) Ułatwia testy manualne smoke, bo nie trzeba pamiętać struktury hosta.
   - (C) Skraca opis w innych dokumentach.
   **Decyzja:** B jako wsparcie smoke testu, rozszerzone o bezpieczeństwo konfiguracji z (A).
3. Dlaczego przypominamy o dwóch kopiach `config.json`?
   - (A) Front serwowany spod `/Kroniki_Ognia/` potrzebuje wariantu w `public/`.
   - (B) Test `tests/test_config_json.py` blokuje rozjazdy.
   - (C) Synchronizacja ręczna jest podatna na błędy przy szybkim hotfixie.
   **Decyzja:** C jako motywacja do dyscypliny, wzmocniona testem z (B).
4. Dlaczego sekcja wskazuje `cloudflared tunnel --url`?
   - (A) Komenda jest mniej oczywista niż `cloudflared tunnel run` i bywa mylona.
   - (B) Zapewnia zgodność z polityką CTO (żadnych skrótów shell bez kontekstu).
   - (C) Ułatwia łączenie z lokalnym portem 5000 bez dodatkowych flag.
   **Decyzja:** A jako zapobieganie błędom, uzupełnione prostotą z (C).
5. Dlaczego workflow CI ma instalować `pytest`, `ruff`, `mypy` jawnie?
   - (A) Gwarantuje wersje zgodne z instrukcjami CTO niezależnie od `requirements.txt`.
   - (B) Pozwala na szybkie rozszerzenie zestawu narzędzi (np. `types-requests`).
   - (C) Zapewnia, że smoke README ma realne odwzorowanie w CI.
   **Decyzja:** A jako gwarancja polityki narzędziowej, rozszerzona elastycznością z (B).

## 5xWhy — Dlaczego dodajemy klucz API i forwarding do n8n
1. Dlaczego `POST /api/ideas` potrzebuje dodatkowego zabezpieczenia?
   - (A) Publiczny tunel łatwo nadużyć bez jakiejkolwiek ochrony.
   - (B) Klucz API pozwala śledzić źródła ruchu między środowiskami.
   - (C) Pozwala szybko wygasić formularz bez dotykania kodu.
   **Decyzja:** A jako tarcza przed nadużyciami, uzupełniona inspekcją źródeł z (B).
2. Dlaczego stawiamy na nagłówek `X-API-Key`, a nie ukryte pole formularza?
   - (A) Nagłówek można rotować bez edycji markup.
   - (B) Ukryte pole jest trywialne do podejrzenia i nadpisania przez boty.
   - (C) Nagłówek nie trafia do logów GitHub Pages.
   **Decyzja:** A jako elastyczność operacyjna, wzmocniona prywatnością z (C).
3. Dlaczego forwarding do n8n wykonujemy asynchronicznie?
   - (A) Użytkownik natychmiast dostaje `201`, nawet jeśli n8n chwilowo nie odpowiada.
   - (B) Pozwala delegować retry na poziomie scenariusza n8n.
   - (C) Otwiera drogę do kolejnych integracji (np. Discord) bez zmiany kontraktu API.
   **Decyzja:** A jako UX-first, doprawione skalowalnością z (C).
4. Dlaczego generujemy `event_id` dla każdego zgłoszenia?
   - (A) Idempotencja przepływów n8n bazuje na unikalnym identyfikatorze.
   - (B) Łatwiej korelować logi SQLite i pliki tekstowe z webhookami.
   - (C) Pomaga przy audycie i raportach manualnych.
   **Decyzja:** A jako klucz do deduplikacji, poszerzony obserwowalnością z (B).
5. Dlaczego formularz odczytuje klucz z `data-api-key`?
   - (A) Pozwala konfigurować różne wartości per środowisko bez bundlera.
   - (B) Testy end-to-end zachowują kompatybilność dzięki domyślnemu `dev-key`.
   - (C) CTA HTML pozostaje czyste — brak dodatkowych inputów w treści formularza.
   **Decyzja:** A jako wsparcie środowisk, rozszerzone kompatybilnością z (B).

## 5xWhy — Dlaczego aliasujemy payload jako `pomysł`
1. Dlaczego webhook potrzebuje sekcji `pomysł` obok `idea`?
   - (A) Scenariusz n8n jest przygotowany pod polskie nazwy pól.
   - (B) Alias upraszcza mapowanie danych w już istniejących node'ach n8n.
   - (C) Zapobiega konieczności refaktoryzacji historycznych przepływów.
   **Decyzja:** A jako zgodność z istniejącym scenariuszem, wzmocniona łatką migracyjną z (B).
2. Dlaczego warto utrzymać jednocześnie sekcję `idea`?
   - (A) Zapewnia kompatybilność z anglojęzycznymi integracjami (np. Discord, Slack).
   - (B) Testy backendu już walidują strukturę `idea` i łatwo je rozbudować o alias.
   - (C) Chroni przyszłe automatyzacje analityczne, które korzystają z wersji angielskiej.
   **Decyzja:** C jako inwestycja w przyszłe integracje, rozszerzona testowalnością z (B).
3. Dlaczego ustawiamy domyślny webhook developerski?
   - (A) Przyspiesza konfigurację lokalną bez potrzeby eksportu zmiennych środowiskowych.
   - (B) Pozwala testom manualnym od razu trafiać do n8n uruchomionego na maszynie developera.
   - (C) Chroni przed zapomnieniem zmiennej `N8N_WEBHOOK_URL` podczas warsztatów.
   **Decyzja:** A jako optymalizacja onboardingu, dopełniona wygodą z (B).
4. Dlaczego nagłówek autoryzacji jest opcjonalny?
   - (A) Lokalne instancje n8n często nie wymagają tokenu i odrzucałyby pusty header.
   - (B) Pozwala łatwo przełączać środowiska bez restartu backendu.
   - (C) Upraszcza debugowanie requestów HTTP.
   **Decyzja:** A jako zgodność z lokalnym n8n, połączona z ergonomią z (C).
5. Dlaczego test `test_post_ideas_forwards_to_n8n` powinien sprawdzać alias?
   - (A) Chroni kontrakt integracji przy przyszłych refactorach.
   - (B) Zmusza do utrzymania spójności między polską a angielską strukturą.
   - (C) Zapobiega cichym regresjom podczas optymalizacji payloadu.
   **Decyzja:** B jako gwarancja spójności, rozszerzona osłoną regresji z (C).

## 5xWhy — Dlaczego rozszerzamy CORS o nagłówek `X-API-Key`
1. Dlaczego przeglądarka blokowała formularz mimo poprawnego klucza API?
   - (A) Preflight CORS nie znajdował `X-API-Key` w `Access-Control-Allow-Headers`.
   - (B) Tunel cloudflared okresowo zrywał sesję i zwracał błędy 5xx.
   - (C) Frontend korzystał z niezsynchronizowanego `config.json`.
   **Decyzja:** A jako blokada krytyczna, uzupełniona monitoringiem tunelu z (B).
2. Dlaczego nagłówek nie był dodany do konfiguracji CORS?
   - (A) Lista dozwolonych nagłówków została przygotowana manualnie i obejmowała tylko `Content-Type` i `Authorization`.
   - (B) Polegano na domyślnej konfiguracji Flask-CORS.
   - (C) Nazewnictwo nagłówków nie było udokumentowane w README.
   **Decyzja:** A jako realna luka, rozszerzona o dokumentację z (C).
3. Dlaczego manualna lista pozostała niezmieniona mimo dodania klucza API?
   - (A) Review backendu koncentrował się na walidacji payloadu, nie na nagłówkach CORS.
   - (B) Brakowało testu kontraktowego sprawdzającego preflight.
   - (C) Tunel w testach lokalnych pomijał nagłówek `X-API-Key`.
   **Decyzja:** B jako brakujący test regresyjny, uzupełniony focus-em review z (A).
4. Dlaczego nie zidentyfikowano problemu przed publikacją na GitHub Pages?
   - (A) Scenariusze QA zakładały ten sam host dla frontu i backendu.
   - (B) Nie przeprowadzono E2E w trybie `https://pkrokosz.github.io` + tunel.
   - (C) Komunikaty konsoli nie były agregowane w dokumentacji.
   **Decyzja:** B jako luka testowa, rozszerzona o agregację błędów z (C).
5. Dlaczego dodajemy automatyczny test CORS?
   - (A) Chroni przed regresją przy kolejnej zmianie nagłówków.
   - (B) Umożliwia szybkie wykrycie problemu w CI zamiast w produkcji.
   - (C) Dokumentuje wymagania CTO względem bezpieczeństwa tunelu.
   **Decyzja:** A jako tarcza regresji, zasilona szybkim feedbackiem z (B).

## 5xWhy — Dlaczego dodajemy nagłówek Authorization dla formularza pomysłów
1. Dlaczego front musi wysyłać `Authorization: Bearer` oprócz `X-API-Key`?
   - (A) Nowa polityka bezpieczeństwa partnera wymaga standardowego nagłówka Bearer.
   - (B) Tunelowane requesty łatwiej debugować w narzędziach, które wykrywają nagłówek Authorization.
   - (C) Umożliwia przyszłe scalenie z usługami oczekującymi OAuth 2.0.
   **Decyzja:** A jako wymóg zewnętrzny, rozszerzony ergonomią debuggera z (B).
2. Dlaczego utrzymujemy jednocześnie `X-API-Key`?
   - (A) Istniejące integracje i skrypty smoke wciąż używają starego nagłówka.
   - (B) Pozwala to na płynne wycofywanie fallbacku bez przestojów.
   - (C) Testy kontraktowe już operują na kluczu w tym nagłówku.
   **Decyzja:** A jako zgodność wsteczna, wzmocniona ścieżką migracji z (B).
3. Dlaczego backend porównuje oba nagłówki przez funkcję pomocniczą?
   - (A) Zapewnia jedno źródło prawdy dla sposobu odczytu klucza.
   - (B) Upraszcza dodanie kolejnych schematów (np. `ApiKey <token>`).
   - (C) Ułatwia testowanie i mockowanie w pytest.
   **Decyzja:** A jako baza utrzymaniowa, uzupełniona elastycznością z (B).
4. Dlaczego testujemy zarówno Bearer, jak i legacy `X-API-Key`?
   - (A) Chroni przed regresją podczas okresu przejściowego.
   - (B) Dokumentuje oficjalnie wspierane scenariusze w CI.
   - (C) Zapewnia, że stare klienckie automaty nie przestaną działać z dnia na dzień.
   **Decyzja:** A jako tarcza regresji, połączona z dokumentacją w (B).
5. Dlaczego dodaliśmy parametr `?v=20241005` do importu `idea-form.js`?
   - (A) Wymusza odświeżenie cache przeglądarek po zmianie nagłówków.
   - (B) Pozwala łatwo identyfikować wersje formularza podczas QA.
   - (C) Minimalizuje ryzyko, że GitHub Pages zaserwuje starą wersję modułu.
   **Decyzja:** C jako kluczowy mechanizm bustingu cache, wsparty diagnostyką z (B).

# Notatki (Iteracja — higiena dokumentacji i ambient 2024-09)
- README, plan, zadania, notatki i CONTEXT zostały odchudzone z duplikatów, a nagłówki są unikalne.
- Dodano test `tests/test_documentation.py`, który blokuje powrót zduplikowanych sekcji README.
- Ambientowe tła otrzymały wyższe `opacity`, filtr saturacji oraz test weryfikujący progi widoczności.
- Workflow CI (`codex.yml`) uruchamia teraz `ruff check .`, `mypy app.py` oraz `pytest` zgodnie z wymaganiami CTO persony.

## 5xWhy — Dlaczego czyścimy dokumentację
1. Dlaczego usuwamy zduplikowane sekcje?
   - (A) Duplikaty wprowadzały rozbieżności i dezorientowały zespół.
   - (B) Zwiększały koszty utrzymania przy każdej aktualizacji.
   - (C) Utrudniały odnalezienie właściwych instrukcji przy onboardingach.
   **Decyzja:** A jako natychmiastowe ryzyko błędnych decyzji, wzmocnione redukcją kosztu z (B).
2. Dlaczego potrzebny jest test pilnujący nagłówków README?
   - (A) Manualny review nie zawsze wychwyci regresje.
   - (B) Automatyczny strażnik skraca feedback loop.
   - (C) Zapewnia metrykę jakości dokumentacji.
   **Decyzja:** B jako szybki feedback, uzupełniony o prewencję regresji z (A).
3. Dlaczego kontynuacja obejmuje także `docs/`?
   - (A) Główne dokumenty planistyczne są równie podatne na duplikaty.
   - (B) Zapewnia spójne standardy w całym repozytorium.
   - (C) Przygotowuje grunt pod automatyczny raport zmian.
   **Decyzja:** B jako harmonizacja standardów, rozszerzona o niezawodność z (A).
4. Dlaczego dokumentujemy zmiany w README i notesach?
   - (A) README jest pierwszym punktem styku dla nowego agenta.
   - (B) Notesy zachowują kontekst decyzji dla audytu CTO.
   - (C) Ułatwia to przygotowanie raportów fazowych.
   **Decyzja:** A jako główny kanał komunikacji, wsparte pamięcią projektową z (B).
5. Dlaczego CI uruchamia `ruff`, `mypy`, `pytest` po tej iteracji?
   - (A) Wymóg CTO persony zakłada lint, typowanie i testy jako bloker.
   - (B) Automatyczny zestaw zmniejsza ryzyko regresji przy kolejnych fazach.
   - (C) Ułatwia przygotowanie raportów jakościowych.
   **Decyzja:** A jako polityka jakości, wzmocniona stabilnością z (B).

# Notatki (Faza 6)
- Zakładki edycji na kafelkach umożliwiają korekty narracji bez edycji kodu; zapis wykorzystuje `localStorage`, a brak dostępu komunikowany jest w UI.
- Moduł `assets/editable-tiles.js` obserwuje DOM (MutationObserver), dzięki czemu działa także na dynamicznych kafelkach `organizacja.html`.
- Styl `tile-edit-*` zachowuje klimat żaru i nie narusza istniejących hoverów kart, ponieważ aktywne karty otrzymują dodatkowy margines na panel edycji.

## 5xWhy — Dlaczego edycja kafelków zostaje po stronie przeglądarki
1. Dlaczego korzystamy z `localStorage`, a nie backendu?
   - (A) Zapewnia natychmiastowe, offline-ready modyfikacje bez dodatkowej infrastruktury.
   - (B) Upraszcza kontrolę wersji, bo zmiany nie opuszczają przeglądarki.
   - (C) Chroni narrację przed nieautoryzowanymi wpisami użytkowników.
   **Decyzja:** A jako baza MVP (brak backendu), wzmocniona bezpieczeństwem z (C).
2. Dlaczego interfejs to zakładka po prawej stronie?
   - (A) Nie zasłania kluczowej treści i nie wymaga przebudowy layoutu kafelka.
   - (B) Podkreśla modularność kart w duchu „fiszki archiwalnej”.
   - (C) Zapewnia spójność z innymi kontrolkami (np. panelami feedbacku) poprzez zachowanie pionowych linii.
   **Decyzja:** A jako ergonomia, wzbogacona wizualnym motywem archiwalnym z (B).
3. Dlaczego tryb edycji wykorzystuje `contenteditable` zamiast formularza modalnego?
   - (A) Pozwala zachować istniejące formatowanie (np. listy, pogrubienia) bez konwersji.
   - (B) Minimalizuje liczbę kliknięć — edycja odbywa się w miejscu.
   - (C) Ułatwia kopiowanie fragmentów do innych narzędzi bez przełączania kontekstu.
   **Decyzja:** A jako gwarancja zachowania struktury, rozszerzona o szybkość z (B).
4. Dlaczego blokujemy edycję przy braku `localStorage` zamiast pozwalać na nietrwałe zmiany?
   - (A) Zapobiega złudzeniu zapisania i utracie pracy przy odświeżeniu.
   - (B) Upraszcza komunikaty dostępności — jasny stan „edytowalne” vs „zablokowane”.
   - (C) Zmniejsza powierzchnię błędów w testach regresji.
   **Decyzja:** A jako ochrona użytkownika, doprawiona klarownością komunikatów z (B).
5. Dlaczego moduł obserwuje DOM przez `MutationObserver`?
   - (A) Strona `organizacja.html` renderuje kafelki dynamicznie.
   - (B) Przygotowuje grunt pod przyszłe lazy-loady i generowane sekcje.
   - (C) Zapobiega powielaniu inicjalizacji po SPA-like aktualizacjach.
   **Decyzja:** A jako wymóg kompatybilności, uzupełniony przyszłościowością z (B).

## Raport agenta — Faza 5 (CORS preflight)
- **Co zostało zrobione:** Formularz „Dodaj pomysł” znów działa spod GitHub Pages dzięki rozszerzeniu CORS o nagłówek `X-API-Key` oraz testowi preflight zabezpieczającemu kontrakt.
- **Dlaczego:** Zrezygnowaliśmy z poluzowania polityki CORS (`*`/dowolne nagłówki), by utrzymać kontrolę hostów i spełnić wymagania CTO dotyczące bezpieczeństwa tunelu.
- **Cel funkcji i stan pipeline’u:** Zmiana uszczelnia fazę 5 (tunel backendu) i utrzymuje pipeline QA (pytest/ruff/mypy) zielony — test regresyjny chroni kontrakt.
- **Kolejny krok ku MVP:** Priorytetem jest automatyczny monitoring tunelu (np. zadanie cronowe uruchamiające smoke test) — prowadzi do Zadania 7 w fazie 5.
