# Latenca — Specyfikacja (scalona, dokument roboczy)

> **Ten dokument łączy dwa wcześniejsze projekty w jeden kierunek.**
> - Z **projektu 15** (dojrzały prototyp): rzemiosło — model danych, formuła cenowa, filozofia szwów, myślenie mobile-first o przepływie, customizacja „na szynach".
> - Z **projektu 17** (kanoniczne repo `sellab-git/latenca`): strategia — koncept **AI-doradcy**, „projekt ściany" jako rdzeń, źródło katalogu (muzealne CC0 + AI), marketplace twórców odłożony.
>
> **Zasada rozstrzygania konfliktów:** gdzie 15 i 17 się kłócą → **wygrywa strategia z 17**; 15 dostarcza wykonanie.
> Status: pre-build, faza **mockupów HTML mobile-first** (Next.js dopiero później). Ostatnia aktualizacja: 2026-07-19.
> Kod/pola po angielsku; reszta po polsku.

---

## 0. Legenda
- ✅ **DECYZJA** — ustalone
- 🔬 **ZWERYFIKOWANE** — potwierdzone researchem/źródłem (patrz MARKET.md, COSTS.md, DECISIONS.md)
- 🟡 **DO DECYZJI** — otwarte
- ⛔ **NIE TERAZ** — świadomie odłożone

---

## 1. Czym jest Latenca

✅ **Kurowana marka pomagająca pewnie wybrać i ułożyć sztukę na ścianę.** Nie „sklep ze sztuką", nie „druk zdjęć", nie generator. Sprzedajemy **pewność decyzji**, nie same grafiki. Rdzeń = **ściana / zestaw**, nie pojedyncze dzieło.

Dwa wcześniejsze projekty opisywały to samo z dwóch stron i **teraz się schodzą**:
- 17 nazwał to „AI Wall Designer" — **doradca prowadzi** klienta krokami do dobrej decyzji.
- 15 nazwał to „builder ściany" — **prowadzony przepływ** (step-flow), z którego powstaje zestaw.

**To jest jedno.** Doradca AI to inteligentna warstwa na prowadzonym przepływie; przepływ produkuje ścianę. Na telefonie to **kolejne ekrany decyzyjne**, nie płótno do przeciągania (obie strony do tego doszły niezależnie — 15 §1b i 17 mockupy).

✅ **Kuracja to fosa.** W świecie zalanym grafiką AI jedyne, co przeżywa, to kurowany gust + spójne zestawy — czego marketplace skopiować nie może (🔬 zwycięzcy kategorii to kurowane marki: Mixtiles, Displate; otwarte — Society6, Redbubble — umierają). AI jest **źródłem**, nigdy tożsamością.

---

## 2. Dwie ścieżki, jeden cel

| | Doradca AI (drzwi dla niepewnych) | Przeglądanie (drzwi dla pewnych) |
|---|---|---|
| Z projektu | 17 | 15 |
| Wejście | rozmowa/kroki: pokój → styl → rozmiar | katalog + wyszukiwarka + kolekcje |
| Cel wspólny | **gotowa ściana** (zestaw prac) → produkt → koszyk | |

**Klucz spójności:** obie ścieżki lądują w tym samym miejscu — w **ścianie/zestawie**. To czyni z tego jeden produkt, nie dwa zszyte.

🟡 **Otwarte (Faza 2 — mapa ekranów):** czy „ściana" na mobile to ekran-wynik z lekką korektą (rekomendacja doradcy), czy prosty edytor slotów. **Builder z 15 = próba, NIE wzorujemy się na nim — projektujemy od zera pod doradcę i flow zakupu** (decyzja Artura 2026-07-19). Lean: ekrany decyzyjne + prezentowany wynik, nie ręczne komponowanie.

---

## 3. Zakres v1 vs odłożone

**W v1:**
- Dwie ścieżki (doradca + przeglądanie) → ściana → produkt → koszyk
- Katalog kurowany (źródło: sekcja 4), **atrybucja artysty** (przeglądaj po autorze)
- Kolekcje = **gotowe ściany** (merchandising zestawów, jak „gallery walls" Desenio)
- Customizacja „na szynach", warstwy nie-AI (sekcja 7)
- Sprzedaż: druk POD (Gelato) + plik cyfrowy; **zestawy = silnik koszyka**

**⛔ Odłożone (świadomie):**
- **Marketplace/upload twórców** (17 D-011 → faza 2). Artysta jako atrybucja zostaje; otwarty upload nie.
- **Canvas-builder** (ręczne przeciąganie) — zły wzorzec mobilny.
- **Generatywna warstwa AI dla klienta** (podmiana tematu / „Twój pupil") — silnik #2.
- **Prawdziwa logika rozmowy AI** — w mockupach udajemy ją ekranami.
- **Backend** (Supabase/Stripe/Gelato) — Faza 4, dopiero po zamknięciu flow.

---

## 4. Skąd bierze się sztuka (17 rządzi)

✅ **Katalog źródłowo-agnostyczny** (każde dzieło ma `source` + `collection`). v1 wypełniony z:
1. **Muzealne public-domain (CC0)** — legalne do sprzedaży, darmowe, **w rozdzielczości do dużego druku** (rozwiązuje naraz prawo autorskie I rozdzielczość, których czysty AI nie ma). Proof: `reference/catalog-demo-17/`. 🔬 17 D-011.
2. **AI kurowane przez operatora** — grafika AI, którą operator sam generuje/wybiera (nie generacja przez klienta).

**Artysta:**
- **Teraz (a):** atrybucja edytorska — prace mają podpisanego autora, można przeglądać po nim. Bez otwartego uploadu.
- **Docelowo (b):** marketplace twórców z drabiną zaufania (15 §2) — faza 2. **Szew w modelu danych stawiamy już teraz** (tani), żeby (b) było wpuszczaniem, nie przepisywaniem.

---

## 5. Model danych (15 rządzi — to jest przemyślane)

> Zasada: **grafika ≠ produkt do kupienia ≠ zamówienie.** Jedyna dyscyplina, którą trzeba zrobić dobrze od dnia 1 (retrofit = przepisanie całości).

Byty (z 15 §3, zachowane):
- **ARTIST** — konto, `trust_tier`, `revenue_share%`, dane wypłat. Pełny byt od początku (nawet gdy v1 = tylko atrybucja: operator = pierwszy artysta).
- **ARTWORK** — sama grafika: `source`, `source_image` (master hi-res), tagi, `artist_id`, `allowed_tones[]/allowed_crops[]/allow_text`. Bez ceny.
- **DERIVATIVE** — wariant WYGLĄDU (tonacja/kadr/układ-tekstu), przepis nie plik, `root_artist_id` zawsze płaci. ~24/dzieło, indeksowany do wyszukiwania.
- **PRODUCT/VARIANT** — SKU (oś przedmiotu): `(artwork|derivative) × {size, material, mat, frame, FILE|PRINT}` + cena z wzoru. Wirtualny, liczony przy wyborze.
- **SET/WALL** — pakietuje N prac, sprzedaje jako jeden produkt. **Centralny obiekt** (= „wall project" z 17).
- **ORDER + ORDER_LINE** — przy zakupie zamrażamy kopię (tytuł, konfiguracja, cena).
- **PAYOUT, MODERATION_REVIEW** — gotowe pod fazę 2.

⚠️ DERIVATIVE (oś wyglądu, widoczny) ≠ VARIANT (oś przedmiotu, wirtualny). Nie mylić.

---

## 6. Cennik (15 formuła + COSTS.md realne liczby)

**Formuła gross-up** (jedna dla druku i pliku):
```
Cena netto = (koszt_Gelato + koszty_stałe) ÷ (1 − nasza_marża% − %_artysty − prowizja%)
```
Trzy zabezpieczenia: limit % artysty (~40%), podłoga marży, % artysty od NETTO (przed VAT).

**Realne koszty Gelato są już znane** (nie „za loginem" jak w 15 — pobrane z API, patrz [`COSTS.md`](COSTS.md)):
- Druk 50×70: €17,79 (PL) / $12,49 (US). Wysyłka kolejnej sztuki w paczce: **~€0,29** → zestawy to cały biznes.
- **USA ≈ 2× marża Europy** (tańszy druk + brak unijnego VAT przy eksporcie).
- Duży format bije mały; małe formaty (30×40) w EU to pułapka.

🟡 Do decyzji (COSTS.md + sekcja 11): nasza marża %, podłoga, cel rynkowy (USA?), papier.

---

## 7. Customizacja „na szynach" (15 §1c, przycięte do v1)

Wchodzisz od arcydzieła, nie od pustej kartki. Ograniczone warstwy, które **zawsze dają dobry efekt** (szit nie ma jak powstać — nie ma takiej opcji w UI). Większość warstw **nie potrzebuje AI** (obróbka obrazu/typografia — zero kosztu, zero ryzyka prawnego).

| Warstwa | Tech | v1? |
|---|---|---|
| Tonacja, kadr, format, rozmiar, oprawa, zestaw | obróbka obrazu | ✅ (do potwierdzenia zestaw) |
| Napis/treść | typografia (kurowane fonty/miejsca) | 🟡 może v1, „mina smaku" |
| Pupil/temat w stylu | AI bounded | ⛔ silnik #2 |

Artysta decyduje, które warstwy dozwolone na jego pracy (`allowed_customizations[]`).
🟡 **Do decyzji (wisi od 2026-07-10):** ostateczny zestaw warstw i ile ich. Rekomendacja: tonacja + kadr + rozmiar + oprawa + zestaw; tekst i pupil później.

---

## 8. Mobile-first + step-flow (zasady, świeży design)

Reguły (z 15 §1b, zweryfikowane adwersaryjnie — zostają jako zasady, nie jako konkretne ekrany):
- **Paradygmat = prowadzony przepływ (step-flow), jedna decyzja na ekran** (🔬 Baymard: +do 35% konwersji vs gęsta powierzchnia).
- **Nie freeform-drag** (🔬 NN/g: touch-drag multi-obiekt = pułapka).
- Akcje w dolnej 1/3 ekranu; cele ≥44px; góra ekranu = strefa nieosiągalna kciukiem.
- Mocne presety układów (ściana wygląda dobrze zanim klient cokolwiek ruszy — zabija paraliż wyboru).
- Projektujemy od 390px w górę, nie odwrotnie.

Design system: tokeny z 15 (kolor/typografia/odstępy — przemyślane, zostają), zaadaptowane mobile-first. Akcent 🟡 (lawenda z 15 vs ciepły dąb z 17) — decyzja przy Fazie 1.

---

## 9. Stack i szwy (15 §5–6; kolejność zmieniona)

- **Teraz: mockupy HTML mobile-first.** Next.js dopiero gdy flow i design zamknięte.
- **Później:** Custom Next.js + Supabase (Postgres) + Stripe + Tailwind/shadcn (🔬 obroniony 2026→2035 dla produktu opartego na treści+integracjach).
- **Szew vs silnik:** cienka nazwana granica (Gelato, `ArtworkSource`, model AI, CDN, płatności) rysowana od dnia zero; ciężka maszyneria dopiero, gdy dane zza szwu powiedzą „warto". Reguła trójki. Nudny stack.
- **Trzy zmienne za szwem:** Gelato (druk), model AI (przez agregator), CDN obrazków.

---

## 10. ⛔ Czego NIE budujemy teraz
Marketplace/upload twórców (faza 2) · canvas-builder · generatywna warstwa AI dla klienta · prawdziwa rozmowa AI (mockup udaje) · backend · osobna wyszukiwarka (Postgres FTS+pgvector wystarczą) · multi-vendor/mikroserwisy.

---

## 11. 🟡 Otwarte pytania
- **Ekran „ściany" na mobile** — wynik z korektą vs edytor slotów (Faza 2).
- **Akcent/tożsamość wizualna** — lawenda vs ciepły dąb (Faza 1).
- **Zestaw warstw customizacji** — ile, które (wisi od 2026-07-10).
- **Cennik** — marża %, podłoga, rynek docelowy (USA?), papier (COSTS.md).
- **Napis w v1?** — mina smaku, wymaga kurowanych szyn.
- **VAT/podatki** — progi UE + „economic nexus" USA → księgowy (COSTS.md).
- **Dystrybucja** — największa niewiadoma; do kogo docierasz taniej niż reklamą? (patrz PROJECT_STATUS + MARKET.md).

---

## Powiązane dokumenty
- [`COSTS.md`](COSTS.md) — realne koszty Gelato + scenariusze marży
- [`MARKET.md`](MARKET.md) + [`market-map.html`](market-map.html) — mapa rynku, konkurencja, prawo AI
- [`DECISIONS.md`](DECISIONS.md) — log decyzji (z 17, + D-017 = to połączenie)
- [`PRODUCT_ARCHITECTURE.md`](PRODUCT_ARCHITECTURE.md), [`AI_SYSTEM.md`](AI_SYSTEM.md), [`USER_RESEARCH.md`](USER_RESEARCH.md), [`BUSINESS.md`](BUSINESS.md), [`WALL_DESIGN_KNOWLEDGE.md`](WALL_DESIGN_KNOWLEDGE.md) — Biblia z 17
- [`reference/`](reference/) — kopie źródeł (15 prototyp HTML, 17 mockupy/specs/catalog-demo) tylko do czytania
