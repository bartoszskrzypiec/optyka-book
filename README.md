# Optyka dla Artystów Technicznych

Statyczna, polskojęzyczna książka o tym, co obiektyw robi z obrazem — i dlaczego.
Nie kurs fotografii i nie podręcznik optyki: dla artysty CG, który chce
**rozumieć, dlaczego obraz wygląda tak, jak wygląda**, a potem odtworzyć to
w renderze i w compie.

**Strona:** https://bartoszskrzypiec.github.io/optyka-book/

## O czym to jest

Pluginy do compu dają suwak podpisany „halation", „bokeh" albo „aberration".
Ta książka mówi, co jest po drugiej stronie tego suwaka. Że halacja to światło,
które przeszło przez emulsję, odbiło się od spodu podłoża i naświetliło ją
z powrotem od tyłu. Że bokeh to kształt źrenicy wyjściowej widzianej z danego
punktu kadru — i że z tego jednego zdania wynika i „kocie oko", i wirujące tło,
i cebulkowe pierścienie. Że gwiazdki wokół latarni i spadek ostrości po
przymknięciu do f/16 mają dokładnie tę samą przyczynę.

Każdy efekt jest doprowadzony do przyczyny. Jeśli rozdział potrafi zjawisko
tylko opisać, jest niedokończony.

## Co jest w środku

- **42 rozdziały** w dziewięciu częściach, ułożonych tak, że nic nie pojawia
  się, zanim nie ma czym tego wytłumaczyć: Fresnel przed ghostingiem, dyfrakcja
  przed gwiazdkami, źrenica przed bokeh, a wady przed konstrukcjami — bo
  konstrukcja obiektywu jest odpowiedzią na wadę.
- **~30 dodatków** dla tych, którzy chcą głębiej — tu mieszkają wyprowadzenia
  i policzone przykłady.
- **`matematyka/`** — primer „Zanim zaczniesz" z matematyką, na której opierają
  się rozdziały.
- Wizualizacje: diagramy SVG, diagramy sterowane suwakiem, symulacje Canvas2D
  i widgety 3D na three.js. Zero rastrów w repozytorium.

### Części

| | Część | O czym |
|---|---|---|
| I | Światło, zanim dotknie szkła | Fala czy promień, załamanie, dyspersja, Fresnel, soczewka cienka |
| II | Kadr i głębia | Ogniskowa i format, przysłona f vs T, źrenice, głębia ostrości, bokeh, dyfrakcja |
| III | Wady, czyli charakter | Sferyczna, koma, astygmatyzm, krzywizna pola, dystorsja, LoCA i TCA, korekcja i jej cena |
| IV | Konstrukcje | Petzval, Tessar, Sonnar, Double Gauss, retrofokus, tele i katadioptryk, zoom, anamorf |
| V | Światło, które zbłądziło | Veiling glare, ghosting, powłoki, starburst, smugi anamorficzne |
| VI | Matryca, taśma i czas | Fotony→liczby, halacja, ziarno, winietowanie, zakres dynamiczny, migawka, oddech |
| VII | To wszystko w CG | Kamera w rendererze, render vs comp, Z-depth, undistort/redistort, kolejność w compie |
| VIII | Optyka jako język operatorski | Ogniskowa jako decyzja, ostrość jako reżyseria uwagi, powściągliwość i faktura, format |
| IX | Czytanie kadru | Odwrotna inżynieria kadru; dlaczego akceptujemy wady i kiedy CG je przesadza |

## Struktura

```
index.html                              spis treści
rozdzialy/rozdzial-NN-slug.html         42 rozdziały
dodatki/dodatek-x-slug.html             dodatki
matematyka/podstawy-matematyczne.html   primer „Zanim zaczniesz"
assets/style.css                        arkusz stylów tej książki
assets/*.js, assets/*.css               wspólny toolkit (patrz niżej)
assets/vendor/                          three.js, wgrany do repo
dev/                                    narzędzia deweloperskie, nie budowanie
```

## Uruchomienie

Nie ma czego budować. Otwórz `index.html` w przeglądarce albo podaj katalog
dowolnym serwerem statycznym:

```
python -m http.server 8000
```

Widgety 3D są modułami ES i wymagają serwera (`file://` zablokuje import) —
reszta książki działa nawet z otwartego pliku. Kiedy import jest zablokowany,
widget pokazuje komunikat z przyczyną, nigdy pustego prostokąta.

## Narzędzia deweloperskie

```
python dev/scaffold.py szkielet   tworzy brakujące strony (istniejących nie rusza)
python dev/scaffold.py sprawdz    kontrola spójności — musi przechodzić przed commitem
python dev/slowa.py               licznik prozy i wizualizacji (cel: 2000–3500 słów, 5–8 wiz.)
python dev/wstaw.py  <strona> <plik>   wstawia treść w miejsce <!-- TRESC -->
python dev/dopisz.py <strona> <plik>   dopisuje sekcje przed blokiem „Z praktyki"
```

`sprawdz` łapie martwe linki, rozjazd nawigacji górnej z dolną, jednostronne
`EXT OF`, brakujące bloki obowiązkowe, modal bez hosta, widget 3D bez fallbacku
i wzór bez zdefiniowanych symboli. Przy siedemdziesięciu stronach z ręcznie
utrzymywaną nawigacją to jedyny sposób, żeby złapać literówkę w linku
„Następny →".

## Zależności

Jedna: **three.js**, wgrany do repozytorium w `assets/vendor/`, nie ładowany
z CDN-a. Poza fontami Google żadna strona nie wysyła zapytania na zewnątrz.
Książka działa offline.

Reszta `assets/` to kopie ze wspólnego toolkitu
[learning-materials](https://github.com/bartoszskrzypiec/learning-materials) —
kopiowane, nie linkowane, bo każda książka wdraża się niezależnie.

## Rodzina

| Projekt | Strona |
|---|---|
| Ray Tracing dla Artystów Technicznych | https://bartoszskrzypiec.github.io/raytracing-book/ |
| Lookdev dla Artystów Technicznych | https://bartoszskrzypiec.github.io/lookdev-book/ |
| Pipeline dla Artystów Technicznych | https://bartoszskrzypiec.github.io/pipeline-book/ |
| PxrSurface Guide | https://bartoszskrzypiec.github.io/pxrsurface-guide/ |
| Atmosfera i chmury dla ciekawych | https://bartoszskrzypiec.github.io/atmosfera_chmury_book/ |

Wspólny toolkit: https://github.com/bartoszskrzypiec/learning-materials
