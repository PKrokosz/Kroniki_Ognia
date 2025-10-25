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
- Dodano instrukcję weryfikacji domeny organizacji GitHub przez rekord TXT `_gh-SilesianGames-o.www.larpkronikiognia.pl` z wartością `6224e5ae12`, podkreślając 7-dniową ważność kodu i 72-godzinną propagację.

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

## 5xWhy — Weryfikacja domeny organizacji TXT
1. Dlaczego trzeba potwierdzić domenę organizacji GitHub rekordem TXT?
   - (A) Aby umożliwić wysyłkę maili transakcyjnych z własnej domeny.
   - (B) By zabezpieczyć markę przed podszywaniem się w ramach GitHub Pages.
   - (C) Żeby przygotować pod przyszłe integracje SSO.
   **Decyzja:** B jako krytyczne zabezpieczenie, wzbogacone o możliwość mailingu z (A).
2. Dlaczego używamy hosta `_gh-SilesianGames-o.www.larpkronikiognia.pl`?
   - (A) GitHub wymaga prefiksu `_gh-<org>-` dla weryfikacji domen organizacji.
   - (B) Dzięki temu nie kolidujemy z rekordem `CNAME` hosta `www`.
   - (C) Prefiks pozwala na równoległe rekordy testowe.
   **Decyzja:** A jako wymóg formalny, dopełniony o bezpieczeństwo `CNAME` z (B).
3. Dlaczego należy zapisać wartość `6224e5ae12` w dokumentacji?
   - (A) Ułatwia to operatorom DNS szybkie wdrożenie.
   - (B) Pozwala sprawdzić, czy kod nie wygasł po 7 dniach.
   - (C) Pomaga testerom E2E odtwarzać scenariusz.
   **Decyzja:** A jako główny cel operacyjny, rozszerzony o kontrolę ważności z (B).
4. Dlaczego trzeba wspomnieć o propagacji do 72 godzin?
   - (A) Rekordy TXT bywają cache'owane dłużej niż `CNAME`.
   - (B) Pozwala zaplanować okno publikacji bez presji.
   - (C) Informuje o konieczności wielokrotnego monitoringu.
   **Decyzja:** A jako najczęstszy problem, wzbogacony o planowanie z (B).
5. Dlaczego zalecamy monitorowanie `dig _gh-SilesianGames-o... TXT`?
   - (A) Zapewnia mierzalny checkpoint w pipeline.
   - (B) Edukuje zespół w zakresie narzędzi sieciowych.
   - (C) Ułatwia automatyzację przyszłych testów.
   **Decyzja:** A jako część pipeline'u, rozszerzona o potencjał automatyzacji z (C).
