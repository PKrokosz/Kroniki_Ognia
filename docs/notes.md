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
- Dodano test `tests/test_custom_domain.py`, który pilnuje zawartości pliku `CNAME` oraz znaku nowej linii na końcu.
- Test został doprecyzowany tak, aby wymuszać dokładnie jedną linię `www.larpkronikiognia.pl` zakończoną `\n`, eliminując przypadkowe spacje.
- README zawiera procedurę konfiguracji DNS dla `www.larpkronikiognia.pl`, włącznie z adresami IP dla rekordu A i checklistą weryfikacji.
- Plan oraz tasks uzupełniono o fazę 3, a ADR odnotowuje decyzję o mapowaniu domeny na GitHub Pages.

## 5xWhy — Custom domain i hosting
1. Dlaczego potrzebujemy własnej domeny na GitHub Pages?
   - (A) Buduje wiarygodność marki LARP poza kontekstem GitHub.
   - (B) Ułatwia promocję wydarzenia podczas kampanii marketingowych.
   - (C) Zapewnia pełną kontrolę nad certyfikatami TLS.
   **Decyzja:** A jako główne uzasadnienie, rozszerzone o łatwość promocji z (B).
2. Dlaczego należy utrzymywać plik `CNAME` w repozytorium?
   - (A) GitHub automatycznie provisionuje certyfikat dla domeny.
   - (B) Chroni przed przypadkowym resetem ustawień Pages.
   - (C) Umożliwia testy regresyjne na CI.
   **Decyzja:** B jako priorytet, z dołączeniem testowalności z (C).
3. Dlaczego automatyczny test `pytest` jest potrzebny?
   - (A) Zapewnia natychmiastową informację zwrotną przy zmianach.
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

## 5xWhy — Format pliku CNAME
1. Dlaczego wymuszać pojedynczą linię w pliku `CNAME`?
   - (A) GitHub Pages odrzuca pliki z dodatkowymi spacjami, co blokuje deploy.
   - (B) Zmniejsza ryzyko konfliktów merge'owych, bo format jest przewidywalny.
   - (C) Ułatwia agentom manualną weryfikację w UI GitHuba.
   **Decyzja:** A jako krytyczne uzasadnienie, wzbogacone o przewidywalność z (B).
2. Dlaczego test powinien sprawdzać dokładny tekst zamiast `.strip()`?
   - (A) `.strip()` ukrywa błędy polegające na dodatkowych spacjach lub tabulatorach.
   - (B) Dzięki temu łatwiej przygotować fixture dla kolejnych testów DNS.
   - (C) Pozwala w przyszłości rozszerzyć walidację o inne domeny.
   **Decyzja:** A jako główny cel, uzupełniony o możliwość dalszej walidacji z (C).
3. Dlaczego dokumentacja powinna wspominać o `\n`?
   - (A) Edytory tekstowe potrafią usuwać ostatnią nową linię bez ostrzeżenia.
   - (B) Nowicjusze repo szybciej skojarzą problem z deployem.
   - (C) Ułatwia współpracę z zespołem infrastruktury.
   **Decyzja:** A z dopisanym aspektem edukacyjnym z (B).
4. Dlaczego warto odnotować regułę w `AGENTS.md`?
   - (A) Dokument kieruje przyszłych agentów i narzuca standard pracy.
   - (B) Zmniejsza liczbę rozbieżności między testami a oczekiwaniami.
   - (C) Ułatwia audyt procesowy CTO personie.
   **Decyzja:** A jako prymarny argument, rozszerzony o audytowalność z (C).
5. Dlaczego zadanie kontynuacyjne ma dotyczyć HTTPS?
   - (A) Zapewnia pełny end-to-end od DNS po certyfikat.
   - (B) Buduje na świeżo ustabilizowanym `CNAME`, wykorzystując te same testy.
   - (C) Daje wartość organizatorom planującym kampanie promocyjne.
   **Decyzja:** A jako kierunek do MVP, z dodaniem reużywalności testów z (B).
