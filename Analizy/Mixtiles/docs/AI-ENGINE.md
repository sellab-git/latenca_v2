# AI-ENGINE — generatory i rekomendacje

## 1. Photo-to-Art (generator stylizowany)
Obserwacja Mixtiles: użytkownik wybiera MOTYW (np. "The Photoshoot", "High Society", "Pet Anatomy"), wgrywa zdjęcie, AI zwraca stylizowane warianty osadzone na ścianie.

### Architektura (rekomendacja)
- **Themes** = szablony promptów + parametry stylu (nie pokazywać użytkownikowi surowego promptu).
- Pipeline: upload → preprocessing (detekcja obiektu/twarzy, kadrowanie, upscale) → generacja (model image-to-image / dyfuzyjny z warunkowaniem na zdjęciu) → post (osadzenie w mockupie ramy/ściany) → warianty do wyboru.
- Asynchronicznie: kolejka + status jobu.
- Kontrola jakości: filtr NSFW, sprawdzenie podobieństwa do inputu, retry.

### Kategorie motywów (jak Mixtiles, ale własne treści)
PET, FAMILY, KIDS, PLACES — każda z zestawem własnych, oryginalnych stylów.

## 2. Wizualizacja na ścianie
- MVP: kompozycja 2.5D (osadzenie w gotowych mockupach wnętrz/ram).
- v2: inpainting w zdjęciu wnętrza użytkownika (upload własnej ściany) — przewaga UX.

## 3. Advisor / rekomendacje (most do Fy!)
- Ekstrakcja encji z briefu (pokój, paleta, nastrój) + quiz.
- Dopasowanie prac z katalogu przez embeddingi (pgvector) + tagi.
- Generowanie nazwanych kuracji z uzasadnieniem ("dlaczego ta praca").
- Rekomendacje "For You" po interakcjach (kontekst sesji, wishlist).

## 4. Zasady
- Prompty/motywy po stronie serwera, wersjonowane.
- Koszty AI: cache embeddingów, batch, tańsze modele do rutyny, drogie do finalnego renderu.
- Wyjaśnialność doboru jako element zaufania.
