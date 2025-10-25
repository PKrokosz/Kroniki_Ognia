# Notatki (Faza 1)
- Repo zawiera trzy główne dokumenty HTML z bogatą treścią narracyjną.
- Brak wspólnego stylu i nawigacji — konieczna centralizacja w `assets/styles.css`.
- Do dodania `index.html` jako landing page dla GitHub Pages.
- Należy utrzymać oryginalne teksty bez zmian merytorycznych.
- Nowa nawigacja została wdrożona wraz z testem `tests/test_navigation.py`; wszystkie strony korzystają z identycznego nagłówka.

# Notatki (Faza 2)
- Paleta barw została przygaszona wokół barw ziemistych, dodano ambientową warstwę tła i animację pulsującą, zachowując czytelność tekstów.
- Nawigacja na urządzeniach mobilnych przechodzi w układ kolumnowy, a karty otrzymują mniejsze paddingi, co poprawia ergonomię.
- Powstał zestaw testów `tests/test_responsive_theme.py` weryfikujących zarówno bloki @media, jak i obecność efektów graficznych.
- Wdrożono wielowarstwowe, rozmyte tła z zasobów `img/` — trzy obrazy na podstronę płynnie przesuwają się horyzontalnie i respektują `prefers-reduced-motion`.

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

# Notatki (Faza 3)
- Dodano wspólny baner "flying object" prowadzący do Notebook LM z bazą wiedzy brainstormu; zachowuje klimat projektu dzięki animowanej ikonie zwiadowcy.
- Test `tests/test_notebook_banner.py` kontroluje link, atrybuty bezpieczeństwa oraz komunikat narracyjny.
- Baner respektuje preferencje ograniczonego ruchu i układ mobilny, dzięki czemu CTA pozostaje dostępne.
- Baner uzupełniono o CTA do archiwum Google Drive z zasobami wspierającymi produkcję; kolorowa ikona sygnalizuje, że chodzi o repozytorium plików wizualnych.

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
