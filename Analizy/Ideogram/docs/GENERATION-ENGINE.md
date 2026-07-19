# GENERATION-ENGINE — silnik generatywny (wzorce Ideogram)

## Modele
- Wiele wersji: 4.0 (latest, 2K, najwyższa jakość), 3.0, Legacy.
- Tryb **Auto** — system dobiera model do zadania.
- **Custom models** — użytkownik trenuje własny styl/tożsamość.

## Magic Prompt
- Automatyczne wzbogacenie krótkiego promptu użytkownika w rozbudowany, opisowy prompt (obserwowane: bardzo długie, "malarskie" opisy).
- W UI dostępne jako osobna zakładka obok oryginalnego promptu → transparentność (użytkownik widzi, co model faktycznie dostał).

## Parametry generacji (obserwowane w metadanych)
- Model / wersja (np. Ideogram 4.0).
- Aspect ratio (np. 1:3) i Resolution (np. 1024×3072).
- Rendering / Speed (np. Turbo) — kompromis jakość/koszt/czas.
- Seed (np. 2093396245) — powtarzalność.
- Liczba obrazów w partii (np. 4).

## Rekomendacje dla NAS
- Warstwa "prompt enhancement" (własny odpowiednik Magic Prompt) z pokazaniem finalnego promptu.
- Zawsze zapisywać seed + parametry → remix i powtarzalność.
- Wiele profili jakości (szybki/tani vs wolny/wysoka jakość) sterowanych kredytami.
- Custom modele jako funkcja premium (styl marki/klienta).
- Kolejka asynchroniczna (generacja to długie zadanie): submit → status → wyniki.
- Moderacja treści (NSFW/znaki towarowe) przed publikacją do feedu.
