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

# Notatki (Faza 3)
- Dodano wspólny baner "flying object" prowadzący do Notebook LM z bazą wiedzy brainstormu; zachowuje klimat projektu dzięki animowanej ikonie zwiadowcy.
- Test `tests/test_notebook_banner.py` kontroluje link, atrybuty bezpieczeństwa oraz komunikat narracyjny.
- Baner respektuje preferencje ograniczonego ruchu i układ mobilny, dzięki czemu CTA pozostaje dostępne.

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
