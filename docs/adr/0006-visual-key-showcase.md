# ADR 0006 — Sekcja visual key „Próby Płomienia”

## Status
Zaakceptowano — Faza 2

## Kontekst
Landing kończył się dotąd na kartach tekstowych i formularzu „Dodaj pomysł”. Brakowało warstwy wizualnej, która w kilku krokach odda klimat klasztoru i przeprowadzi odbiorcę przez kluczowe podstrony. Repozytorium dysponuje dziewięcioma zdjęciami w katalogu `img/`, już wykorzystywanymi w ambientowych tłach. Potrzebowaliśmy modułu, który bez powielania zasobów pokaże te fotografie w sposób czytelny, zgodny z narracją i dostępnością.

## Decyzja
- Landing otrzymuje sekcję `<section class="content-section visual-key">` z trzema kafelkami (`visual-key__tile--ember`, `--glow`, `--flame`) reprezentującymi progi Iskra → Żar → Płomień.
- Każdy kafelek wykorzystuje istniejące zdjęcia `img/1.jpg`, `img/4.jpg`, `img/7.jpg`, zawiera opis w duchu repo oraz CTA do odpowiadającej podstrony (`cechy.html`, `imersja_mechanika.html`, `draft_planu.html`).
- Nowe style w `assets/styles.css` zapewniają spójny, bursztynowy wygląd, efekt podświetlenia aktywnego kafelka oraz responsywność < 720 px.
- Skrypt `assets/visual-key.js` obsługuje interakcje (hover/focus, aria-current) oraz opcjonalne autoodtwarzanie sterowane przyciskiem `data-visual-key-autoplay`, które szanuje `prefers-reduced-motion` i ogłasza status przez `aria-live`.
- Test `tests/test_visual_key.py` pilnuje struktury sekcji, obrazów, linków oraz obecności przycisku i statusu.

## Konsekwencje
- Landing zyskał wizualną narrację, która natychmiast przywołuje klimat projektu przed formularzem zgłoszeń.
- Dokumentacja (`README.md`, `docs/notes.md`, `docs/tasks.md`) opisuje moduł i kryteria akceptacji, a `AGENTS.md` utrwala standard trzech kafelków i powiązań.
- Przyszłe rozszerzenia (np. więcej progów, alternatywne galerie) wymagają aktualizacji skryptu, styli oraz testu regresyjnego — zadanie kontynuacyjne trafi do backlogu, jeśli pojawi się taka potrzeba.
- Autoodtwarzanie jest kontrolowane przez użytkownika; w środowiskach z ograniczonym ruchem pozostaje nieaktywne, co minimalizuje ryzyko dyskomfortu i wspiera zgodność z dostępnością.
