# Notatki (Faza 1)
- Repo zawiera trzy główne dokumenty HTML z bogatą treścią narracyjną.
- Brak wspólnego stylu i nawigacji — konieczna centralizacja w `assets/styles.css`.
- Do dodania `index.html` jako landing page dla GitHub Pages.
- Należy utrzymać oryginalne teksty bez zmian merytorycznych.
- Nowa nawigacja została wdrożona wraz z testem `tests/test_navigation.py`; wszystkie strony korzystają z identycznego nagłówka.
- `.gitignore` rozszerzono o standardowe wpisy (środowiska, cache, logi), aby repo pozostawało wolne od artefaktów lokalnych i binarnych.

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
   **Decyzja:** A jako ochrona przed inflacją repo, z dodatkowym onboardingiem z (C).
3. Dlaczego warto ignorować katalogi edytorów (`.idea/`, `.vscode/`)?
   - (A) Każdy agent korzysta z innej konfiguracji IDE.
   - (B) Pliki te często zawierają ścieżki lokalne i sekrety.
   - (C) Zmiany w tych plikach utrudniają code review.
   **Decyzja:** A jako gwarancja neutralności narzędzi, poszerzona o bezpieczeństwo z (B).
4. Dlaczego wpisy dla logów i plików `.env` są krytyczne?
   - (A) Zapobiegają wyciekowi danych konfiguracyjnych lub tokenów.
   - (B) Minimalizują konflikty podczas debugowania.
   - (C) Wspierają pipeline bezpieczeństwa repo.
   **Decyzja:** A jako ochrona tajemnic, z kontrolą bezpieczeństwa z (C).
5. Dlaczego potrzebny jest kolejny krok automatyzujący walidację `.gitignore`?
   - (A) Manualna kontrola może zostać pominięta w przyszłych iteracjach.
   - (B) Automatyzacja pozwoli szybciej wykrywać regresje.
   - (C) Wzmacnia kulturę narzędziową przed MVP.
   **Decyzja:** B jako impuls do CI, wzbogacony o kulturę narzędziową z (C).

# Notatki (Faza 2)
- Paleta barw została przygaszona wokół barw ziemistych, dodano ambientową warstwę tła i animację pulsującą, zachowując czytelność tekstów.
- Nawigacja na urządzeniach mobilnych przechodzi w układ kolumnowy, a karty otrzymują mniejsze paddingi, co poprawia ergonomię.
- Powstał zestaw testów `tests/test_responsive_theme.py` weryfikujących zarówno bloki @media, jak i obecność efektów graficznych.
- Wdrożono wielowarstwowe, rozmyte tła z zasobów `img/` — trzy obrazy na podstronę płynnie przesuwają się horyzontalnie i respektują `prefers-reduced-motion`.
- Wzmocniono ekspozycję ambientowych warstw: zwiększona jasność, saturacja i amplituda ruchu sprawiają, że galeria jest wyraźnie widoczna nawet pod nakładającymi się efektami.
- Landing wzbogacono o sekcję visual key "Próby Płomienia" z trzema progami (Iskra, Żar, Płomień), wykorzystującą zdjęcia `img/1.jpg`, `img/4.jpg`, `img/7.jpg` oraz prowadzącą do kluczowych podstron.
- Sekcja visual key otrzymała przycisk autoodtwarzania z respektowaniem `prefers-reduced-motion` i komunikatami statusu.

## 5xWhy — Wzmocnienie widoczności ambientu
1. Dlaczego należy zwiększyć jasność i saturację warstw?
   - (A) Aby obrazki były zauważalne mimo rozmycia i niskiej przezroczystości.
   - (B) Aby zachować spójność kolorystyczną z narracją o żarze i płomieniach.
   - (C) Aby umożliwić wyróżnienie sekcji CTA bez dodatkowych elementów.
   **Decyzja:** A jako główna potrzeba, uzupełniona o narracyjny charakter z (B).
2. Dlaczego animacja powinna mieć większą amplitudę horyzontalnego ruchu?
   - (A) Małe przesunięcia były praktycznie niezauważalne dla odbiorcy.
   - (B) Większa amplituda oddaje efekt falowania żaru na wietrze.
   - (C) Ułatwia testowanie regresji wizualnych w przyszłych iteracjach.
   **Decyzja:** A jako priorytet użytkowy, z dodaniem klimatu z (B).
3. Dlaczego należy skorygować relację `z-index` między ambientem a innymi efektami?
   - (A) Poprzednio nakładające się pseudo-elementy maskowały tła.
   - (B) Wyższy `z-index` ułatwia przyszłą rozbudowę (np. dodatkowe efekty świetlne).
   - (C) Dzięki temu animacja nie znika na urządzeniach mobilnych z niższą wydajnością.
   **Decyzja:** A jako kluczowe, rozszerzone o przyszłościowość z (B).
4. Dlaczego należy odnotować zmianę w dokumentacji?
   - (A) Nowi agenci muszą wiedzieć, że widoczność jest wymogiem jakości.
   - (B) README stanowi checklistę akceptacyjną przed wdrożeniem.
   - (C) Notatki tworzą historię decyzji potrzebną do audytu.
   **Decyzja:** B jako punkt kontrolny, wzmocniony archiwizacją z (C).
5. Dlaczego trzeba zaplanować tryb akcentowy ekspozycji?
   - (A) Niektóre sekcje (np. CTA) mogą potrzebować mocniejszego tła.
   - (B) Zmiany oparte na sekcjach umożliwią dalsze testy kontrastów.
   - (C) Przygotowuje grunt pod interaktywne sterowanie w kolejnych fazach.
   **Decyzja:** A jako najbliższa potrzeba, doprawiona testowalnością z (B).

## 5xWhy — Ambientowe galerie tła
1. Dlaczego dodajemy wielowarstwowe galerie tła?
   - (A) Aby wizualnie zróżnicować każdą podstronę bez naruszania treści.
   - (B) Aby wykorzystać istniejące zdjęcia z katalogu `img/` zamiast szukać nowych zasobów.
   - (C) Aby wzmocnić immersję przez subtelny ruch.
   **Decyzja:** C jako cel przewodni, wzbogacony o kuratorskie wykorzystanie istniejących zdjęć z (B).
2. Dlaczego ruch tła powinien być delikatny i horyzontalny?
   - (A) Horyzontalny dryf koresponduje z rozpościeraniem się płomieni na wietrze.
   - (B) Pionowy ruch mógłby zakłócić czytelność sekcji tekstowych.
   - (C) Delikatność pomaga uniknąć rozpraszania odbiorcy.
   **Decyzja:** A jako motyw narracyjny, doprawiony o ograniczenie rozpraszania z (C).
3. Dlaczego potrzebna jest automatyczna weryfikacja obrazów w CSS?
   - (A) Zapobiega przypadkowemu usunięciu któregoś z plików `img/`.
   - (B) Upewnia, że każda podstrona ma przypisane trzy warstwy.
   - (C) Przygotowuje grunt pod dalszą automatyzację parametrów animacji.
   **Decyzja:** B jako główny wymóg jakości, rozszerzony o kontrolę zasobów z (A).
4. Dlaczego blok `prefers-reduced-motion` musi obejmować też tła?
   - (A) Odbiorcy wrażliwi na ruch powinni móc bezpiecznie przeglądać repozytorium.
   - (B) Spójność dostępności buduje zaufanie do całej witryny.
   - (C) Ułatwia audyt CTO personie.
   **Decyzja:** A jako wymóg dostępności, połączony ze spójnością marki z (B).
5. Dlaczego animacje są oparte na czystym CSS zamiast JS?
   - (A) CSS zapewnia niższy narzut wydajnościowy.
   - (B) Brak JS upraszcza utrzymanie na GitHub Pages.
   - (C) Pozwala zachować kompatybilność z dotychczasowymi testami.
   **Decyzja:** B jako gwarancja prostoty, uzupełniona o wydajność z (A).

## 5xWhy — Sekcja visual key
1. Dlaczego potrzebujemy sekcji visual key na landingu?
   - (A) Aby pokazać klimat projektu przed formularzem "Dodaj pomysł".
   - (B) Aby wykorzystać istniejące zdjęcia `img/` jako natychmiastowe odwołania.
   - (C) Aby zaoferować mistrzom gry szybki pitch treści podstron.
   **Decyzja:** A jako główny impuls, wzmocniony biblioteką zdjęć z (B).
2. Dlaczego sekcja powinna mieć trzy progi narracyjne?
   - (A) Tryptyk odzwierciedla strukturę repozytorium (świat, narzędzia, plan).
   - (B) Trzy kroki ułatwiają prowadzenie prezentacji live.
   - (C) Parzysta liczba kafelków trudniej buduje dramaturgię.
   **Decyzja:** A jako fundament, uzupełniony o rytm prezentacji z (B).
3. Dlaczego zastosowaliśmy tryb autoodtwarzania zamiast slidera?
   - (A) Autoodtwarzanie można włączyć lub pominąć — nie wymusza ruchu.
   - (B) Slider wymagałby dodatkowej paginacji i kontroli focusu.
   - (C) Przycisk łatwiej testować i respektuje dostępność.
   **Decyzja:** A zapewnia kontrolę użytkownikowi, wzmocniona prostotą testów z (C).
4. Dlaczego status sekcji jest komunikowany przez `aria-live`?
   - (A) Osoby niewidzące muszą wiedzieć, czy autoodtwarzanie działa.
   - (B) Pozwala raportować blokadę przy `prefers-reduced-motion`.
   - (C) Wspiera QA przy sprawdzaniu zachowania przycisku.
   **Decyzja:** A jako wymóg dostępności, rozszerzony o klarowne komunikaty z (B).
5. Dlaczego obrazy pochodzą z `img/1.jpg`, `img/4.jpg`, `img/7.jpg`?
   - (A) Otwierają i zamykają istniejące ambienty, zachowując spójność.
   - (B) Unikamy duplikacji plików i dbamy o testy, które już pilnują katalogu.
   - (C) Ten zestaw pokrywa drogę od wprowadzenia po finał dnia.
   **Decyzja:** C jako narracyjny łuk, wsparte przez spójność zasobów z (A).

# Notatki (Faza 3)
- Dodano wspólny baner "flying object" prowadzący do Notebook LM z bazą wiedzy brainstormu; zachowuje klimat projektu dzięki animowanej ikonie zwiadowcy.
- Test `tests/test_notebook_banner.py` kontroluje link, atrybuty bezpieczeństwa oraz komunikat narracyjny.
- Baner respektuje preferencje ograniczonego ruchu i układ mobilny, dzięki czemu CTA pozostaje dostępne.
- Baner uzupełniono o CTA do archiwum Google Drive z zasobami wspierającymi produkcję; kolorowa ikona sygnalizuje, że chodzi o repozytorium plików wizualnych.
- Plik `.nojekyll` w katalogu głównym blokuje przetwarzanie Jekylla na GitHub Pages, dzięki czemu cała struktura repozytorium jest serwowana bezpośrednio jako statyczna witryna i test `tests/test_nojekyll.py` będzie szybko alarmował o brakach.

## 5xWhy — Dlaczego link do archiwum Google Drive
1. Dlaczego dodajemy link do Google Drive?
   - (A) Aby zespół szybko dotarł do plików referencyjnych (zdjęcia, moodboardy).
   - (B) Aby zapewnić redundancję wobec Notebook LM na wypadek awarii.
   - (C) Aby przygotować repozytorium pod przyszły import zasobów wizualnych.
   **Decyzja:** A jako cel nadrzędny, rozszerzone o odporność z (B).
2. Dlaczego CTA powinno być w banerze "flying object"?
   - (A) Baner jest wspólnym, natychmiast widocznym elementem na każdej podstronie.
   - (B) Osadzony link w treści mógłby zginąć w długich sekcjach opisowych.
   - (C) Umożliwia wykorzystanie istniejącej metafory zwiadowcy.
   **Decyzja:** A zapewnia najwyższą widoczność, doprawiona narracyjną spójnością z (C).
3. Dlaczego stosujemy ikonę w barwach Google?
   - (A) Rozpoznawalny kształt przyspiesza identyfikację zasobu.
   - (B) Kolorowy element równoważy stonowaną paletę i przyciąga wzrok.
   - (C) Wspiera przyszłe testy automatyczne przez możliwość wykrycia atrybutu.
   **Decyzja:** A jako walor UX, poszerzony o testowalność z (C).
4. Dlaczego zachowujemy ten sam tryb otwierania (`target="_blank"`, `rel="noopener"`)?
   - (A) Zapobiega utracie kontekstu strony podczas przeglądania plików.
   - (B) Utrzymuje standard bezpieczeństwa dla linków zewnętrznych.
   - (C) Ułatwia zespół organizacyjny powrót do repo po sprawdzeniu zasobów.
   **Decyzja:** B jako wymóg bezpieczeństwa, połączony z wygodą z (A).
5. Dlaczego potrzebny jest test automatyczny dla Google Drive?
   - (A) Chroni przed przypadkowym usunięciem linku lub ikony.
   - (B) Dokumentuje konwencję klas CSS dla banera.
   - (C) Przygotowuje grunt pod przyszłe rozszerzenia (np. dodatkowe CTA).
   **Decyzja:** A jako główny strażnik, z rozszerzeniem dokumentacyjnym z (B).

## 5xWhy — Responsywność i nastrój
1. Dlaczego należy zmienić paletę i układ?
   - (A) By dopasować wizję artystyczną do nastroju opowieści.
   - (B) By poprawić kontrast w warunkach słabego oświetlenia mobilnego.
   - (C) By wyróżnić repo jako gotowy MVP.
   **Decyzja:** A z dodatkiem kontroli kontrastu z (B).
2. Dlaczego wizja artystyczna wymaga ambientowych efektów?  
   - (A) Utrzymuje narracyjną spójność z motywem ognia.  
   - (B) Zapewnia unikalność wobec konkurencyjnych projektów.  
   - (C) Działa jako subtelny przewodnik wzroku.  
   **Decyzja:** C jako kluczowa funkcja, rozszerzona o delikatny klimat z (A).
3. Dlaczego przewodnik wzroku powinien działać także na mobile?  
   - (A) Smartfony stanowią główny kanał konsumpcji.  
   - (B) Użytkownicy oczekują spójnego doświadczenia.  
   - (C) Minimalizacja bounce rate na stronie.  
   **Decyzja:** A wzmocnione o oczekiwania użytkowników z (B).
4. Dlaczego główny kanał konsumpcji wymusza testy automatyczne?  
   - (A) Zmiany CSS są podatne na regresje.  
   - (B) Pipeline CI wymaga mierzalnych kryteriów.  
   - (C) Przygotowuje grunt pod kolejne fazy.  
   **Decyzja:** B jako pewny fundament, z rozszerzeniem o prewencję regresji z (A).
5. Dlaczego pipeline potrzebuje dokumentacji zmian?  
   - (A) Zapewnia kontekst dla przyszłych agentów.  
   - (B) Ułatwia audyt CTO persony.  
   - (C) Buduje pamięć projektową (CONTEXT).
   **Decyzja:** A jako wiodące, uzupełnione o audytowalność z (B).

# Notatki (Faza 3)
- Repozytorium rezygnuje z przechowywania pliku `CNAME`; konfiguracja domeny odbywa się ręcznie w ustawieniach GitHub Pages.
- Test `tests/test_custom_domain.py` pilnuje braku pliku `CNAME` i wymusza aktualność dokumentacji opisującej proces ustawiania domeny.
- README oraz ADR #0002 aktualizują instrukcję DNS, dodając przypomnienie o potwierdzaniu zmian w interfejsie Pages.
- Plan i tasks opisują nowe zadania: zabezpieczenie przed przypadkowym dodaniem `CNAME` oraz przyszłe monitorowanie certyfikatu HTTPS i statusu domeny.
- Skorygowano instrukcję DNS tak, by jasno wskazywała na docelowy host GitHub Pages `pkr0kosz.github.io` i ewentualną domenę lustrzaną `.com`.

# Notatki (Faza 5)
- Front wczytuje `BACKEND_URL` z `public/config.json`, dzięki czemu GitHub Pages może wskazywać na tunel `https://api-kroniki.<MOJA-DOMENA>` bez przebudowy frontu.
- Duplikat `config.json` w katalogu głównym eliminuje 404 podczas serwowania strony spod `/Kroniki_Ognia/` i jest weryfikowany testem `tests/test_config_json.py`.
- Formularz otrzymał pola na tytuł, treść i opcjonalne tagi; JS ustawia `form.action` po załadowaniu konfiguracji.
- Backend Flask wymusza schemat `{title, content, tags?}`, zapisuje tagi w JSON oraz loguje wpisy z timestampem. CORS ogranicza pochodzenie do GitHub Pages i tunelu, a Flask-Limiter blokuje flood do 10/min.
- `tests/test_api.py` oraz zaktualizowane `tests/test_idea_submission.py` pilnują kontraktu odpowiedzi `{"id": ..., "status": "ok"}` oraz poprawnego utrwalenia danych.
- README dokumentuje tryb tunelowania i skrypt `scripts/smoke.sh`, który wykonuje POST do publicznego endpointu.

## 5xWhy — Konfiguracja tunelu backendu
1. Dlaczego front powinien ładować URL backendu z `config.json`?
   - (A) Pozwala przełączać środowiska (lokalne/tunel) bez rekompilacji.
   - (B) Ułatwia nietechnicznym osobom zmianę adresu bez dotykania JS.
   - (C) Chroni przed wyciekami, bo nie commitujemy prywatnych adresów w kodzie.
   **Decyzja:** A jako główny cel elastyczności, rozszerzony o prosty onboarding z (B).
2. Dlaczego ograniczamy CORS do trzech hostów?
   - (A) Minimalizujemy powierzchnię ataku XHR.
   - (B) Jasno sygnalizujemy oczekiwany ruch z Pages/tunelu.
   - (C) Przygotowujemy się pod ewentualne środowisko stagingowe.
   **Decyzja:** A jako wiodący aspekt bezpieczeństwa, wzmocniony obserwacją ruchu z (B).
3. Dlaczego warto dodać rate limit 10/min?
   - (A) Chroni tunel przed floodem podczas eventu.
   - (B) Stabilizuje działanie SQLite na słabszych maszynach.
   - (C) Zapobiega przypadkowym pętlom w testach.
   **Decyzja:** A jako tarcza operacyjna, doprawiona minimalizacją obciążenia z (B).
4. Dlaczego zachowujemy kompatybilność z polem `idea`?
   - (A) Istniejące zgłoszenia mogą nadal używać starej wersji formularza.
   - (B) Ułatwia rollback bez migracji.
   - (C) Pozwala importować historyczne wpisy tekstowe.
   **Decyzja:** A jako ciągłość usługi, z bonusem migracyjnym z (C).
5. Dlaczego smoke test w pytest i bashu to konieczność?
   - (A) Pytest zapewnia regresję w CI.
   - (B) Bash pozwala szybko sprawdzić tunel po wdrożeniu.
   - (C) Dublet testów zwiększa zaufanie architekta.
   **Decyzja:** A jako fundament w pipeline, rozszerzony o operacyjny komfort z (B).

## 5xWhy — Podwójny `config.json`
1. Dlaczego potrzebujemy kopii `config.json` w katalogu głównym?
   - (A) GitHub Pages dla projektów (`/Kroniki_Ognia/`) szuka plików względem ścieżki repozytorium.
   - (B) Narzędzia lokalne (np. `python -m http.server`) serwują root bez katalogu `public/`.
   - (C) Dokumentacja staje się spójniejsza, gdy wskazuje jeden plik konfiguracyjny.
   **Decyzja:** A jako wymóg hostingu, zasilony wygodą lokalnych testów z (B).
2. Dlaczego oba pliki muszą mieć identyczną zawartość?
   - (A) Rozjazd adresów tunelu powodowałby losowe błędy w fetch.
   - (B) Automatyczne testy mogą łatwo wykryć niespójność.
   - (C) Synchronizacja manualna jest prosta i szybka.
   **Decyzja:** A jako krytyczne bezpieczeństwo, z automatyczną kontrolą z (B).
3. Dlaczego warto dodać test do pilnowania duplikatu?
   - (A) Chroni przed zapomnieniem o aktualizacji jednego z plików.
   - (B) Buduje kulturę "konfiguracja jako kod".
   - (C) Ułatwia audyt CTO personie.
   **Decyzja:** A jako główny hamulec regresji, doprawiony audytem z (C).
4. Dlaczego test powinien sprawdzać format URL?
   - (A) Dzięki temu szybciej wyłapiemy przypadkowy brak protokołu.
   - (B) Zapewnia spójność z wymogiem tunelu HTTPS.
   - (C) Ułatwia tworzenie smoke testów CLI.
   **Decyzja:** B jako wymóg bezpieczeństwa, rozszerzony o ergonomię CLI z (C).
5. Dlaczego nadal utrzymujemy plik w `public/`?
   - (A) Repozytorium służy też do budowania statycznych assetów w przyszłości.
   - (B) Historyczne dokumenty i ADR-y odwołują się do tej lokalizacji.
   - (C) Umożliwia reużycie w alternatywnych bundlerach.
   **Decyzja:** B dla ciągłości dokumentacji, wzbogacone o elastyczność narzędzi z (C).

## 5xWhy — Custom domain i hosting
1. Dlaczego potrzebujemy własnej domeny na GitHub Pages?
   - (A) Buduje wiarygodność marki LARP poza kontekstem GitHub.
   - (B) Ułatwia promocję wydarzenia podczas kampanii marketingowych.
   - (C) Zapewnia pełną kontrolę nad certyfikatami TLS.
   **Decyzja:** A jako główne uzasadnienie, rozszerzone o łatwość promocji z (B).
2. Dlaczego rezygnujemy z przechowywania pliku `CNAME` w repozytorium?
   - (A) GitHub Pages może nadpisać plik przy konfiguracji domeny z UI.
   - (B) Ułatwia to zespołowi nietechnicznemu zarządzanie domeną bez konfliktów z Git history.
   - (C) Pozwala odciążyć agentów od ręcznego pilnowania formatu pliku.
   **Decyzja:** A jako kluczowe uzasadnienie, uzupełnione o dostępność dla nietechnicznych osób z (B).
3. Dlaczego automatyczny test `pytest` jest nadal potrzebny?
   - (A) Zapewnia natychmiastową informację o przypadkowym przywróceniu `CNAME`.
   - (B) Umożliwia audyt CTO persony bez manualnej kontroli każdej gałęzi.
   - (C) Uczy agentów respektowania zasad CI/CD.
   **Decyzja:** A wzbogacone o aspekt audytu z (B).
4. Dlaczego dokumentacja DNS musi być w README?
   - (A) To najczęściej odwiedzany dokument onboardingowy.
   - (B) Pozwala prowadzić warsztaty i przekazywać wiedzę organizatorom LARP.
   - (C) Redukuje powtarzające się pytania supportowe.
   **Decyzja:** C jako cel, z wykorzystaniem widoczności README z (A).
5. Dlaczego trzeba planować monitorowanie HTTPS?
   - (A) Certyfikaty odnawiają się automatycznie, ale warto wykrywać awarie.
   - (B) Zapewnia ciągłość dostępu do materiałów fabularnych.
   - (C) Przygotowuje repo na przyszłe integracje (np. status page).
   **Decyzja:** B jako główny powód, rozszerzony o przygotowanie integracji z (C).

## 5xWhy — Dlaczego nie trzymamy CNAME
1. Dlaczego przenosimy `CNAME` do ustawień GitHub Pages?
   - (A) Pozwala utrzymać spójność z automatycznymi commitami GitHuba.
   - (B) Ułatwia szybkie zmiany domeny bez oczekiwania na review PR.
   - (C) Minimalizuje konflikty merge przy wielu agentach.
   **Decyzja:** B jako najistotniejsze, rozszerzone o redukcję konfliktów z (C).
2. Dlaczego test powinien blokować dodanie `CNAME` do repo?
   - (A) Zapobiega przypadkowemu cofnięciu decyzji procesowej.
   - (B) Informuje zespół o konieczności pracy przez UI.
   - (C) Chroni pipeline przed niepotrzebnymi zmianami w branchu Pages.
   **Decyzja:** A wzmocnione komunikatem edukacyjnym z (B).
3. Dlaczego dokumentacja musi wyjaśniać brak pliku?
   - (A) Osoby nowe w repo mogą szukać pliku i zgłaszać błąd.
   - (B) Wspiera operatorów DNS podczas audytu.
   - (C) Buduje pamięć organizacyjną projektu.
   **Decyzja:** A jako główne, doprawione pamięcią organizacyjną z (C).
4. Dlaczego notatki zapisują decyzję formą 5xWhy?
   - (A) Pozwala szybko odtworzyć tok rozumowania CTO persony.
   - (B) Przygotowuje grunt pod ewentualną zmianę strategii domenowej.
   - (C) Łączy architekta i implementera wspólnym słownikiem.
   **Decyzja:** A jako fundament, rozszerzony o adaptacyjność z (B).
5. Dlaczego zadanie kontynuacyjne obejmuje monitorowanie ustawień Pages?
   - (A) UI GitHuba nie ma alertów o utracie wpisu domeny.
   - (B) Spójność z zadaniem HTTPS daje kompletny łańcuch E2E.
   - (C) Działa jako strażnik przed wprowadzeniem `CNAME` do repo.
   **Decyzja:** B jako główny cel, z wykorzystaniem ochrony przed cofnięciem decyzji z (C).

## 5xWhy — Dlaczego weryfikacja DNS GitHub Pages się nie powiodła
1. Dlaczego GitHub zgłosił błąd „Both www.larpkronikiognia.pl and its alternate name are improperly configured”? 
   - (A) Rekord `CNAME` wskazywał na nieistniejący host (`larpkronikiognia.github.io`).
   - (B) Rekordy `A` dla domeny głównej nie zostały ustawione.
   - (C) DNS nie zdążył się jeszcze propagować.
   **Decyzja:** A jako główny powód; dopełniamy konfigurację wskazując poprawnie na `pkr0kosz.github.io`, utrzymując świadomość propagacji z (C).
2. Dlaczego host docelowy musi być `pkr0kosz.github.io`?
   - (A) Repozytorium jest projektem pod profilem `pkr0kosz`.
   - (B) GitHub Pages mapuje certyfikaty TLS według nazwy użytkownika.
   - (C) Tylko tak zapisany rekord przejdzie automatyczny check w ustawieniach Pages.
   **Decyzja:** C jako krytyczne wymaganie, rozszerzone o świadomość zależności TLS z (B).
3. Dlaczego trzeba wspomnieć o domenie `.com`?
   - (A) Zespół rozważa wariant marketingowy `.com`.
   - (B) Konsolidacja domen ogranicza duplikację SEO.
   - (C) Łatwiej przetestować fallback w przypadku awarii `.pl`.
   **Decyzja:** B jako przewodni cel, wzbogacony o możliwość fallbacku z (C).
4. Dlaczego instrukcja powinna wskazywać testy `dig` dla obu domen?
   - (A) Ułatwia to debugging w razie ponownego błędu.
   - (B) Edukuje nietechniczne osoby w zakresie narzędzi CLI.
   - (C) Pozwala zapisać w pipeline jednoznaczne kryterium akceptacji.
   **Decyzja:** A jako kluczowa pomoc operacyjna, z edukacyjnym walorem (B).
5. Dlaczego uwzględniamy przekierowanie 301 `.com` → `.pl`?
   - (A) Zapewnia spójny canonical URL dla wyszukiwarek.
   - (B) Chroni uczestników przed trafieniem na nieaktualne treści.
   - (C) Upraszcza konfigurację certyfikatu Let's Encrypt na GitHubie.
   **Decyzja:** A jako główny efekt, ze wsparciem doświadczenia uczestników z (B).
   **Decyzja:** A jako wiodące, uzupełnione o audytowalność z (B).

# Notatki (Faza 3)
- Repozytorium rezygnuje z przechowywania pliku `CNAME`; konfiguracja domeny odbywa się ręcznie w ustawieniach GitHub Pages.
- Test `tests/test_custom_domain.py` pilnuje braku pliku `CNAME` i wymusza aktualność dokumentacji opisującej proces ustawiania domeny.
- README oraz ADR #0002 aktualizują instrukcję DNS, dodając przypomnienie o potwierdzaniu zmian w interfejsie Pages.
- Plan i tasks opisują nowe zadania: zabezpieczenie przed przypadkowym dodaniem `CNAME` oraz przyszłe monitorowanie certyfikatu HTTPS i statusu domeny.

## 5xWhy — Custom domain i hosting
1. Dlaczego potrzebujemy własnej domeny na GitHub Pages?
   - (A) Buduje wiarygodność marki LARP poza kontekstem GitHub.
   - (B) Ułatwia promocję wydarzenia podczas kampanii marketingowych.
   - (C) Zapewnia pełną kontrolę nad certyfikatami TLS.
   **Decyzja:** A jako główne uzasadnienie, rozszerzone o łatwość promocji z (B).
2. Dlaczego rezygnujemy z przechowywania pliku `CNAME` w repozytorium?
   - (A) GitHub Pages może nadpisać plik przy konfiguracji domeny z UI.
   - (B) Ułatwia to zespołowi nietechnicznemu zarządzanie domeną bez konfliktów z Git history.
   - (C) Pozwala odciążyć agentów od ręcznego pilnowania formatu pliku.
   **Decyzja:** A jako kluczowe uzasadnienie, uzupełnione o dostępność dla nietechnicznych osób z (B).
3. Dlaczego automatyczny test `pytest` jest nadal potrzebny?
   - (A) Zapewnia natychmiastową informację o przypadkowym przywróceniu `CNAME`.
   - (B) Umożliwia audyt CTO persony bez manualnej kontroli każdej gałęzi.
   - (C) Uczy agentów respektowania zasad CI/CD.
   **Decyzja:** A wzbogacone o aspekt audytu z (B).
4. Dlaczego dokumentacja DNS musi być w README?
   - (A) To najczęściej odwiedzany dokument onboardingowy.
   - (B) Pozwala prowadzić warsztaty i przekazywać wiedzę organizatorom LARP.
   - (C) Redukuje powtarzające się pytania supportowe.
   **Decyzja:** C jako cel, z wykorzystaniem widoczności README z (A).
5. Dlaczego trzeba planować monitorowanie HTTPS?
   - (A) Certyfikaty odnawiają się automatycznie, ale warto wykrywać awarie.
   - (B) Zapewnia ciągłość dostępu do materiałów fabularnych.
   - (C) Przygotowuje repo na przyszłe integracje (np. status page).
   **Decyzja:** B jako główny powód, rozszerzony o przygotowanie integracji z (C).

## 5xWhy — Dlaczego nie trzymamy CNAME
1. Dlaczego przenosimy `CNAME` do ustawień GitHub Pages?
   - (A) Pozwala utrzymać spójność z automatycznymi commitami GitHuba.
   - (B) Ułatwia szybkie zmiany domeny bez oczekiwania na review PR.
   - (C) Minimalizuje konflikty merge przy wielu agentach.
   **Decyzja:** B jako najistotniejsze, rozszerzone o redukcję konfliktów z (C).
2. Dlaczego test powinien blokować dodanie `CNAME` do repo?
   - (A) Zapobiega przypadkowemu cofnięciu decyzji procesowej.
   - (B) Informuje zespół o konieczności pracy przez UI.
   - (C) Chroni pipeline przed niepotrzebnymi zmianami w branchu Pages.
   **Decyzja:** A wzmocnione komunikatem edukacyjnym z (B).
3. Dlaczego dokumentacja musi wyjaśniać brak pliku?
   - (A) Osoby nowe w repo mogą szukać pliku i zgłaszać błąd.
   - (B) Wspiera operatorów DNS podczas audytu.
   - (C) Buduje pamięć organizacyjną projektu.
   **Decyzja:** A jako główne, doprawione pamięcią organizacyjną z (C).
4. Dlaczego notatki zapisują decyzję formą 5xWhy?
   - (A) Pozwala szybko odtworzyć tok rozumowania CTO persony.
   - (B) Przygotowuje grunt pod ewentualną zmianę strategii domenowej.
   - (C) Łączy architekta i implementera wspólnym słownikiem.
   **Decyzja:** A jako fundament, rozszerzony o adaptacyjność z (B).
5. Dlaczego zadanie kontynuacyjne obejmuje monitorowanie ustawień Pages?
   - (A) UI GitHuba nie ma alertów o utracie wpisu domeny.
   - (B) Spójność z zadaniem HTTPS daje kompletny łańcuch E2E.
   - (C) Działa jako strażnik przed wprowadzeniem `CNAME` do repo.
   **Decyzja:** B jako główny cel, z wykorzystaniem ochrony przed cofnięciem decyzji z (C).
5. Dlaczego pipeline potrzebuje dokumentacji zmian?
   - (A) Zapewnia kontekst dla przyszłych agentów.
   - (B) Ułatwia audyt CTO persony.
   - (C) Buduje pamięć projektową (CONTEXT).
   **Decyzja:** A jako wiodące, uzupełnione o audytowalność z (B).

# Notatki (Faza 4)
- Strona "Organizacja" zyskała przycisk "Oceń pomysł" przy każdym wątku, rozwijający panel komentarza z komunikatami statusu.
- Komentarze zapisują się w `localStorage`, co pozwala prowadzącym zachować uwagi między odświeżeniami strony podczas iteracji warsztatowych.
- Panel respektuje bursztynową paletę projektu i układ mobilny, a test `tests/test_feedback_panel.py` blokuje regresje markupowe i stylowe.

## 5xWhy — Panel ocen pomysłów
1. Dlaczego dodajemy panel oceny do kart wątków?
   - (A) By zebrać wrażenia w trakcie warsztatów planistycznych.
   - (B) By ocenić priorytety mechanik podczas testów wewnętrznych.
   - (C) By zapewnić notatnik prowadzących bezpośrednio na stronie.
   **Decyzja:** C jako baza funkcjonalności, rozszerzona o warsztatowy kontekst z (A).
2. Dlaczego zapis lokalny w `localStorage`?
   - (A) Nie wymaga backendu ani dodatkowej infrastruktury.
   - (B) Zapewnia natychmiastową synchronizację między wszystkimi uczestnikami.
   - (C) Pozwala działać offline podczas testów gry.
   **Decyzja:** A dla prostoty wdrożenia, z korzyścią pracy offline z (C).
3. Dlaczego panel domyślnie pozostaje zwinięty?
   - (A) Zachowuje czytelność i rytm kart nawet przy dużej liczbie wątków.
   - (B) Minimalizuje koszty renderowania w przeglądarce.
   - (C) Chroni przed przypadkową edycją tekstu przy przewijaniu.
   **Decyzja:** A jako priorytet UX, wzbogacony o ochronę przed przypadkowym dotykiem z (C).
4. Dlaczego potrzebujemy dedykowanych styli mobilnych?
   - (A) Użytkownicy często korzystają z telefonu podczas przygotowań LARP.
   - (B) Utrzymuje spójność wizualną w bursztynowej palecie repozytorium.
   - (C) Ułatwia szybkie testy QA w pipeline'ie.
   **Decyzja:** A jako kluczowe, z konsekwencją stylistyczną z (B).
5. Dlaczego nowy test Pytest jest wymagany?
   - (A) Chroni markup i klucze `localStorage` przed przypadkową regresją.
   - (B) Działa jako podstawa pod przyszłą synchronizację eksportu komentarzy.
   - (C) Zapewnia zgodność z wymaganiami CI i dokumentacją planu.
   **Decyzja:** A jako fundament, rozszerzone o dyscyplinę CI z (C).

## 5xWhy — Baner Notebook LM
1. Dlaczego dodajemy baner z odnośnikiem do Notebook LM?
   - (A) By użytkownicy szybko trafili do pełnej bazy wiedzy po burzy mózgów.
   - (B) By wzmocnić narrację repo o latającym zwiadowcy prowadzącym do wiedzy.
   - (C) By zebrać wszystkie zasoby w jednym miejscu dla przygotowania MVP.
   **Decyzja:** A jako priorytet, wzbogacony o element narracyjny z (B).
2. Dlaczego komunikat ma formę "flying object"?
   - (A) Podtrzymuje klimat mistycznego klasztoru ognia.
   - (B) Wyróżnia CTA na tle innych elementów strony.
   - (C) Pozwala rozbudować motyw przewodni na przyszłe interakcje.
   **Decyzja:** B jako klucz do widoczności, z klimatem z (A).
3. Dlaczego baner potrzebuje osobnego testu automatycznego?
   - (A) Gwarantuje stałą dostępność linku do knowledge base.
   - (B) Chroni atrybuty bezpieczeństwa (`rel`, `target`).
   - (C) Zapobiega przypadkowemu usunięciu narracyjnego komunikatu.
   **Decyzja:** A jako fundament, rozszerzony o wymagania bezpieczeństwa z (B).
4. Dlaczego animacja musi respektować `prefers-reduced-motion`?
   - (A) Dostępność to wymóg MVP.
   - (B) Minimalizuje ryzyko dyskomfortu użytkowników.
   - (C) Pozwala zachować płynność działania strony.
   **Decyzja:** A jako główna motywacja, z uwzględnieniem komfortu z (B).
5. Dlaczego planujemy kontynuację prac nad Notebook LM?
   - (A) Aby streścić kluczowe wnioski w samej witrynie.
   - (B) Aby zsynchronizować wiedzę z pipeline'em dokumentacyjnym.
   - (C) Aby przygotować kolejny test akceptacyjny dla integracji.
   **Decyzja:** B jako kierunek, z planem na streszczenie z (A).

## 5xWhy — Dlaczego wymuszamy `.nojekyll`
1. Dlaczego dodajemy plik `.nojekyll`?
   - (A) Aby GitHub Pages nie uruchamiał Jekylla, który ignoruje katalogi zaczynające się od `_`.
   - (B) Aby pipeline był kompatybilny z istniejącymi testami wykorzystującymi katalog `tests/` na froncie.
   - (C) Aby uniknąć konfliktów z własnym generatorem statycznym w przyszłości.
   **Decyzja:** A jako najpilniejsza potrzeba, wzmocniona świadomością kompatybilności z (B).
2. Dlaczego musimy utrzymywać dokumentację o `.nojekyll`?
   - (A) Nowi współtwórcy zrozumieją, że brak pliku to regresja w deployu.
   - (B) Dokumentacja służy jako checklist przy audytach CTO.
   - (C) README pomaga przy on-boardingu osób odpowiedzialnych za Pages.
   **Decyzja:** A jako główna ochrona, doprawiona aspektem onboardingu z (C).
3. Dlaczego potrzebny jest test automatyczny dla `.nojekyll`?
   - (A) Ręczna kontrola łatwo przeoczy brak pliku po refaktorach.
   - (B) Test może także sprawdzać, czy README tłumaczy decyzję.
   - (C) Włączenie do CI pozwala szybko reagować na regresje hostingowe.
   **Decyzja:** C jako strażnik CI, rozszerzony o dokumentacyjną kontrolę z (B).
4. Dlaczego test ma pilnować również wzmianki w README?
   - (A) Bez przypomnienia w dokumentacji decyzja mogłaby zostać cofnięta.
   - (B) README jest najczęściej czytanym plikiem przez utrzymanie.
   - (C) Chronimy spójność między wiedzą operacyjną a stanem repo.
   **Decyzja:** C jako wymóg spójności, uzupełniony o popularność README z (B).
5. Dlaczego planujemy dalszą automatyzację kontroli artefaktów Jekylla?
   - (A) GitHub może ponownie włączyć Jekylla przy zmianie ustawień projektu.
   - (B) Monitoring `/_site` wykryje przypadkowe wdrożenia generatora.
   - (C) Alert w pipeline pozwoli reagować zanim trafi to do produkcji.
   **Decyzja:** C jako główny cel operacyjny, wzbogacony o obserwację artefaktów z (B).

# Notatki (Faza 4)
- Strona główna otrzymuje formularz "Dodaj pomysł" z natychmiastowym feedbackiem i dostępnością `aria-live`.
- Backend Flask (`app.py`) utrwala zgłoszenia w SQLite i równoległym dzienniku tekstowym do dalszej kuracji narracji.
- Test `tests/test_idea_submission.py` pilnuje, że request kończy się kodem 201 i zapisuje dane w obu warstwach storage.

## 5xWhy — Rejestr pomysłów
1. Dlaczego potrzebujemy formularza "Dodaj pomysł"?
   - (A) Aby uczestnicy mogli szybko przekazać inspiracje bezpośrednio z witryny.
   - (B) By zebrać materiał do dalszej kuracji narracyjnej.
   - (C) By zademonstrować interaktywne MVP poza statycznym HTML.
   **Decyzja:** C jako sygnał MVP, wzmocniony o pozyskiwanie inspiracji z (A).
2. Dlaczego zapisujemy dane w bazie SQLite?
   - (A) Zapewnia transakcyjną trwałość i możliwość późniejszego raportowania.
   - (B) Ułatwia migrację do innych systemów danych.
   - (C) Umożliwia testom automatycznym walidację struktury danych.
   **Decyzja:** A jako fundament, uzupełniony o testowalność z (C).
3. Dlaczego równolegle tworzymy plik tekstowy?
   - (A) Kuratorzy narracji mogą szybko przejrzeć pomysły bez narzędzi SQL.
   - (B) Zapewnia backup w razie uszkodzenia bazy.
   - (C) Pozwala zasilić warsztaty fabularne wydrukiem.
   **Decyzja:** A jako główna wartość, rozszerzona o backup z (B).
4. Dlaczego formularz ma `aria-live` i jasny feedback?
   - (A) Dostępność to wymóg dla MVP.
   - (B) Minimalizuje frustrację użytkownika w razie błędów sieci.
   - (C) Ułatwia testy ręczne i automatyczne.
   **Decyzja:** A jako zobowiązanie dostępności, z komunikacją błędów z (B).
5. Dlaczego backend korzysta z Flask?
   - (A) Lekka integracja z istniejącym Pythonowym toolsetem repo.
   - (B) Zapewnia prosty testowy klient do `pytest`.
   - (C) Przygotowuje grunt pod ewentualną rozbudowę API.
   **Decyzja:** B dla kompatybilności testów, z elastycznością rozbudowy z (C).

## Raport agenta — Ambientowe tła
- **Co zostało zrobione:** Każda podstrona otrzymała trzywarstwowe, rozmyte tło z galerii zdjęć, które powoli przesuwa się horyzontalnie, utrzymując klimat płonącego klasztoru.
- **Dlaczego (z czego zrezygnowano):** Odłożono dynamiczne sterowanie prędkością w oparciu o scroll JS, aby zachować lekkość implementacji i kompatybilność z hostingiem statycznym.
- **Cel funkcji i stan pipeline'u:** Warstwa wizualna ma pogłębić immersję bez utraty dostępności; pipeline jest zabezpieczony nowym testem `tests/test_ambient_backgrounds.py`, a kontynuacją jest zaplanowanie sterowania ruchem w `docs/tasks.md`.
- **Spojrzenie na cel repo + kolejny krok ku MVP:** Repo zmierza ku pełnemu doświadczeniu LARP (wizualia + interakcje). Następny krok to dostosowanie prędkości tła do scrolla i przygotowanie narzędzi do dalszego rozszerzania ambientu.
