# ROADMAP — Displate jako filar wall-art 2026

Roadmapa wdrożenia wzorców z Displate do naszego produktu. Ujęcie fazowe: od
fundamentu commerce, przez różnicowanie, po skalowanie marketplace. Displate to
głównie filar **produktu fizycznego + marketplace + mechanik sprzedaży**.

> Zakres: wzorce i architektura, nie kopiowanie treści/IP/brandingu Displate.

## Faza 0 — Fundament (0–4 tyg.)
- Zdefiniować model produktu fizycznego: typy podłoża/wykończenia, rozmiary,
  warianty wieloelementowe, oprawy/ramy.
- Product Configurator MVP: wybór wariantu + żywy przelicznik ceny.
- Model danych produktu i wariantów (patrz DATA-MODEL.md).
- Zgodność cenowa: logika „najniższej ceny z 30 dni" (Omnibus) po stronie backendu.

## Faza 1 — Commerce Core (4–8 tyg.)
- Koszyk + checkout + rabaty ilościowe („taniej od 2 szt.").
- Promocje i odliczanie (poprawne liczenie, nie tylko UI).
- Trust Layer: recenzje, oceny, oznaczenia jakości/pochodzenia treści.
- Analityka zdarzeń commerce (view_item / add_to_cart / purchase) — własna warstwa,
  prywatna, bez wycieku danych wrażliwych.

## Faza 2 — Konwersja i podgląd (8–14 tyg.)
- Integracja z Wall Preview Engine (Mixtiles) — dzieło na ścianie na PDP.
- Integracja z Advisorem (Fy!) — rekomendacja prowadząca do gotowego wariantu.
- Eksploracja katalogu: filtry po kategorii/temacie, „bestselling", szybki podgląd
  wariantów z karty produktu.
- Optymalizacja PDP pod mobile (konfigurator jako główny element).

## Faza 3 — Różnicowanie treścią (14–22 tyg.)
- Generation Service (Ideogram) jako źródło unikatowych grafik → produkt custom.
- Zarządzanie prawami do treści wygenerowanej (licencja, atrybucja, użycie komercyjne).
- „Custom" ścieżka: własna grafika → konfigurator → produkt fizyczny.

## Faza 4 — Marketplace twórców (22–34 tyg.)
- Onboarding i profile twórców, weryfikacja („Verified Creator").
- Model payout / podziału przychodu, panel twórcy.
- Kuratorowanie i kolekcje tematyczne (własne, bez licencjonowanego IP).
- Pętla podaży: twórcy + AI stale zasilają katalog, który zasila Advisora.

## Faza 5 — Skalowanie i operacje (34+ tyg.)
- Pilotaż fulfillmentu (druk/oprawa) z jednym dostawcą → potem multi-vendor.
- Rozszerzenie wariantów (nowe rozmiary, wykończenia, oprawy premium).
- Programy lojalnościowe / subskrypcja (odpowiednik „Club" — własna mechanika).
- Ekspansja rynkowa: waluty, lokalizacja, zgodność cenowa per rynek.

## Kamienie milowe (definicja „gotowe")
- **M1**: Konfigurator + Commerce Core → pierwsza sprzedaż wariantu premium.
- **M2**: Advisor + Wall Preview podnoszą konwersję na istniejącym katalogu.
- **M3**: Generacja AI → produkt custom z uregulowanymi prawami.
- **M4**: Marketplace twórców z payoutem → samonapędzająca się podaż treści.

## Ryzyka roadmapy
- Fulfillment fizyczny to najtrudniejszy operacyjnie element — nie skalować przed
  pilotażem jakościowym.
- Prawa do treści (AI + twórcy) muszą być uregulowane zanim ruszy sprzedaż custom.
- Nadmiar funkcji naraz — trzymać Advisora jako warstwę upraszczającą wybór.
