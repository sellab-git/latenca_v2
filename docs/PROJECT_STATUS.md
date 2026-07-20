# PROJECT_STATUS

> Jedyne źródło prawdy o **bieżącym stanie** projektu — „gdzie jesteśmy teraz". Nadpisywane swobodnie.
> Czytaj to jako pierwsze każdą sesję.

Ostatnia aktualizacja: 2026-07-20

---

## Czym jest ten projekt (folder 18)

**Tu odbywa się praca.** Repo: `sellab-git/latenca_v2`, publiczne, auto-push.

Linia rozwojowa projektów:
- **15. Latenca** — **baza UX/UI.** Skończony design system, 11 prototypów, 201 wersji archiwalnych. Każdy nowy ekran startuje stąd. Kopia w `reference/prototype-html-15/`
- **17. Latenca** — miejsce, gdzie pojawiły się **pomysły na zmianę systemu**: koncept doradcy, governance, briefy ekranów. Kopie w `reference/mockups-17/` i `reference/design-specs-17/`
- **18. Latenca** — **tutaj** ← praca bieżąca
- ~~19. Latenca~~ — **to był tylko test. Nic stamtąd nie bierzemy.**

Źródła (15 i 17) pozostają nietknięte — tylko czytamy i kopiujemy.

---

## Gdzie jesteśmy

**Kierunek produktu jest ustalony i zablokowany** (D-020 … D-033). Skończył się etap „co my w ogóle budujemy" — zaczyna się rzemiosło na jednej, wybranej powierzchni.

**Produkt w jednym zdaniu:** kurowany sklep z jednym momentem AI — sklep jest podłogą, doradca drzwiami frontowymi i **nigdy bramką** (D-022).

**MVP** = Krok 1 (kręgosłup sklepu) + Krok 2 (doradca) — D-030. Doradca to **jedyna** zależność od zewnętrznego AI; rozmiar, format, wykończenie i rama to zwykłe parametry produktu.

**Powierzchnia wyświetlania: płaska ściana** — i **tylko ona** dostaje teraz inwestycje (D-033). Pokoje zostają w prototypie jako przełącznik do porównania, ale bez rozbudowy. Zdjęcia klientów są **czytane, nigdy zamalowywane** (D-031).

---

## Zasady stałe

- **Tylko mockupy HTML** teraz — Next.js później
- **Mobile-first od 390px**; każdy ekran weryfikowany w przeglądarce na 390 i desktopie **zanim** zostanie pokazany (D-032)
- **Nie wymyślamy komponentów** — używamy prawdziwych klas z 15. Jeśli dobra wersja istnieje, **kopiujemy plik i edytujemy** (D-032)
- **Nic ważnego nie zostaje w scratchpadzie.** Wersje zamrażamy w `prototypes/mockups/versions/` — Product v56–v59 przepadł, bo tej zasady nie było
- **Dotykamy tylko folderu 18**
- Artyści = atrybucja teraz, marketplace docelowo (szew w modelu danych już jest)

---

## Aktywne zadania — doskonalenie płaskiej ściany (D-033)

Kolejność od najważniejszego. Cała obietnica pewności spoczywa teraz na liczbach i samej pracy, bo nie ma mebla, o który oko może zahaczyć.

- [ ] **Obrys odniesienia w prawdziwej skali** (sofa albo postać) — odzyskuje intuicję rozmiaru bez zdjęcia pokoju
- [ ] **Porównanie rozmiarów obok siebie** — zamiast przełączania i zgadywania
- [ ] Siatka (`Grid`) — wyczucie skali bez mebla; ma to Fy!
- [ ] Faktura i światło ściany — żeby rama czytała się jako *wisząca*, nie naklejona
- [ ] Ramy i materiały na płaskiej ścianie — **maszyneria już istnieje** w `prototypes/mockups/03-product.html`, nie budujemy od nowa
- [ ] Układy wieloelementowe (para, tryptyk) — zestawy to jedyna ekonomia, która się spina

## Poza powierzchnią wyświetlania

- [ ] **Ręczny test dystrybucji** — 20–30 materiałów, zero automatyzacji, **równolegle** z budową (D-028). Dotyka ryzyka nr 1 i nie wymaga gotowego produktu
- [ ] Krok 1: kręgosłup sklepu (katalog → strona produktu → konfigurator → koszyk)
- [ ] Baza wiedzy projektowej, warstwy A/B/D (D-024) — warunek jakości doradcy od dnia 1
- [ ] Log decyzji od dnia 1; pętli uczenia nie budujemy do czasu wolumenu

---

## Ryzyka

- **Dystrybucja/CAC to ryzyko nr 1**, nie produkt. W formule fosy (D-025) dystrybucja wynosi dziś **~0**. Latenca nie ma jeszcze fosy — ma projekt mechanizmu
- **CAC ~$55–120 vs ~$40 zysku/zamówienie** → pojedyncza sprzedaż na zimnym ruchu jest stratna. Stąd zestawy i rynek USA
- **Over-building** — budowa infrastruktury przed walidacją popytu. Stąd mockupy, nie aplikacja
- **Koszt AI** jest zabezpieczony sześcioma warstwami (`AI_COST_MODEL.md`); maks. ~1 zł za sesję. Sklep działa bez doradcy, więc rachunek za AI nigdy nie zatrzyma sprzedaży

---

## Otwarte pytania

- **Dystrybucja** — który kanał realnie dowozi pierwszych obcych klientów taniej niż reklama? Pinterest jest **hipotezą do testu**, nie kanałem zatwierdzonym
- **Czy przy nieznanej sztuce pokój znaczy więcej niż przy własnych zdjęciach klienta?** Mixtiles może pominąć pokój, bo emocja siedzi w treści. U nas treść jest obca. **Rozstrzygną to klienci, nie analiza**
- Akcent wizualny, zestaw warstw customizacji, marża i rynek docelowy — patrz `PRODUCT_BIBLE.md` sekcja 11

---

## Podgląd makiet

```
python -m http.server 8099    # uruchom w katalogu 18
```
→ **http://localhost:8099/prototypes/index.html** — bieżące makiety, nasze zamrożone wersje, 11 prototypów z 15 i 201 wersji archiwalnych.
**Zanim zaczniesz projektować panel od zera — sprawdź tam. Najprawdopodobniej już istnieje.**
