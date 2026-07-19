# Latenca — mapa rynku sztuki i druku

> Stan na 2026-07-16. Skrót z badań (kilka rund deep-research + weryfikacja bezpośrednia).
> Pełna klikalna wersja: [`market-map.html`](market-map.html) — otwórz w przeglądarce.
> Zasada: ZWERYFIKOWANE = z oficjalnego regulaminu/API platformy. Reszta = zgłoszone/założone.

---

## Sześć kategorii graczy

| Kategoria | Definicja | Przykłady |
|---|---|---|
| **Otwarty POD marketplace** | każdy artysta wgrywa, niski royalty | Redbubble, Society6, Displate, Fine Art America, INPRNT, Zazzle |
| **Kurowane sklepy plakatowe** | marka kontroluje katalog i ceny | **Desenio**, Poster Store, JUNIQE, King & McGaw, Fy! |
| **Marketplace sztuki** | bramkowane, wysoka prowizja | Saatchi Art, Artsy, Artfinder, Singulart, Rise Art |
| **Foto-na-ścianę** | Twoje zdjęcie staje się produktem | **Mixtiles**, CanvasPop, Shutterfly, Artifact Uprising |
| **Platformy AI-art** | generatory z opcją druku/sprzedaży | Ideogram, NightCafe, Midjourney, Etsy AI-shops, Desenio Imaginator |
| **Prezenty POD** | portret/prezent ze zdjęcia | Crown & Paw, Printful, Printify |

Najbliższe analogi dla Latenca: **Desenio** (kurowana marka + gallery walls), **Mixtiles** (AI-personalizacja na skalę), **andyokay** (kurowana marka charytatywna).

---

## Ekonomia artystów (ZWERYFIKOWANE z regulaminów)

Kluczowy wzorzec: **na żadnej platformie druku artysta nie kontroluje ceny detalicznej** (poza Artfinder — ale tam i tak wymuszają przeceny).

| Platforma | Zarobek artysty | Kto ustala cenę | Uwagi |
|---|---|---|---|
| **Society6** | 5–10% netto (od 2025-03-18) | platforma | odebrali kontrolę narzutu; ma ludzką kuratelę |
| **Displate** | stała kwota $4,50/$9/$14,50 od sztuki | platforma | wypłata $50, tylko PayPal, przepada po 3 latach; bramka to automat, nie kuratela; **żadnej polityki AI**, żadnej klauzuli licencyjnej |
| **Redbubble** | % narzutu na cenie bazowej | platforma (baza) | ich wyprzedaże po cichu tną zarobek; próg wypłat $20→$10 od 2026-07-01 |
| **Saatchi Art** | 60% (40% prowizji) | artysta | jednostronne przeceny bez prawa odmowy |
| **Artfinder** | 55–60% (45%/40% prowizji) | **artysta** | ale: *„we are unable to offer an opt out"* przy przecenach |

**Gelato i Prodigi** = czysta hurtownia, zero prowizji, Ty ustalasz cenę. Marża = cena − druk − wysyłka − prowizja płatnicza − **VAT** (4. pozycja, którą pomijają w marketingu; istotna dla firmy z PL).

---

## Polityka AI per platforma (ZWERYFIKOWANE z ich stron)

| Platforma | Polityka AI |
|---|---|
| Etsy | POZWALA z obowiązkiem oznaczenia |
| Zazzle | POZWALA (tag „generativecontent", miękki) |
| Adobe Stock | POZWALA (obowiązkowy checkbox + ograniczenia promptów) |
| Society6 | OGRANICZA (wymaga ludzkiego wkładu) |
| Displate | **NIC nie publikuje** (przeszukano cały regulamin) |
| Shutterstock | **ZAKAZ** (jedyny; powód: nie może zweryfikować źródła modelu) |

**Wniosek:** artyści AI NIE są wypychani z rynku. Teza „nie mają gdzie pójść" jest fałszywa.

---

## Prawo autorskie (USA) — twarde ograniczenie

Grafika z samego promptu **nie ma ochrony prawnej** (US Copyright Office 2025; Sąd Najwyższy odmówił kasacji w Thaler v. Perlmutter, 2026-03-02). Katalogu „wpisz prompt → sprzedaj" nie da się obronić jako wyłącznej własności — potrzeba realnej pracy człowieka przy każdej pracy. (Dotyczy prawa USA; UE osobno, niezbadane.)

---

## Ceny rynkowe (obserwowane, do kalibracji własnych)

- **Desenio** (bestsellery, US): $17,97 / $23,40 / $27,57 / $29,95 / $45,95 / $55,95 — typowo $18–45 po stałym rabacie ~40%. 606 gallery walls, 108k recenzji, darmowa wysyłka >$69.
- **andyokay**: ~$44 (medium) / $59 (large), zakotwiczone od $140/$190, „82% off for charity". ~200 prac → 213k sprzedaży. Shopify. Start z gotową publicznością.
- **Etsy pliki cyfrowe**: $3–12 typowo; bundle **150 000+ grafik za $1,72**. To jest cena „wielkiego katalogu AI" w 2026.
