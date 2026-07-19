# Przepływy UX i komponenty

> Dokument inspirowany analizą Fy! Art Advisor. Nie odwzorowuje 1:1 ich UI/treści — opisuje własne, docelowe przepływy naszego produktu.

## Mapa wysokopoziomowa
```
[RoomEntry] → [QuizPanel LUB Brief tekstowy] → [Generowanie kuracji]
→ [SpaceView: 3 kuracje] → { WallVisualizer | Chat | ForYouStrip }
→ [Zapis ściany / Udostępnienie / Koszyk]
```

## Ekrany i stany

### 1. RoomEntry (wejście)

Hasło + dwie ścieżki: pole tekstowe "Opisz przestrzeń..." ORAZ przyciski quizu.

Opcjonalny upload zdjęcia pokoju (drugoplanowy w MVP, pierwszoplanowy w v1).

CTA: "Skomponuj ścianę".

### 2. QuizPanel (opcjonalny brief)

Pytania (rozszerzone względem konkurencji):

- **Rozmiar ściany:** mała / średnia / duża / bardzo duża (galeryjna).
- **Kompozycja / liczba prac:** pojedynczy statement piece / dyptyk / tryptyk / ściana galeryjna (5+).
- **Nastrój i paleta:** chłodny i spokojny / ciepły i przytulny / odważny i kontrastowy / minimalistyczny / botaniczny.
- **Pokój / kontekst (opcjonalne):** salon / sypialnia / biuro / przedpokój / jadalnia.
- **Styl (opcjonalne):** abstrakcja / fotografia / ilustracja / typografia / vintage.

Zasady: wizualne karty (nie suchy select), pola opcjonalne pomijalne, stan trzymany w sesji (odzyskiwalny po odświeżeniu), CTA aktywne po minimum wymaganych odpowiedziach.

### 3. Loading / Generacja

Loader z komunikatem procesu ("Dobieram prace pod Twój nastrój…") — buduje zaufanie, że system pracuje. Fallback po timeoucie: pokaż rekomendacje "For You" zamiast pustego stanu.

### 4. SpaceView (widok przestrzeni)

Zwykle **3 nazwane kuracje** (tematyczne), każda z zestawem prac i krótkim uzasadnieniem doboru. Elementy:

- **WallVisualizer** — prace osadzone w wizualizacji ściany/ramy (flagowa funkcja emocjonalna).
- **Przełącznik notatek o pracach** ("dlaczego ta praca").
- **"Ustaw jako moja ściana"** — zapis wyboru.
- **"Udostępnij ścianę"** — link do współdzielenia (+ obraz OG do social).
- **ForYouStrip** — dynamiczne rekomendacje, odświeżane po każdej interakcji (uwzględnia wishlist/kontekst sesji).

### 5. Chat (doprecyzowanie)

Iteracja bez restartu quizu. Przykład: "więcej zieleni, mniej abstrakcji" → agent aktualizuje kurację + wizualizację + odświeża For You. Konwersacja zawsze kończy się KONKRETNYM outputem (nowe prace na ścianie), nie samą odpowiedzią tekstową.

### 6. Konwersja

Z każdej pracy: szybkie dodanie do koszyka / wishlisty. Zapis ściany jako trwały, udostępnialny artefakt (powód powrotu + kanał wirusowy).

## Dwie ścieżki wejścia (kluczowa decyzja UX)

- **Ścieżka A — Quiz strukturalny:** niski próg, dla niezdecydowanych.
- **Ścieżka B — Brief w języku naturalnym:** agent LLM ekstrahuje encje (pokój, paleta, nastrój, format).

Kandydat na przewagę (nie zdecydowane): płynne łączenie obu z pamięcią międzyetapową (quiz jako podpowiedź, brief jako override).

## Stany brzegowe

- Zbyt wąski brief / brak wyników → agent proponuje rozszerzenie ("pokazać cieplejsze warianty?").
- Błąd generacji → retry + fallback na "For You".
- Wygasła sesja (obserwowany 404 na starym Space) → czysty restart z zachowanym briefem, jeśli to możliwe.

## Punkty przewagi do rozważenia (otwarte)

- Wizualizacja we WŁASNYM zdjęciu wnętrza użytkownika (upload + inpainting).
- Transparentne "dlaczego" (wyjaśnialność doboru) jako element zaufania.
- Lepsza jakość/szybkość kuracji niż benchmark.
