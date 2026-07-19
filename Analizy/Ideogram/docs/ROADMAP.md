# ROADMAP — plan fazowy (integracja silnika generatywnego)

## Faza 0 — Fundament (1–2 tyg.)
- Wybór dostawcy modeli (self-host GPU vs API zewn.), rejestr modeli.
- Kolejka + storage + pgvector, licznik kredytów.
- Decyzja o przewadze (advisor+generacja+druk jako całość).

## Faza 1 — MVP silnika (4–6 tyg.)
- Generacja z promptu: model bazowy, proporcje, liczba obrazów, seed.
- Prompt enhancement (własny "magic prompt") z podglądem finalnego promptu.
- Biblioteka (moje obrazy), like, download.
- Upscale (pod druk).

## Faza 2 — Społeczność + edycja (4–6 tyg.)
- Explore (feed, kategorie, search, similaritySearch).
- Remix, follow, kolekcje.
- Remove BG, layerize text, edit/inpaint.

## Faza 3 — Integracja z produktem (6–8 tyg.)
- Wpięcie advisora (Fy!) → generacja → kompozycja ściany.
- Pipeline Mixtiles: rama/rozmiar/efekt + wizualizacja + checkout.
- Wysoka rozdzielczość → druk wielkoformatowy.

## Faza 4 — Custom modele + skalowanie (ciągłe)
- Training custom modeli (styl marki/klienta).
- Publiczne API + dashboard.
- Optymalizacja kosztów GPU, moderacja, licencje.

## Metryki
- Koszt generacji/druku na zamówienie vs wartość koszyka.
- Konwersja: generacja → ściana → zakup.
- Zaangażowanie społeczności (remix rate, follows).
