# PRD — Product Requirements Document

## 1. Wizja
Zakup sztuki na ścianę jest trudny: ludzie nie znają terminologii, nie wiedzą jaki rozmiar
pasuje, boją się że "nie będzie pasować do wnętrza". ArtAdvisor usuwa to tarcie — użytkownik
opisuje swoją przestrzeń własnymi słowami, a asystent proponuje gotowe, dopasowane kompozycje
i pokazuje je zawieszone na jego ścianie.

## 2. Grupa docelowa (persony)

### Persona A — "Niepewny nowicjusz" (główna)
Kupuje pierwszy raz sztukę do mieszkania. Nie zna stylów ani rozmiarów. Potrzebuje prowadzenia
za rękę i pewności, że wybór będzie dobry. Ceni wizualizację "u siebie".

### Persona B — "Zdecydowany dekorator"
Ma wizję, szuka konkretnej estetyki (np. "minimalizm w chłodnych błękitach do sypialni").
Chce szybko dostać trafne propozycje bez zbędnego quizu. Ścieżka: czat od razu.

### Persona C — "Kompletujący galerię"
Ma jeden obraz, chce dobrać zestaw 3-5 spójnych prac (gallery wall). Potrzebuje kuracji
dbających o spójność kolorystyczną i kompozycyjną.

## 3. Historyjki użytkownika (MVP)
- Jako użytkownik chcę opisać pokój i styl własnymi słowami, aby dostać dopasowane propozycje.
- Jako użytkownik chcę odpowiedzieć na kilka szybkich pytań (lub je pominąć), aby doprecyzować brief.
- Jako użytkownik chcę zobaczyć 2-3 gotowe kuracje z ceną i krótkim uzasadnieniem.
- Jako użytkownik chcę zobaczyć wybraną kurację zawieszoną na wizualizacji ściany.
- Jako użytkownik chcę zapisać ulubione prace na shortliście.
- Jako użytkownik chcę wrócić do sesji bez zakładania konta (identyfikacja przez fingerprint).

## 4. Historyjki v1 (po MVP)
- Jako użytkownik chcę wgrać zdjęcie mojego pokoju i zobaczyć sztukę na MOJEJ ścianie (AR/inpainting).
- Jako użytkownik chcę zobaczyć DLACZEGO system polecił daną pracę (transparentność).
- Jako użytkownik chcę, aby system uczył się z moich lajków/odrzuceń.
- Jako użytkownik chcę udostępnić projekt ściany znajomemu po link.

## 5. Metryki sukcesu
- Konwersja: % sesji kończących się dodaniem do koszyka.
- Zaangażowanie: średnia liczba wygenerowanych kuracji na sesję.
- Trafność: % kuracji, w których użytkownik kliknął "Set as my wall" / dodał do shortlisty.
- Retencja sesji: % powracających fingerprintów w 7 dni.

## 6. Poza zakresem (na razie)
- Logowanie i konta użytkowników (v2).
- Płatności (delegujemy do warstwy e-commerce, np. Shopify/Stripe).
- Aplikacja mobilna natywna (na razie responsywny web).
