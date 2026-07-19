# VISION — Latenca (strategiczny przegląd)

> **Co to jest:** wysokopoziomowa wizja — *co* budujemy, *dlaczego*, *dokąd zmierzamy* i *co bierzemy z konkurencji*. To dokument do konsultacji (Artur ↔ ChatGPT ↔ Claude), nie nowy „lock".
> **Relacja do innych dokumentów:** szczegółowa specyfikacja = [`PRODUCT_BIBLE.md`](PRODUCT_BIBLE.md); zablokowane decyzje = [`DECISIONS.md`](DECISIONS.md) (zwłaszcza D-020, D-021); benchmarki konkurencji, na których się opieramy = folder [`../Analizy/`](../Analizy/) (Fy! · Mixtiles · Ideogram · Displate).
> **Status:** synteza do przeglądu. Trzyma pełną ambicję jako gwiazdę północną i pokazuje, jak fazuje się do realnego, jednoosobowego MVP.
> Język: polski (proza), angielski (kod/nazwy). Ostatnia aktualizacja: 2026-07-19.

---

## 1. Dlaczego Latenca istnieje (problem + luka)

Wybór sztuki na ścianę jest **paraliżujący**. Ludzie wiedzą, że pusta ściana im przeszkadza, ale nie wiedzą, co na niej powiesić — boją się, że wybiorą źle, że nie będzie pasować, że wyda pieniądze i pożałują.

Cały rynek odpowiada na to **jednym z dwóch sposobów** — i żaden nie leczy tego lęku:

- **Nieskończony wybór** (Displate, Society6, marketplace'y) → jeszcze większy paraliż. „Milion plakatów" nie pomaga komuś, kto nie wie, czego chce.
- **Twoje własne zdjęcia** (Mixtiles) → świetne, jeśli masz gotową grafikę. Nie pomaga, gdy jej nie masz i potrzebujesz *pomysłu*, nie druku.

**Luka:** nikt nie sprzedaje **pewności decyzji.** Nikt nie prowadzi Cię za rękę od „nie mam pojęcia" do „tak, to jest to i będzie pasować u mnie".

To jest miejsce Latenki.

---

## 2. Czym jest Latenca (wizja — *co*)

**Latenca to kurowana marka, która pomaga pewnie wybrać i ułożyć sztukę na ścianę.**

Nie „sklep ze sztuką". Nie „druk zdjęć". Nie generator grafik. Sprzedajemy **pewność**, nie same obrazy. Rdzeniem nie jest pojedyncze dzieło, tylko **dobra ściana / zestaw**.

Doświadczenie łączy trzy rzeczy, których konkurencja ma tylko po kawałku:
1. **Moment AI, który daje pewność** — inteligentny doradca prowadzi Cię krokami (pokój → styl → rozmiar) do kuratorowanego, dopasowanego zestawu. To nasze „drzwi wejściowe".
2. **Kuratorski gust** — mały, opiniowany, edytorski wybór zamiast nieskończonej siatki. To jest fosa, której marketplace nie skopiuje.
3. **Spokojny, premium język wizualny** — sam produkt wygląda jak marka, której się ufa (mamy to już zbudowane w mockupach).

**Ważne (D-020):** „inteligencja" Latenki = **orkiestracja + kuracja + prowadzone doświadczenie** (dyrygent), a nie własny wytrenowany model. Modele AI (vision, LLM, generacja) **wynajmujemy** z zewnątrz, za wymienialną warstwą — możemy „wypiąć i wpiąć coś mądrzejszego". **Nasza przewaga to wykonanie, doświadczenie, kuracja, marka i bycie naprawdę dobrym pierwszym — nie model.**

---

## 3. Co nas realnie wyróżnia od dnia 1

- **Sprzedajemy pewność, nie wybór.** Cała obietnica: *„Art you'll be sure about."* Nikt na rynku tak nie stoi.
- **Kuracja/gust jako tożsamość.** W świecie zalanym grafiką AI przeżywają tylko kurowane marki (Mixtiles, Displate); otwarte marketplace'y (Society6, Redbubble) się kanibalizują. AI jest u nas **źródłem, nigdy tożsamością.**
- **Doświadczenie/design.** To, nad czym już siedzieliśmy — flow i wygląd — jest warstwą, której nikt z czwórki nie ma dobrze zrobionej naraz.

---

## 4. Czego uczą nas 4 benchmarki (co konkretnie bierzemy)

Kluczowa obserwacja: **każdy z nich ma jeden mocny kawałek, nikt nie ma całości.** My składamy całość i owijamy ją warstwą wyglądu, której im brakuje.

| Benchmark | Ich mocna strona | **Co bierzemy** | **Czego NIE bierzemy** |
|---|---|---|---|
| **Fy! (Art Advisor)** | Mają w tle prawdziwe AI, które doradza i podmienia obrazy — dokładnie nasz kierunek | **Koncept doradcy** jako drzwi wejściowe (prowadzi, kuruje, doradza) — nasz główny wyróżnik | Ich **słaby UX/UI** — my robimy to z mocnym designem |
| **Mixtiles** | Stary system, ale nailuje **prostotę**: ściany, podgląd obrazu, wybór parametrów, super mobile-first | **Podgląd na neutralnej ścianie** + **wybór parametrów bez AI** (rozmiar/format/rama = zwykły konfigurator, nie AI) + **ściana-jako-zestaw** + błyskawiczny mobilny checkout | Inpainting na zdjęciu pokoju usera (zawodny → backlog, D-021) |
| **Displate** | Ładny UX/UI (choć ~10 lat), **świetna prezentacja pojedynczego produktu** | **Piękna strona produktu** + **prosty konfigurator** (rozmiar/wykończenie/rama + cena na żywo) + **trust layer** (recenzje, dowód społeczny) | Marketplace twórców, konfigurator premium (faza 2); brak u nich ścian i AI |
| **Ideogram** | **Nowoczesny UX/UI** — i to jest kierunek, w którym rynek idzie | **Poziom wykończenia UX** (premium, nowoczesny) jako poprzeczka | **Bycie generatorem** — my nie jesteśmy generatorem grafik (patrz §6) |

---

## 5. Pełna wizja jako drabina (gwiazda północna)

Wizja rośnie „ilością AI" i mapuje się 1:1 na mocne strony czwórki. Każdy szczebel jest osobno sprzedawalny.

- **Krok 0 — wygląd** *(mamy)*. Home + flow doradcy na naszym design-systemie. Poziom Ideogram/Displate. ✅
- **Krok 1 — kręgosłup sklepu**. Kuratorowany katalog + piękna strona produktu (Displate) + prosty konfigurator (rozmiar/format/wykończenie/rama, cena na żywo — **zero AI**) + podgląd na neutralnej ścianie (Mixtiles) + checkout (Gelato).
- **Krok 2 — doradca = pierwszy moment AI** (intencja Fy!, zrobiona lepiej). Krótki flow gust+pokój → kuratorowany zestaw + „pewność", napędzany zewnętrznym LLM/vision. **Tu bijemy Fy!:** oni mają AI, my mamy AI **i** świetny UX.
- **Krok 3 — personalizacja treści** *(przyszłość, z jasnym wyzwalaczem)*. Prawdziwa edycja: „weź ten obraz, ale wstaw 3 inne kwiatki". Dopiero **to** wymaga zewnętrznego image-AI. Ruszamy dopiero, gdy pojawi się realna funkcja edycji treści — nie wcześniej.
- **Krok 4+ — skalowanie** *(funded-team, backlog)*: podgląd na *zdjęciu pokoju* usera (inpainting), otwarta generacja, marketplace twórców (Displate).

---

## 6. Gdzie kończy się MVP (uczciwa granica)

**Ideał (Kroki 0–4) = mapa. MVP = pierwszy spójny wycinek, który już się wyróżnia.**

> **MVP = Krok 1 (sklep) + Krok 2 (doradca).**
> Jedyny moment AI w MVP to **doradca**. Wszystko inne (rozmiar/format/rama) to zwykłe parametry produktu, nie AI.

Dlaczego tu, a nie dalej:
- To już **nie jest goły sklep** — ma wyróżniający moment AI od startu.
- Ma **tylko jedną zależność od zewnętrznego AI** (doradca = orkiestracja, najłatwiejszy kawałek), więc jest realne dla jednej osoby + AI.
- **Personalizacja treści (Krok 3)** jest świadomie zaparkowana z wyzwalaczem — nie udajemy AI, którego nie mamy; dodajemy je, gdy będzie realna funkcja.

To rozstrzyga otwarte „lean vs platforma": **ani goły lean, ani 8-miesięczna platforma** — różnicujący MVP z jasnym kręgosłupem, zasilony wzorcami z 4 analiz, z ambicją trzymaną jako drabina powyżej.

---

## 7. Czego świadomie NIE robimy (bariery ochronne)

- **Nie budujemy własnego modelu AI** (D-020). Orkiestrujemy zewnętrzne, za wymienialną warstwą.
- **Nie jesteśmy generatorem grafik.** Otwarta generacja („wpisz prompt, dostań obraz") to rola Ideogramu, nie nasza. Nasz moment AI to *doradztwo i (później) personalizacja*, nie generacja.
- **Nie udajemy AI.** Fałszywe AI niszczy zaufanie, gdy klient je odkryje. Prawdziwe zewnętrzne AI wycelowane wąsko > atrapa.
- **Nie robimy inpaintingu na zdjęciu pokoju usera w v1** (D-021). Domyślnie neutralna/przykładowa ściana; podgląd „na Twojej ścianie" = best-effort, później.
- **Nie budujemy marketplace twórców w v1.** Artysta istnieje jako atrybucja; otwarty upload = faza 2 (szew w modelu danych stawiamy już teraz, tanio).

---

## 8. Największe ryzyko (nie zapominać)

**Ryzykiem numer 1 NIE jest produkt — jest dystrybucja / CAC** (dotarcie do klienta taniej, niż wynosi marża). Możemy zbudować najpiękniejszy system i nikt go nie zobaczy. Dlatego:
- Wyróżnik („sprzedajemy pewność") jest też **hakiem dystrybucyjnym** — o commodity-sklepie nie ma o czym opowiadać, o „doradcy dobierającym sztukę na ścianę" — jest.
- Dyskusja o kanałach (Pinterest / TikTok / IG, produkt-jako-fabryka-treści) musi iść **równolegle** z budową, nie po niej.

---

## 9. Otwarte pytania do ChatGPT

1. **Granica MVP:** czy Krok 1 + 2 to właściwy zakres na start, czy dołożyć jeszcze coś, żeby wyróżnienie było mocniejsze od dnia 1?
2. **Moment AI (doradca):** czy „pewność" da się wiarygodnie dowieźć zewnętrznym LLM/vision w prostym flow, czy potrzeba czegoś więcej, by to nie było „quiz z ładnym UI"?
3. **Dystrybucja:** który kanał realnie dowozi pierwszych obcych klientów taniej niż płatna reklama — i jak produkt sam ma produkować treść do tego kanału?
4. **Kolejność:** budować równolegle sklep (Krok 1) i doradcę (Krok 2), czy sklep w pełni najpierw?
5. **Ryzyko generatora:** czy słusznie trzymamy „nie jesteśmy generatorem", skoro rynek (Ideogram) idzie w stronę generacji — czy to szansa, którą oddajemy?

---

## Powiązane dokumenty
- [`PRODUCT_BIBLE.md`](PRODUCT_BIBLE.md) — pełna specyfikacja (model danych, cennik, customizacja, stack)
- [`DECISIONS.md`](DECISIONS.md) — log decyzji (D-020 = front orkiestrujący AI; D-021 = neutralna ściana à la Mixtiles)
- [`ROADMAP.md`](ROADMAP.md) · [`PROJECT_STATUS.md`](PROJECT_STATUS.md) — plan i bieżący stan
- [`../Analizy/`](../Analizy/) — benchmarki konkurencji (Fy! · Mixtiles · Ideogram · Displate), z których czerpiemy wzorce (nie kopie)
