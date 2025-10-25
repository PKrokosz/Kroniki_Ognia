# ADR 0003: Panel komentarzy wątków

## Status
Akceptowane — Faza 4 (listopad 2024)

## Kontekst
W sekcji "Organizacja" gromadzimy kilkadziesiąt pomysłów fabularnych i mechanicznych. Podczas warsztatów projektowych zespół potrzebuje miejsca na szybkie notatki przy każdym wątku bez opuszczania strony ani budowania backendu. Dotychczasowe karty nie miały możliwości zapisu lokalnych uwag ani śledzenia iteracji.

## Decyzja
- Dodajemy przycisk "Oceń pomysł" przy każdej karcie, rozwijający panel komentarza z polami formularza.
- Komentarze przechowujemy w `localStorage` z prefiksem `organizacja-feedback:<id wątku>`, aby przeglądarka utrzymała wpisy między odświeżeniami.
- Panel komunikuje status (zapisano, wyczyszczono, brak dostępu do pamięci) i pozostaje domyślnie zwinięty, by nie zasłaniać treści.
- Styl i układ komponentu są definiowane w `assets/styles.css`, respektując istniejącą paletę i media query <= 600px.
- Relewantne elementy są chronione testem `tests/test_feedback_panel.py`, który pilnuje markupów i styli.

## Konsekwencje
- Wersja offline warsztatów zyskuje szybki notatnik, ale komentarze nie synchronizują się między urządzeniami — kolejne zadanie obejmie eksport/import.
- Utrzymanie komponentu wymaga aktualizacji testów przy każdej zmianie markupów lub struktur kluczy.
- Dokumentacja (README, plan, tasks, notes) musi uwzględniać panel jako nowy element MVP.
