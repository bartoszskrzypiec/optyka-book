# Tom 1 „Światło i materia” — brief dla autorów rozdziałów

Ten plik czyta każdy agent piszący rozdział Tomu 1 (razem z `CLAUDE.md`). Autorzy piszą
równolegle w obrębie części i **nie widzą swoich tekstów nawzajem**. Dlatego brief ustala:
kto jest właścicielem którego tematu, jakie symbole i liczby obowiązują w całym tomie
i jaką jedną wersję mechanizmu opowiadamy. Jeśli rozdział potrzebuje tematu, którego
właścicielem jest inny rozdział: jedno zdanie i link, bez rozwijania.

Struktura i tytuły: `dev/spis-tom1.json`. Pliki: `tom1/rozdzialy/rozdzial-NN-slug.html`,
`tom1/dodatki/dodatek-x-slug.html`, `tom1/matematyka/podstawy-matematyczne.html`.
Tom 2 (istniejąca książka) leży w `tom2/`, jego spis w `dev/spis-tom2.json`.

---

## 0. Konwencje całego tomu

### 0.1 Rozmiar rozdziału — obowiązuje bramka, nie stara liczba z CLAUDE.md
- **1200–1600 słów prozy w `<div class="section">`** (TL;DR, „Z praktyki”, „Słowniczek”,
  „Co dalej” i podpisy wizualizacji się nie liczą) i **4–6 wizualizacji**. Mierzy
  `python dev/slowa.py`, bramkuje `sprawdz`. Liczba „2000–3500 / 5–8” w CLAUDE.md jest nieaktualna
  (próg obniżony 2026-09-02, bo rozdziały były za gęste dla artysty).
- **2–4 sekcje** `.section`, **najwyżej 3–4 nowe pojęcia** na rozdział — brief każdego rozdziału
  wymienia je w punkcie „Nowe pojęcia”. Czego nie ma na liście, nie wprowadzaj.
- Nadmiar idzie do **bloków „Zaawansowane”** (przycisk `<button class="advanced-btn"
  data-modal-target="adv-…">Zaawansowane: …</button>` w sekcji + treść w `.modal-overlay` na końcu
  strony, jak w Tom 2, Rozdział 1) albo do dodatku. Brief wymienia proponowane „Zaawansowane”
  (0–2 na rozdział). Treść modala nie liczy się do słów sekcji.
- Wizualizacje w briefie: zwykle 5 pozycji; **ostatnia oznaczona (opcjonalna)** — pomiń ją,
  jeśli rozdział ma już 5, albo gdy brakuje miejsca. Nigdy więcej niż 6.

### 0.2 Reguły ogólne (z CLAUDE.md, przypomnienie)
- Forma „ty”. Kolejność zawsze: **co widzisz → dlaczego → liczba**. Rozdział nie otwiera się wzorem.
- Kolejność strony: topnav → readout → eyebrow → h1 → subtitle → TL;DR (dokładnie 3 punkty)
  → `.section` × 2–4 → „Z praktyki” → „Słowniczek” → „Co dalej” → „Idź głębiej” → site-nav
  → `.modal-overlay` (jeśli są bloki „Zaawansowane” lub modale wzorów).
- Zero rastrów. Liczby metryczne, przecinek dziesiętny, także w JS (`.toFixed(1).replace('.', ',')`).
- Każdy `.formula` ma `.sub` z definicją symboli. Pełne wyprowadzenia tylko w dodatkach [WZORY].
- Linki do siostrzanych książek: **absolutne URL-e**. Linki do Tomu 2: względne
  `../../tom2/rozdzialy/rozdzial-NN-slug.html` (dodatki: `../../tom2/dodatki/…`),
  w tekście „Tom 2, Rozdział 3”. W obrębie Tomu 1: „Rozdział 12” / „Dodatek F”, linki względne.
- Budżet 3D: ≤ 8 widgetów sky3d w całym tomie, **tylko te z listy 0.7**. Nikt nie dodaje
  własnego widgetu 3D.

### 0.3 Semantyka kolorów Tomu 1 (te same hexy co Tom 2)
| Token | Hex | Znaczy w Tomie 1 |
|---|---|---|
| amber | `#e8a33d` | **światło / pole EM**: fala, wektor E, promień, foton, fala rozproszona |
| cyan | `#4fc3c0` | **materia**: elektron, chmura elektronowa, dipol, ośrodek, atom, wiązanie |
| violet | `#9c82d8` | **strata**: absorpcja, tłumienie, κ, zanik; też afordancja „idź głębiej” |
| raster | `#6e93be` | **skala makro**, czyli to, co widzi oko lub kamera: kolor wynikowy, piksel, próbka materiału |

- Wektor E zawsze amber. Elektron, chmura i dipol cyan. Jądro ciemniejszy cyan albo neutralny szary `#8a8f98`, nigdy amber.
- Krzywe absorpcji i κ violet. „Kolor wynikowy” to łatka w rzeczywistym kolorze sRGB w ramce raster.
- Pole B, gdy trzeba je odróżnić od E: amber przerywany albo amber z kryciem 50%. **Nie** nowy kolor.
- Pasek tęczy tylko jako oś długości fali, nie jako dekoracja.

### 0.4 Terminologia (polski termin, angielski w nawiasie przy pierwszym użyciu w rozdziale)
- **polaryzacja światła** (polarization of light) vs **polaryzacja ośrodka** (polarization density, P).
  Nigdy gołe „polaryzacja”, jeśli kontekst nie rozstrzyga.
- **polaryzowalność** α (polarizability) — cecha jednej cząsteczki.
- **dipol indukowany** (induced dipole) vs **dipol trwały** (permanent dipole, np. woda).
- **rezonans** (resonance), **częstość rezonansowa** ω₀, **tłumienie** γ (damping).
- **współczynnik załamania** n (refractive index); **zespolony współczynnik załamania** ñ = n + iκ.
- κ: „kappa”, **urojona część współczynnika załamania** (ang. extinction coefficient).
  Po polsku **nie nazywaj κ „współczynnikiem ekstynkcji”**, bo ta nazwa należy do σₜ.
- **współczynnik absorpcji** σₐ, **rozpraszania** σₛ, **ekstynkcji** σₜ = σₐ + σₛ [1/m].
  To notacja z volume renderingu, celowo zgodna z rendererami.
- **przekrój czynny** (cross-section) C [m²] jednej cząstki: C_sca, C_abs, C_ext.
- **funkcja fazowa** (phase function): przy pierwszym użyciu dopisz, że nie ma nic wspólnego z fazą
  fali, tylko opisuje rozkład kątowy rozpraszania.
- **rozpraszanie spójne / niespójne** (coherent / incoherent).
- **przerwa energetyczna** (band gap), **pasmo walencyjne / przewodnictwa** (valence / conduction band).
- **wiązanie sprzężone** (conjugated bond), **chromofor** (chromophore).
- **barwnik** (dye): rozpuszczony, nie rozprasza. **Pigment** (pigment): nierozpuszczalne ziarno.
- **częstotliwość plazmowa** ωₚ (plasma frequency); **głębokość wnikania** δ (penetration / skin depth).
- **dopasowanie współczynników** (index matching).
- **orbital** zawsze jako „chmura”, „obszar, gdzie elektron najpewniej jest”; nigdy „tor”.

### 0.5 Symbole (jedno znaczenie w całym tomie)
| Symbol | Znaczenie | Jednostka / uwaga |
|---|---|---|
| λ | długość fali w próżni | nm; w ośrodku zawsze λ/n |
| f | częstotliwość | Hz (nie ν) |
| ω | częstość kołowa, ω = 2πf | rad/s |
| T | okres, T = 1/f | fs |
| k | liczba falowa, k = 2π/λ | 1/m (≠ κ!) |
| c | prędkość światła w próżni | 2,998·10⁸ m/s; w tekście „300 000 km/s” |
| **E** | natężenie pola elektrycznego (wektor) | V/m; pogrubione lub ze strzałką |
| **B** | indukcja pola magnetycznego | T |
| E_γ | energia fotonu | eV; E_γ = hc/λ ≈ 1240/λ[nm] |
| h | stała Plancka | 6,626·10⁻³⁴ J·s = 4,136·10⁻¹⁵ eV·s |
| φ | faza | rad lub stopnie |
| A | amplituda | |
| I | natężenie, I ∝ A² | W/m² |
| e | ładunek elementarny | 1,602·10⁻¹⁹ C |
| mₑ | masa elektronu | 9,109·10⁻³¹ kg |
| x | wychylenie elektronu z równowagi | m (≪ 0,1 nm) |
| **p** | moment dipolowy, p = q·d | C·m |
| α | polaryzowalność, **p** = α**E** | C·m²/V; liczbowo podawaj objętość polaryzowalności α/(4πε₀) w m³ |
| ω₀ | częstość rezonansowa | |
| γ | tłumienie oscylatora | 1/s |
| N | gęstość liczbowa (cząsteczek lub elektronów) | 1/m³ |
| **P** | polaryzacja ośrodka, P = N·p | C/m² |
| ε₀ | przenikalność próżni | 8,854·10⁻¹² F/m |
| εᵣ | względna przenikalność | εᵣ = n² (ośrodek niemagnetyczny) |
| χ | podatność, εᵣ = 1 + χ | tylko R10 i Dodatek C |
| n, κ, ñ | część rzeczywista, urojona, ñ = n + iκ | |
| σₐ, σₛ, σₜ | współczynniki absorpcji, rozpraszania, ekstynkcji | 1/m; σₐ = 4πκ/λ |
| δ | głębokość wnikania, δ = 1/σₐ = λ/(4πκ) | nm lub m |
| C_sca, C_abs, C_ext | przekroje czynne cząstki | m²; σₛ = N·C_sca |
| a | promień cząstki | µm |
| x_M | parametr rozmiaru Mie, 2πa/λ | w R14 można pisać „x”, zaznaczając, że to nie wychylenie z R8 |
| Q | sprawność, Q = C/(πa²) | |
| g | czynnik asymetrii, ⟨cos θ⟩ | −1…1, jak w Henyeyu–Greensteinie |
| θ | kąt rozpraszania / padania | ° |
| R, F₀ | współczynnik odbicia; R przy padaniu prostopadłym | 0–1 lub % |
| θ_B | kąt Brewstera, tan θ_B = n₂/n₁ | |
| ωₚ | częstotliwość plazmowa | podawaj też w eV |
| E_g | przerwa energetyczna | eV |
| V | liczba Abbego | tylko wzmianka; właściciel: Tom 2, Rozdział 2 i Tom 2, Dodatek A |

**Konwencja znaku:** zależność czasowa e^{−iωt}, więc ñ = n + iκ, κ ≥ 0 dla ośrodka pochłaniającego.
Tylko Dodatek H wspomina konwencję inżynierską n − iκ.

### 0.6 Standardowe liczby (używaj dokładnie tych)
| Wielkość | Wartość w tomie |
|---|---|
| zakres widzialny | **380–750 nm** |
| energia fotonu widzialnego | **1,65–3,26 eV** |
| zielone odniesienie | **550 nm → 2,25 eV; f ≈ 5,45·10¹⁴ Hz; T ≈ 1,8 fs** |
| barwy do wykresów | fiolet 400, niebieski 450, zielony 550, żółty 580, czerwony 650, skraj czerwieni 700 nm |
| rozmiar atomu | **≈ 0,1 nm**; jądro ≈ 10⁻¹⁵ m |
| λ/atom | **≈ 5000** |
| N₂ | ≈ 0,3 nm; objętość polaryzowalności ≈ 1,7·10⁻³⁰ m³ |
| wodór, jonizacja | 13,6 eV |
| sód, linia D | **589 nm (2,1 eV)**; neon ≈ 640 nm |
| powietrze | **n = 1,0003**; N ≈ 2,5·10²⁵ 1/m³ |
| woda | **n = 1,33** (1,331 czerwień – 1,343 fiolet); εᵣ statyczne ≈ 80 |
| lód | **n = 1,31** |
| szkło crown (BK7) | **n = 1,52**, V ≈ 64; flint 1,6–1,9 |
| diament | **2,42** |
| celuloza / keratyna / skóra | ≈ 1,53 / ≈ 1,55 / ≈ 1,4 (F₀ ≈ 0,028) |
| polimer, spoiwo | ≈ 1,5 (PMMA 1,49; PS 1,59); olej lniany ≈ 1,48 |
| TiO₂ (rutyl) | n ≈ 2,7; ziarno optymalne 0,2–0,3 µm |
| F₀ woda / szkło / diament | **0,02 / 0,04 / 0,17** |
| Brewster woda / szkło | **53° / 57°** |
| kąt graniczny szkło / woda | 41° / 49° |
| E_g | SiO₂ ≈ 9 eV · diament 5,5 · ZnO 3,3 · TiO₂ ≈ 3,0–3,2 · CdS 2,4 · HgS 2,0 · CdSe 1,7 · Si 1,1 · grafit ≈ 0 |
| wiązania | O–H ≈ 4,8 eV; wodorowe ≈ 0,2 eV; H–O–H **104,5°** |
| Rayleigh | (700/450)⁴ ≈ **5,9×**; (700/400)⁴ ≈ 9,4× |
| grubość optyczna atmosfery (pion) | ≈ 0,1 przy 550 nm; 0,2 przy 450; 0,04 przy 700 |
| kropla chmury | promień **5–10 µm** („ok. 10 µm”), x_M ≈ 100; g ≈ 0,85 |
| dym, aerozol | **0,1–1 µm** |
| woda, absorpcja przy 700 nm | σₐ ≈ 0,6 1/m (1/e na ok. 1,5 m) |
| głębokość wnikania w metal | **≈ 10 nm** (Al ≈ 7 nm przy 550 nm) |
| ωₚ | Al ≈ 15 eV; Ag efektywnie ≈ 3,8 eV |
| próg przejść z pasma d | Au ≈ 2,4 eV (≈ 520 nm); Cu ≈ 2,1 eV (≈ 590 nm); Ag ≈ 3,9 eV (UV) |
| F₀ metali (liniowe RGB, orientacyjnie) | Ag ≈ (0,97; 0,96; 0,91), Al ≈ 0,91, Au ≈ (1,00; 0,77; 0,34), Cu ≈ (0,96; 0,64; 0,54), Fe ≈ 0,56 |
| β-karoten | 11 sprzężonych C=C, absorpcja ≈ 450–480 nm |
| hemoglobina / chlorofil | Soret ≈ 415, Q ≈ 540 i 575 nm / ≈ 430 i ≈ 660 nm |
| łuski włosa | ≈ 3° |
| tęcza / halo | **42°** (czerwień 42°, fiolet 40,5°), wtórna **51°** / **22°**, 46° |

### 0.7 Przydział widgetów sky3d (cała pula: 8)
| # | Rozdział | Widget | Dlaczego 3D |
|---|---|---|---|
| 1 | R2 | Fala płaska E ⊥ B ⊥ kierunek; przełącznik polaryzacji liniowa / kołowa / niespolaryzowana | kołowa to spirala, w rzucie wygląda jak liniowa |
| 2 | R4 | Orbitale jako chmury punktów 1s, 2s, 2p×3; przełącznik H / C / Na | kształt p i przenikanie chmur znikają w 2D |
| 3 | R5 | Geometria H₂O, CO₂, CH₄, NH₃ z wektorem momentu dipolowego | brak dipola CO₂ to kwestia symetrii przestrzennej |
| 4 | R11 | „Pączek” promieniowania dipola sin²θ, oś drgań, suwak ω | przekrój gubi symetrię obrotową i ciemną oś |
| 5 | R13 | Kopuła nieba z wektorami polaryzacji, ruchome Słońce, pas 90° | wzór żyje na sferze |
| 6 | R14 | Funkcja fazowa Mie jako bryła, suwak x | płat do przodu i listki boczne |
| 7 | R25 | Włos jako walec z łuskami: stożki R, TT, TRT | stożek wokół osi włókna |
| 8 | R27 | Obserwator, punkt antysłoneczny, stożki 42° i 51° z kroplami | tęcza to stożek, nie łuk w miejscu |

Każdy widget ma `.viz3d__fallback`, a zdanie obok niesie treść bez widgetu.

### 0.8 Jedna wersja mechanizmu: łańcuch faz (R9, R11, R12, R15, R16, R17, R18)
Każdy z tych rozdziałów opowiada **swoje ogniwo tego samego łańcucha**. Nie wolno go przestawiać.
1. (R9) Elektron pchany polem **poniżej** rezonansu drga prawie **w fazie** z polem.
   **Przy** rezonansie spóźnia się o 90° i pochłania najwięcej. **Powyżej** drga w przeciwfazie.
2. (R11) Drgający elektron promieniuje falę o tej samej częstotliwości. Fala niesie fazę ruchu
   elektronu, opóźnioną o czas przelotu r/c.
3. (R12) Fala z **całej płaskiej warstwy** dipoli drgających razem, zsumowana w punkcie przed
   warstwą, jest **opóźniona o 90°** względem ich ruchu. Powód jest geometryczny: najbliższy dipol
   dochodzi pierwszy, dalsze coraz później, suma wypada ćwierć okresu później.
4. (R15) Duży fazor fali padającej + mały fazor warstwy opóźniony o 90° = suma lekko obrócona
   wstecz, czyli **opóźnienie fazy**. Warstwa po warstwie grzbiety posuwają się wolniej:
   prędkość fazowa c/n, n > 1. **Nic nie jest pochłaniane.**
5. (R16) Bliżej rezonansu amplituda elektronu rośnie, więc rośnie opóźnienie i n. Rezonans szkła
   jest w UV, dlatego niebieski załamuje się mocniej.
6. (R17) Przy rezonansie elektron jest 90° za polem, fala warstwy 180° za falą padającą i ją
   **odejmuje**: amplituda maleje, pojawia się κ.
7. (R15, blok „Zaawansowane”) Powyżej rezonansu faza przyspiesza, n < 1 (promienie X). Prędkość
   fazowa > c jest dozwolona, bo nie niesie informacji.
8. (R18) Te same dipole promieniują też **wstecz**. W głębi fale wsteczne się znoszą, zostaje
   wkład przy granicy: to odbicie.

Zakazane w całym tomie: „foton jest pochłaniany i natychmiast wysyłany ponownie” jako mechanizm n;
„światło zwalnia, bo odbija się między atomami”; „foton w szkle leci wolniej” bez wyjaśnienia.

### 0.9 Mity — każdy autor sprawdza swój tekst (w nawiasie rozdział, który je prostuje)
- Pochłonięcie i ponowna emisja jako źródło n (R15; nikt inny tego nie rozwija).
- Niebo niebieskie od kurzu, od odbicia oceanu, bo „powietrze jest niebieskie” (R13).
- Planetarny model Bohra dosłownie, elektron na torze (R4; dozwolony tylko jako historyczny szkic).
- „Metal błyszczy, bo jest gładki” (R20: gładkość decyduje o ostrości odbicia, nie o metaliczności).
- „Mokre jest ciemniejsze, bo woda pochłania” (R24, właściciel pełnego wyjaśnienia).
- „Czarne nic nie odbija” (R21: błyszcząca czerń ma odblask ≈ 4%).
- „Biel to odbicie jak w lustrze” (R19, R24: biel to wielokrotne rozpraszanie na granicach).
- „Chmury białe, bo woda biała”, „szare, bo brudne” (R26).
- „Tęcza stoi w konkretnym miejscu” (R27: każdy obserwator ma własną).
- „Żyły niebieskie od niebieskiej krwi” (R25). „Niebieskie oczy mają niebieski pigment” (R22, R25).
- „Kolor to długość fali” (R1, R27: kolor to odpowiedź oka na całe widmo).
- „Przezroczyste = nie oddziałuje” (R12, R19).
- „Szkło to płynąca ciecz” (R6, jeśli w ogóle: mit).

---

## Część I — Światło, zanim spotka materię (R1–R3)

### R1 · Czym właściwie jest światło · `rozdzial-01-czym-jest-swiatlo`
- **(a) Pytanie:** czym jest to, co renderer nazywa promieniem RGB? Po lekturze przeliczasz λ ↔ f ↔ E_γ, znasz skalę (λ ≈ 5000 atomów) i wiesz, kiedy myśleć falą, a kiedy porcją.
- **Nowe pojęcia (4):** widmo EM · λ i f · foton i eV · kolor ≠ długość fali.
- **(b) Sekcje:**
  1. *Co widzisz:* pryzmat, widmo ciągłe żarówki kontra jedna linia lampy sodowej. Światło to fala pola EM: λ, f, c; widzialne jako wąski pasek widma.
  2. *Skala:* 550 nm kontra 0,1 nm atomu. Fala „widzi” materię jako gładką (zapowiedź R12).
  3. *Porcje:* foton, E_γ = hc/λ w eV; matryca liczy porcje (link Tom 2, Rozdział 27). Dwa opisy jednej rzeczy.
  4. *Kolor to nie λ:* widmo → oko/kamera → trzy liczby; metameria jednym zdaniem + link lookdev.
- **Zaawansowane:** „Dlaczego akurat 380–750 nm” (widmo Słońca, okno przezroczystości wody, energia wiązań).
- **(c) Wzory:** c = λ·f; E_γ = hc/λ; E_γ[eV] ≈ 1240/λ[nm].
- **(d) Wizualizacje:**
  - SVG+slider: widmo EM (oś log), suwak λ, odczyt f, T, E_γ.
  - Static SVG: pasek skali log: atom, cząsteczka, wirus, λ = 550 nm, włos 70 µm.
  - Canvas2D: widmo ciągłe kontra liniowe (sód, neon).
  - Static SVG: widmo → trzy krzywe czułości → RGB (raster, sam kształt krzywych).
  - Static SVG (opcjonalna): ta sama wiązka jako grzbiety fali i jako kropki-fotony przy słabym świetle.
- **(e) Mity:** kolor = λ; foton jako kulka; „albo fala, albo cząstka”.
- **(f) Wymaga:** nic. **Nie rusza:** pól E/B i polaryzacji (R2), interferencji (R3), poziomów w atomie (R4).
- **(g) Linki:** Dodatek A, Dodatek M; Tom 2, Rozdział 1; Tom 2, Rozdział 27; https://bartoszskrzypiec.github.io/raytracing-book/ (spectral rendering); https://bartoszskrzypiec.github.io/lookdev-book/ (kolor).
- **(h) Z praktyki:** renderer RGB kontra spektralny: co tracisz przy trzech „długościach fali” (dyspersja, metameria pod lampą sodową).

### R2 · Pole E i B: fala, która pcha ładunki · `rozdzial-02-pole-e-i-b`
- **(a) Pytanie:** co fizycznie faluje i jak ta fala działa na elektron? Po lekturze wiesz, że fala to pole pchające ładunek, E ⊥ B ⊥ kierunek, i czym jest polaryzacja światła.
- **Nowe pojęcia (3):** pole E jako siła na ładunek · fala płaska E ⊥ B · polaryzacja światła.
- **(b) Sekcje:**
  1. *Co widzisz:* okulary polaryzacyjne gaszą odblask z wody, obrócony polaryzator na LCD. Pole jako „siła czekająca na ładunek”: F = qE.
  2. *Fala płaska:* E i B razem, prostopadle; B = E/c, więc siła magnetyczna na wolny elektron jest ∝ v/c i w optyce liczy się prawie tylko E. Pole zmienia kierunek co 0,9 fs.
  3. *Polaryzacja światła:* liniowa, kołowa, niespolaryzowana; polaryzator jako filtr kierunku E; prawo Malusa.
- **Zaawansowane:** „Ile to jest volt na metr” (słońce ≈ 1000 W/m² → E ≈ 900 V/m; przesunięcie elektronu — liczba z Dodatku A).
- **(c) Wzory:** F = q·E; B = E/c; I = I₀cos²θ (θ kąt między polaryzatorami).
- **(d) Wizualizacje:**
  - **sky3d #1:** fala płaska E ⊥ B ⊥ kierunek, przełącznik polaryzacji.
  - SVG+slider: elektron (cyan) pchany polem E (amber) w jednym punkcie, suwak czasu.
  - SVG+slider: dwa polaryzatory, suwak kąta, odczyt I/I₀.
  - Canvas2D: niespolaryzowane jako losowo skaczący wektor E; za polaryzatorem stały kierunek.
  - Static SVG (opcjonalna): widok od czoła trzech polaryzacji (odcinek, okrąg, gwiazdka).
- **(e) Mity:** fala w eterze; „B nieważne, bo małe” bez wyjaśnienia; „niespolaryzowane = bez kierunku pola”.
- **(f) Wymaga:** R1. **Nie rusza:** równań Maxwella (Dodatek A), polaryzacji przez rozpraszanie (R13) i odbicie (R18) — tylko zapowiedź; dipola (R8).
- **(g) Linki:** Dodatek A; Tom 2, Dodatek AB `../../tom2/dodatki/dodatek-ab-filtry.html`; Tom 2, Rozdział 3.
- **(h) Z praktyki:** polaryzator na obiektywie zdejmuje odblask na planie; w compie nie da się go zdjąć po fakcie, w renderze masz AOV specular.

### R3 · Faza i dodawanie fal · `rozdzial-03-faza-i-dodawanie-fal`
- **(a) Pytanie:** co się dzieje, gdy spotykają się dwie fale? Po lekturze dodajesz fale fazorami i odróżniasz sumę spójną od niespójnej. To narzędzie do R12, R13 i R15.
- **Nowe pojęcia (3):** faza jako kąt (fazor) · dodawanie fazorów · spójne kontra niespójne.
- **(b) Sekcje:**
  1. *Co widzisz:* zmarszczki na wodzie przechodzące przez siebie, prążki dwóch źródeł. Faza jako kąt obracającej się strzałki; Δφ = 2πΔs/λ.
  2. *Dodawanie:* w fazie 2×, w przeciwfazie 0, pod 90° √2. **Mała strzałka pod 90° do dużej głównie obraca sumę** — pokaż wprost, R15 z tego korzysta.
  3. *Spójne kontra niespójne:* stała różnica faz → dodajesz amplitudy (I ∝ N²); losowa → natężenia (I ∝ N). Światło naturalne jest niespójne.
- **Zaawansowane:** „Energia nie znika w przeciwfazie” (gdzie się przenosi).
- **(c) Wzory:** Δφ = 2π·Δs/λ; I = A₁² + A₂² + 2A₁A₂cos Δφ; I_spójne ∝ N², I_niespójne ∝ N.
- **(d) Wizualizacje:**
  - SVG+slider: fazor i jego rzut-sinusoida.
  - SVG+slider: dwie sinusoidy z suwakiem przesunięcia, suma + fazory.
  - SVG+slider: duży fazor + mały, suwak kąta; odczyt obrotu i długości sumy.
  - Canvas2D: suma N fazorów o losowych kontra równych fazach, wykres I(N).
  - Canvas2D (opcjonalna): dwa źródła punktowe, mapa prążków.
- **(e) Mity:** „w przeciwfazie energia znika”; „interferencja to rzadkość laboratoryjna” (dzieje się w każdym szkle).
- **(f) Wymaga:** R1, R2. **Nie rusza:** cienkich warstw i koloru strukturalnego (R22; powłoki Tom 2, Rozdział 24), dyfrakcji (Tom 2, Rozdział 10). Bez notacji zespolonej — tylko link do primera.
- **(g) Linki:** `../matematyka/podstawy-matematyczne.html`; Tom 2, Rozdział 10; Tom 2, Rozdział 24. Brak dodatku (zamierzone).
- **(h) Z praktyki:** renderer sumuje radiancje i to działa, bo światło w scenie jest niespójne; wyjątek to cienka warstwa (shader thin-film).

---

## Część II — Z czego zbudowana jest materia (R4–R7)

Zasada części: chemia **jakościowo poprawna, bez formalizmu kwantowego**. Bez funkcji falowej,
Schrödingera i liczb kwantowych l, m. Orbitale jako chmury, zakaz Pauliego słownie, powłoki,
walencja, typy wiązań, pasma i przerwa. Układ 2–8–8 dozwolony z zastrzeżeniem, że od potasu
robi się bardziej złożony. Recenzja sprawdzi liczby elektronów i geometrie.

### R4 · Atom: jądro, elektrony i dlaczego pierwiastki się różnią · `rozdzial-04-atom`
- **(a) Pytanie:** z czego jest atom i dlaczego pierwiastki różnie reagują na światło? Po lekturze wiesz, że Z wyznacza pierwiastek, elektrony siedzą na poziomach w eV, a przejścia dają linie widmowe.
- **Nowe pojęcia (4):** jądro i Z · orbital jako chmura + Pauli + powłoki · poziom energii i przejście · elektrony walencyjne.
- **(b) Sekcje:**
  1. *Co widzisz:* lampa sodowa, neon, ciemne linie w widmie Słońca. Budowa: jądro 10⁻¹⁵ m, chmura 10⁻¹⁰ m, protony wyznaczają pierwiastek.
  2. *Chmury i powłoki:* orbital jako chmura, najwyżej dwa elektrony na orbital, H(1), C(2,4), N(2,5), O(2,6), Ne(2,8), Na(2,8,1), Cl(2,8,7). Dlaczego nie tor Bohra.
  3. *Poziomy i linie:* foton = różnica poziomów; emisja i absorpcja tych samych linii; sód 589 nm = 2,1 eV.
  4. *Układ okresowy jako mapa walencji:* gaz szlachetny (pełna powłoka), metal alkaliczny (jeden luźny elektron), węgiel (cztery). Zapowiedź R5 i R20.
- **Zaawansowane:** „Skąd dyskretne poziomy” (fala uwięziona, jakościowo; szczegóły w Dodatku K).
- **(c) Wzory:** E_γ = E_wyższy − E_niższy = hc/λ.
- **(d) Wizualizacje:**
  - **sky3d #2:** orbitale jako chmury punktów, przełącznik H / C / Na.
  - SVG+slider: drabina poziomów sodu; wybór przejścia → linia w widmie i jej λ.
  - Canvas2D: widmo emisyjne kontra absorpcyjne (te same linie).
  - Static SVG: układ okresowy, okresy 1–3, elektrony walencyjne jako kropki.
  - Static SVG (opcjonalna): skala jądro/atom w dwóch zbliżeniach.
- **(e) Mity:** elektron krąży po torze; elektron „spada na jądro”; atom „pusty”, więc światło przelatuje przez pustkę.
- **(f) Wymaga:** R1. **Nie rusza:** wiązań (R5), pasm (R6), polaryzowalności (R8).
- **(g) Linki:** Dodatek K; https://bartoszskrzypiec.github.io/atmosfera_chmury_book/ (zorza, emisja linii).
- **(h) Z praktyki:** lampa sodowa w nocnej scenie: światło monochromatyczne gasi kolory, a render RGB z „żółtym” światłem ich nie gasi; jak to udać (światło spektralne albo desaturacja).

### R5 · Wiązania: jak z atomów powstają cząsteczki · `rozdzial-05-wiazania`
- **(a) Pytanie:** jak z atomów powstają cząsteczki i kryształy? Po lekturze znasz typy wiązań, ich skalę energii i wiesz, skąd trwały dipol wody.
- **Nowe pojęcia (4):** wiązanie jako obniżenie energii · kowalencyjne / jonowe / metaliczne · słabe (wodorowe, van der Waalsa) · biegunowość cząsteczki.
- **(b) Sekcje:**
  1. *Co widzisz:* sól, cukier, woda, powietrze — kilka pierwiastków, zupełnie różne rzeczy. Atomy łączą się, bo razem mają niższą energię.
  2. *Silne wiązania:* kowalencyjne (H₂, O₂ podwójne, N₂ potrójne, C–H, O–H), jonowe (NaCl), metaliczne (wspólna pula, zapowiedź R20).
  3. *Słabe wiązania i skala:* wodorowe (woda, celuloza, keratyna), van der Waalsa. O–H 4,8 eV, wodorowe 0,2 eV, foton 1,65–3,26 eV.
  4. *Kształt i biegunowość:* H₂O zgięta 104,5° → trwały dipol; CO₂ liniowa → brak; CH₄ tetraedr.
- **Zaawansowane:** „Czy światło zrywa wiązania” (tylko UV i tylko niektóre; zapowiedź żółknięcia w R24).
- **(c) Wzory:** brak.
- **(d) Wizualizacje:**
  - **sky3d #3:** H₂O, CO₂, CH₄, NH₃ z wektorem momentu dipolowego.
  - Static SVG: krzywa energii dwóch atomów w funkcji odległości (dołek).
  - Static SVG: typy wiązań schematycznie (para wspólna, przekazany elektron, morze elektronów, mostek H).
  - SVG+slider: drabina energii (log): wiązania kontra fotony widzialne.
  - Static SVG (opcjonalna): mostki wodorowe w wodzie ciekłej.
- **(e) Mity:** wiązanie jako patyczek; jonowe i kowalencyjne jako rozłączne światy.
- **(f) Wymaga:** R4. **Nie rusza:** ciał stałych i pasm (R6), chemii węgla (R7), dipola indukowanego (R8), drgań cząsteczek (R9, R19).
- **(g) Linki:** Dodatek L.
- **(h) Z praktyki:** olej i woda w symulacji to dwie fazy o różnym IOR (1,47 i 1,33); emulsja wygląda mlecznie z powodu granic (zapowiedź R14).

### R6 · Od cząsteczki do ciała stałego · `rozdzial-06-od-czasteczki-do-ciala-stalego`
- **(a) Pytanie:** co się dzieje z poziomami, gdy atomów jest 10²³? Po lekturze rozumiesz pasma i przerwę i klasyfikujesz materiał, porównując E_g z 1,65–3,26 eV.
- **Nowe pojęcia (3):** stany uporządkowania (kryształ, szkło, polimer) · pasmo z poziomów · przerwa energetyczna i krawędź absorpcji.
- **(b) Sekcje:**
  1. *Co widzisz:* kwarc przezroczysty, krzem szary jak metal, siarczek kadmu żółty. Uporządkowanie: gaz, ciecz, kryształ, szkło amorficzne, polimer, metal.
  2. *Z poziomów pasma:* 2 atomy → 2 poziomy, N → pasmo; pasmo walencyjne, przewodnictwa, przerwa.
  3. *Przerwa decyduje:* izolator (E_g > 3,26 eV, przezroczysty), półprzewodnik (E_g w widzialnym: kolor albo czerń), metal (bez przerwy, R20). Foton pochłonięty, gdy E_γ ≥ E_g.
- **Zaawansowane:** „Szkło nie płynie” (mit witraży).
- **(c) Wzory:** λ_krawędzi ≈ 1240/E_g[eV] nm.
- **(d) Wizualizacje:**
  - SVG+slider: poziomy rozszczepiające się w pasmo przy 2, 4, 8…N atomach.
  - SVG+slider: diagram pasm z suwakiem E_g; pasek widma i kolor wynikowy (raster).
  - Static SVG: rozkład atomów w krysztale, szkle, polimerze, gazie.
  - Static SVG: oś E_g z materiałami z 0.6 i pasmem widzialnym.
  - Static SVG (opcjonalna): izolator / półprzewodnik / metal — trzy diagramy pasm obok siebie.
- **(e) Mity:** szkło płynie; „amorficzne = chaotyczne jak gaz”; „przezroczyste, bo przez pustkę”.
- **(f) Wymaga:** R4, R5. **Nie rusza:** koloru z przerwy i pigmentów (R22), Drudego (R20), wyprowadzenia pasm (Dodatek K).
- **(g) Linki:** Dodatek K; Tom 2, Rozdział 27 (krzem w matrycy, E_g 1,1 eV).
- **(h) Z praktyki:** matryca krzemowa widzi do ok. 1100 nm, oko do 750 nm; stąd filtr IR-cut i „fioletowa czerń” syntetyków pod IRND.

### R7 · Chemia węgla · `rozdzial-07-chemia-wegla`
- **(a) Pytanie:** dlaczego większość cząsteczek organicznych jest bezbarwna, a niektóre intensywnie kolorowe? Po lekturze rozpoznajesz łańcuch, pierścień i wiązanie sprzężone i wiesz, że dłuższe sprzężenie przesuwa absorpcję ku czerwieni.
- **Nowe pojęcia (3):** szkielet węglowy (łańcuch, pierścień) · wiązanie sprzężone · długość sprzężenia → kolor.
- **(b) Sekcje:**
  1. *Co widzisz:* parafina biała, marchew pomarańczowa, liść zielony, krew czerwona. Węgiel ma cztery wiązania: łańcuchy (polietylen), pierścienie (benzen).
  2. *Sprzężenie:* naprzemienne pojedyncze i podwójne; elektrony rozmyte po całym ciągu. Obraz fali w pudełku: dłuższe pudełko → mniejszy odstęp → dłuższa fala pochłonięta.
  3. *Liczby i galeria:* krótki ciąg → UV (bezbarwne); β-karoten, 11 wiązań → pochłania 450–480 nm → pomarańczowy; pierścienie porfirynowe (hem, chlorofil). Po jednym zdaniu: celuloza, lignina, polietylen, keratyna, kolagen, melanina z odsyłaczami do R22–R25.
- **Zaawansowane:** brak (galerię rozwija Dodatek L).
- **(c) Wzory:** brak (E ∝ 1/L² tylko w Dodatku K).
- **(d) Wizualizacje:**
  - Static SVG: łańcuch polietylenu i pierścień benzenu.
  - SVG+slider: liczba C=C → odstęp poziomów → λ absorpcji → kolor (raster); adnotacja „model uproszczony”.
  - Static SVG: β-karoten z wyróżnionym ciągiem sprzężonym.
  - Static SVG: pierścień porfirynowy z Fe (hem) i z Mg (chlorofil).
  - Static SVG (opcjonalna): galeria miniatur „bezbarwna / barwna”.
- **(e) Mity:** „organiczne = kolorowe”; kolor hemoglobiny „od żelaza” (głównie od pierścienia sprzężonego); orbitale π dosłownie.
- **(f) Wymaga:** R4–R6. **Nie rusza:** barwników i pigmentów (R22), skóry, włosów, liści (R25), drewna i papieru (R24), absorpcji w liczbach (R17).
- **(g) Linki:** Dodatek L, Dodatek K.
- **(h) Z praktyki:** maska „wieku” plastiku lub papieru powinna przesuwać kolor ku żółci (pochłaniany niebieski), a nie tylko przyciemniać.

---

## Część III — Materia, która drga (R8–R10)

### R8 · Dipol i polaryzowalność · `rozdzial-08-dipol-i-polaryzowalnosc`
- **(a) Pytanie:** co pole E robi z pojedynczą cząsteczką? Po lekturze wiesz, że pole przesuwa chmurę względem jądra (dipol indukowany p = αE), i masz model elektronu na sprężynie.
- **Nowe pojęcia (3):** dipol (trwały / indukowany) · model sprężyny · polaryzowalność α.
- **(b) Sekcje:**
  1. *Co widzisz:* potarty balon przyciąga obojętne skrawki papieru, bo pole robi z nich dipole. Dipol: ±q w odległości d.
  2. *Sprężyna:* siła jądra przywraca chmurę, przesunięcie ≪ 0,1 nm. Jądro stoi, bo jest 1836× cięższe. To przybliżenie, które działa (powiedz dlaczego: małe wychylenia).
  3. *Polaryzowalność:* miękkie i twarde chmury; większe, luźniejsze → większe α (N₂ 1,7·10⁻³⁰ m³). Pole światła zmienia się co 1,8 fs, więc sprężyna musi nadążać (zapowiedź R9).
- **Zaawansowane:** brak.
- **(c) Wzory:** p = q·d; p = α·E; F = −K·x (K sztywność, x wychylenie).
- **(d) Wizualizacje:**
  - SVG+slider: atom w polu E, suwak E przesuwa chmurę, strzałka p.
  - Static SVG: dipol trwały kontra indukowany.
  - Canvas2D: masa na sprężynie obok atomu przy wolno zmiennym polu.
  - Static SVG: słupki α dla kilku atomów i cząsteczek (rząd wielkości).
  - Static SVG (opcjonalna): skala przesunięcia w powiększeniu.
- **(e) Mity:** „elektron odrywa się od atomu”; model sprężyny jako dosłowna budowa.
- **(f) Wymaga:** R2, R4, R5. **Nie rusza:** rezonansu i fazy (R9), gęstości i P (R10), promieniowania (R11).
- **(g) Linki:** Dodatek B.
- **(h) Z praktyki:** wysoki IOR materiału (flint z ołowiem, TiO₂, diament) to makroskopowe echo dużej α — zapowiedź kolejnych części.

### R9 · Oscylator, rezonans i faza · `rozdzial-09-oscylator-rezonans-faza`
- **(a) Pytanie:** jak elektron odpowiada na pole, które drga szybko? Po lekturze znasz krzywą rezonansową (amplituda i faza w funkcji ω/ω₀), rolę γ i wiesz, gdzie leżą rezonanse (UV elektronowe, IR drgania).
- **Nowe pojęcia (3):** rezonans ω₀ · faza odpowiedzi (w fazie → 90° → przeciwfaza) · tłumienie γ jako pochłanianie.
- **(b) Sekcje:**
  1. *Co widzisz:* huśtawka, kieliszek od dźwięku. Poniżej rezonansu: odpowiedź w fazie, amplituda prawie stała (ogniwo 1 z 0.8).
  2. *Rezonans i powyżej:* przy ω₀ duża amplituda, 90° za siłą, energia idzie w ciepło przez γ; powyżej przeciwfaza i amplituda ∝ 1/ω².
  3. *Gdzie są rezonanse:* elektronowe w UV (szkło, woda: dlatego przezroczyste), w widzialnym dla chromoforów, drgania atomów w IR (O–H, Si–O). Materiał to zestaw oscylatorów.
- **Zaawansowane:** „Postać zespolona odpowiedzi” (jedna liczba zespolona = amplituda i faza; link Dodatek B i primer).
- **(c) Wzory:** x₀(ω) = (eE₀/mₑ)/√((ω₀² − ω²)² + γ²ω²); tg φ = γω/(ω₀² − ω²).
- **(d) Wizualizacje:**
  - SVG+slider: amplituda i faza w funkcji ω/ω₀, suwak γ.
  - Canvas2D: animowany oscylator i siła, suwak ω — zmiana fazy na żywo.
  - SVG+slider: moc pochłaniana w funkcji ω (pik, violet).
  - Static SVG: oś od IR do UV z rezonansami wody, szkła i chromoforu.
  - SVG+slider (opcjonalna): dwa sinusy (siła amber, ruch cyan) z odczytem φ.
- **(e) Mity:** „przy rezonansie najsilniej promieniuje wstecz” bez strat (dominuje pochłanianie); „szkło przezroczyste, bo nie ma rezonansów” (ma, w UV i IR).
- **(f) Wymaga:** R8. **Nie rusza:** n i dyspersji (R15, R16), κ (R17), promieniowania (R11). Tylko zapowiedź: „ta faza da n”.
- **(g) Linki:** Dodatek B; primer.
- **(h) Z praktyki:** tabele IOR podają wartość „przy 589 nm”, bo n zależy od odległości od rezonansu; stały IOR w shaderze ignoruje ten ogon.

### R10 · Polaryzacja materii · `rozdzial-10-polaryzacja-materii`
- **(a) Pytanie:** jak z dipoli pojedynczych cząsteczek zrobić wielkość makro? Po lekturze znasz P = NαE, εᵣ = n² i rozumiesz, dlaczego gęstsze znaczy wyższe n.
- **Nowe pojęcia (3):** polaryzacja ośrodka P · przenikalność εᵣ i εᵣ = n² · pole lokalne (słownie).
- **(b) Sekcje:**
  1. *Co widzisz:* powietrze nad gorącym asfaltem faluje, miraż. P = N·p: ośrodek jako morze dipoli drgających razem.
  2. *Od P do n:* εᵣ = 1 + χ, n = √εᵣ; powietrze: N·α → n − 1 ≈ 3·10⁻⁴ (sprawdzenie rzędu wielkości).
  3. *Gęste ośrodki i woda:* w cieczy dipol czuje pole sąsiadów (pole lokalne, słownie → Dodatek C). Woda ma εᵣ ≈ 80 statycznie, ale przy częstości światła trwałe dipole nie nadążają: n² ≈ 1,78.
- **Zaawansowane:** „Clausius–Mossotti jednym wzorem” (wynik, bez wyprowadzenia).
- **(c) Wzory:** P = N·α·E; εᵣ = 1 + Nα/ε₀; n = √εᵣ; gaz: n ≈ 1 + Nα/(2ε₀).
- **(d) Wizualizacje:**
  - SVG+slider: siatka dipoli, suwaki N i E, odczyt P.
  - SVG+slider: n w funkcji gęstości — wzór liniowy kontra z polem lokalnym.
  - Static SVG: woda — trwałe dipole obracają się w polu statycznym, nie nadążają przy 10¹⁴ Hz.
  - Canvas2D: miraż, gradient n zakrzywia promień.
  - Static SVG (opcjonalna): dipol czuje pole sąsiadów.
- **(e) Mity:** „n wody 1,33, bo woda ciężka”; εᵣ = 80 nie znaczy n ≈ 9.
- **(f) Wymaga:** R8, R9. **Nie rusza:** mechanizmu spowolnienia (R15), dyspersji (R16).
- **(g) Linki:** Dodatek C; https://bartoszskrzypiec.github.io/atmosfera_chmury_book/ (miraże).
- **(h) Z praktyki:** heat haze w compie: zniekształcenie z gradientu n, najsilniejsze przy horyzoncie i nad asfaltem; STMapa z szumu o anizotropii poziomej.

---

## Część IV — Jedna cząsteczka, wiele cząsteczek (R11–R14)

### R11 · Dipol promieniuje · `rozdzial-11-dipol-promieniuje`
- **(a) Pytanie:** co drgający elektron robi z otoczeniem? Po lekturze wiesz, że dipol jest anteną: ta sama częstotliwość, rozkład sin²θ z ciemną osią, moc ∝ ω⁴x².
- **Nowe pojęcia (3):** promieniowanie przyspieszanego ładunku · rozkład sin²θ · moc ∝ ω⁴.
- **(b) Sekcje:**
  1. *Co widzisz:* antena radiowa to ta sama fizyka. Przyspieszany ładunek promieniuje, zmiana pola biegnie z c (opóźnienie r/c).
  2. *Kształt:* pączek, najsilniej prostopadle do osi drgań, zero wzdłuż; fala rozproszona spolaryzowana wzdłuż rzutu osi.
  3. *Moc i rozpraszanie:* moc ∝ (przyspieszenie)² ∝ ω⁴x². Rozpraszanie = pole pada → elektron drga → promieniuje z tą samą częstotliwością i fazą ruchu (ogniwo 2). Pełne λ⁻⁴ dopiero w R13.
- **Zaawansowane:** „Rozpraszanie to nie fluorescencja” (brak realnego przejścia, częstotliwość zachowana).
- **(c) Wzory:** I(θ) ∝ sin²θ (θ od osi drgań); P_rad ∝ ω⁴p₀² (p₀ amplituda momentu).
- **(d) Wizualizacje:**
  - **sky3d #4:** pączek promieniowania, oś drgań, suwak ω.
  - Canvas2D: fronty fali od drgającego ładunku, jasność ∝ sin²θ.
  - Static SVG: pole pada → elektron → fala rozproszona.
  - SVG+slider: moc w funkcji ω przy stałej amplitudzie (log–log, nachylenie 4).
  - SVG+slider (opcjonalna): wykres biegunowy sin²θ.
- **(e) Mity:** rozpraszanie jako odbicie kulki; „cząsteczka pochłania foton i wysyła inny”.
- **(f) Wymaga:** R2, R3, R9. **Nie rusza:** sumowania wielu dipoli (R12), nieba i λ⁻⁴ (R13).
- **(g) Linki:** Dodatek D.
- **(h) Z praktyki:** „izotropowe” rozpraszanie w volume shaderze to przybliżenie; nawet jedna cząsteczka ma rozkład (1 + cos²θ) dla światła niespolaryzowanego.

### R12 · Interferencja wielu dipoli · `rozdzial-12-interferencja-wielu-dipoli`
- **(a) Pytanie:** skoro każda cząsteczka rozprasza, dlaczego szkło jest przezroczyste? Po lekturze rozumiesz znoszenie w bok w ośrodku jednorodnym, sumowanie do przodu i to, że rozprasza **niejednorodność**.
- **Nowe pojęcia (3):** sumowanie do przodu / znoszenie w bok · porządek kontra fluktuacje · niejednorodność rozprasza (index matching).
- **(b) Sekcje:**
  1. *Co widzisz:* szyba przezroczysta, szkło zmielone białe; czysta woda kontra mleko. Dwa dipole, rząd, płaszczyzna: w bok fazy się znoszą, do przodu drogi są równe.
  2. *Warstwa do przodu:* suma warstwy opóźniona o 90° (ogniwo 3), jakościowo przez strefy.
  3. *Porządek i nieporządek:* gęsty jednorodny ośrodek prawie nie rozprasza w bok; gaz ma losowe położenia → natężenia się sumują → rozprasza (dla R13). Granice, pęcherzyki, ziarna rozpraszają; dopasowanie n (bagietka w oleju znika).
- **Zaawansowane:** „Gdy odstęp jest rzędu λ” (siatka, kryształy dla promieni X, opal; zapowiedź R22).
- **(c) Wzory:** spójne I ∝ N², niespójne I ∝ N (przywołanie z R3).
- **(d) Wizualizacje:**
  - Canvas2D: dipole na płaszczyźnie, mapa fali rozproszonej; przełącznik uporządkowane / losowe.
  - SVG+slider: fazory z kilku dipoli, suwak kąta obserwacji.
  - Static SVG: strefy Fresnela na warstwie → suma opóźniona o 90°.
  - SVG+slider: szkło lite → kruszone (liczba granic); przezroczystość spada, biel rośnie (raster).
  - Static SVG (opcjonalna): bagietka szklana znika w oleju o n = 1,52.
- **(e) Mity:** „przezroczyste = nie oddziałuje”; „gęstsze rozprasza więcej” (na cząsteczkę mniej niż gaz).
- **(f) Wymaga:** R3, R11. **Nie rusza:** n ilościowo (R15), λ⁻⁴ (R13), Mie (R14), Fresnela (R18).
- **(g) Linki:** Dodatek F; Tom 2, Rozdział 10.
- **(h) Z praktyki:** szkło to BSDF powierzchni, a śnieg, cukier i mleko to objętość; granica zależy od rozmiaru niejednorodności względem λ i względem piksela.

### R13 · Rayleigh: λ⁻⁴ z mechanizmu · `rozdzial-13-rayleigh`
- **(a) Pytanie:** dlaczego małe cząstki rozpraszają niebieski mocniej i dlaczego niebo jest niebieskie i spolaryzowane? Po lekturze składasz λ⁻⁴ z R9 i R11, liczysz 5,9× i wyjaśniasz, czemu niebo nie jest fioletowe.
- **Nowe pojęcia (3):** prawo λ⁻⁴ · polaryzacja przez rozpraszanie (90°) · warunek „cząstka ≪ λ”.
- **(b) Sekcje:**
  1. *Co widzisz:* niebieskie niebo, polaryzator ciemni niebo pod 90° od Słońca. Złożenie: poniżej rezonansu amplituda stała (R9) × moc ∝ ω⁴ (R11) = λ⁻⁴; gaz sumuje natężenia (R12). Rozpraszają N₂ i O₂, nie kurz.
  2. *Liczby i fiolet:* 450/700 → 5,9×, 400/700 → 9,4×. Niebo nie jest fioletowe: słabszy fiolet w widmie Słońca, słaba czułość oka, mieszanka całego widma.
  3. *Polaryzacja:* pod 90° dipol nie wyśle składowej wzdłuż kierunku obserwacji → światło liniowo spolaryzowane (w praktyce 70–80% przez wielokrotne rozpraszanie). Rozkład (1 + cos²θ).
- **Zaawansowane:** „Przekrój czynny Rayleigha” (C_sca = (8π/3)k⁴α_V² jako wynik; wyprowadzenie w Dodatku D).
- **(c) Wzory:** I ∝ λ⁻⁴; I(θ) ∝ 1 + cos²θ.
- **(d) Wizualizacje:**
  - **sky3d #5:** kopuła nieba z wektorami polaryzacji, ruchome Słońce.
  - SVG+slider: widmo Słońca × λ⁻ᵖ × czułość oka → kolor (raster); suwak wykładnika 0…4.
  - Static SVG: łańcuch „amplituda stała × ω⁴ = λ⁻⁴”.
  - Static SVG: geometria polaryzacji pod 90°.
  - SVG+slider (opcjonalna): wykres biegunowy (1 + cos²θ) ze składowymi.
- **(e) Mity:** kurz, odbicie oceanu, „powietrze jest niebieskie”; „rozprasza para wodna”; „powinno być fioletowe, więc teoria zła”.
- **(f) Wymaga:** R9, R11, R12. **Nie rusza:** Mie (R14), zachodu, horyzontu, perspektywy powietrznej (R26 — tylko zapowiedź), kryterium Rayleigha (Tom 2, Rozdział 10 — jedno zdanie: ten sam lord, inna rzecz).
- **(g) Linki:** Dodatek D; https://bartoszskrzypiec.github.io/atmosfera_chmury_book/ (niebo jako zjawisko); Tom 2, Dodatek AB.
- **(h) Z praktyki:** polaryzator na plate ciemni niebo tylko w pasie 90° od Słońca, więc przy szerokim kącie niebo wychodzi nierówne; jak to odtworzyć w sky dome.

### R14 · Mie: kiedy cząstka dorasta do fali · `rozdzial-14-mie`
- **(a) Pytanie:** co się dzieje, gdy cząstka jest porównywalna z falą lub większa? Po lekturze znasz x = 2πa/λ, trzy reżimy, płat do przodu i neutralność barwną dużych cząstek, i łączysz g z anizotropią volume shadera.
- **Nowe pojęcia (3):** parametr rozmiaru x i trzy reżimy · rozpraszanie do przodu (g) · neutralność barwna dużych cząstek.
- **(b) Sekcje:**
  1. *Co widzisz:* biała chmura, mleko, jasna aureola wokół Słońca za mgiełką. x ≪ 1 Rayleigh, x ≈ 1–10 rezonanse, x ≫ 1 optyka geometryczna + dyfrakcja.
  2. *Dlaczego do przodu:* dipole wewnątrz cząstki (R12 w małej skali): do przodu drogi się wyrównują. g ≈ 0,85 dla kropel chmury.
  3. *Dlaczego bez koloru:* dla x ≫ 1 sprawność Q prawie nie zależy od λ, kropla 10 µm rozprasza wszystkie barwy tak samo. Dym 0,1–1 µm jest pośrodku (zapowiedź R26).
- **Zaawansowane:** „Paradoks Q → 2” (cień + dyfrakcja; liczby w Dodatku E).
- **(c) Wzory:** x = 2πa/λ; Q = C/(πa²); g = ⟨cos θ⟩; Henyey–Greenstein p(θ) = (1 − g²)/(4π(1 + g² − 2g cos θ)^{3/2}) jako przybliżenie używane przez renderery.
- **(d) Wizualizacje:**
  - **sky3d #6:** funkcja fazowa jako bryła, suwak x od 0,1 do 50.
  - SVG+slider: Q_ext(x) z tętnieniami; znaczniki dymu, mgły, chmury.
  - SVG+slider: HG kontra kształt Mie (dane uproszczone z Dodatku E), suwak g.
  - Canvas2D: woda z rosnącą ilością mleka: rudawa w przejściu i niebieskawa w bok przy małym stężeniu, potem biała.
  - Static SVG (opcjonalna): trzy reżimy z przykładami (N₂, dym, kropla).
- **(e) Mity:** duża cząstka jako lustro lub kula bilardowa; „chmura biała, bo woda biała”; Mie jako „inna fizyka” niż Rayleigh.
- **(f) Wymaga:** R3, R11–R13. **Nie rusza:** chmur i atmosfery (R26), tęczy (R27 — wzmianka), TiO₂ (R22, R23 — tylko jako przykład x ≈ 1).
- **(g) Linki:** Dodatek E; https://bartoszskrzypiec.github.io/atmosfera_chmury_book/ ; Tom 2, Rozdział 22 (veiling glare, filtr dyfuzyjny); Tom 2, Rozdział 28 (halacja); https://bartoszskrzypiec.github.io/raytracing-book/ (funkcje fazowe).
- **(h) Z praktyki:** anisotropy w volume shaderze: chmura ≈ 0,85, mgła 0,7–0,8, dym 0,3–0,6; jasna krawędź chmury pod światło wymaga dużego g.

---

## Część V — Od cząsteczki do materiału (R15–R18)

### R15 · Załamanie i n: skąd wolniejsza fala · `rozdzial-15-zalamanie-skad-wolniejsza-fala`
- **(a) Pytanie:** dlaczego światło w szkle „zwalnia”? Po lekturze znasz poprawny mechanizm (fala padająca + spóźniona fala elektronów), obalasz mit pochłoń-i-wyślij i wiesz, co się zmienia (λ, faza), a co nie (f).
- **Nowe pojęcia (3):** n jako opóźnienie fazy z sumy fal · wygaszanie fali padającej (Ewald–Oseen, obrazem) · prędkość fazowa c/n przy stałym f.
- **(b) Sekcje:**
  1. *Co widzisz i mit:* łyżeczka „złamana” w wodzie. Popularne „pochłonięte i ponownie wypromieniowane” nazwane wprost, z uwagą, że Tom 2, Rozdział 2 też je prostuje. Trzy powody, dla których to złe: pochłanianie wymaga rezonansu (szkło nie ma go w widzialnym), ponowna emisja szłaby w losowym kierunku i czasie, opóźnienie nie zależałoby tak od λ.
  2. *Mechanizm:* ogniwa 1–4 z 0.8 fazorami; warstwa po warstwie opóźnienie rośnie → c/n. Ewald–Oseen obrazem: fala padająca wciąż biegnie z c, ale fala elektronów wygasza ją na głębokości rzędu λ i zastępuje wolniejszą.
  3. *Co się zmienia:* λ → λ/n, f bez zmian (kolor pod wodą ten sam), załamanie z ciągłości frontów; Snell tylko jako wynik (wyprowadzenie Tom 2, Rozdział 2 i Dodatek A T2).
- **Zaawansowane:** „n mniejsze od jedności” (powyżej rezonansu, promienie X, prędkość fazowa > c, prędkość grupowa jednym zdaniem).
- **(c) Wzory:** v = c/n; λ_ośr = λ/n; n₁sin θ₁ = n₂sin θ₂ (cytat).
- **(d) Wizualizacje:**
  - SVG+slider: fazor fali padającej + fazor warstwy (90°), suwak liczby warstw.
  - Canvas2D: fala padająca, fala elektronów i suma wchodzące w płytkę; suwak n.
  - Canvas2D: wygaszanie fali padającej w głąb na kilku λ (Ewald–Oseen).
  - Static SVG: trzy panele „dlaczego nie pochłoń-i-wyślij”.
  - Static SVG (opcjonalna): λ skraca się, f zostaje.
- **(e) Mity:** pochłoń-i-wyślij; odbijanie między atomami; zmiana koloru/częstotliwości w szkle; „n < 1 niemożliwe”.
- **(f) Wymaga:** R3, R9–R12. **Nie rusza:** n(λ) (R16), absorpcji (R17), odbicia (R18), Snella w liczbach i aberracji (Tom 2).
- **(g) Linki:** Dodatek F, Dodatek C; Tom 2, Rozdział 2; Tom 2, Dodatek A; https://bartoszskrzypiec.github.io/raytracing-book/
- **(h) Z praktyki:** IOR w shaderze to tylko stosunek prędkości fazowych, renderer nie spowalnia promienia; woda o IOR 1,33 nie zmienia koloru, ale głęboka woda już tak (absorpcja, R17, R19).

### R16 · Dyspersja: n(λ) jako ogon rezonansu · `rozdzial-16-dyspersja`
- **(a) Pytanie:** dlaczego n zależy od koloru? Po lekturze widzisz krzywą n(ω) jako ogon rezonansu, wiesz, czemu flint ma wyższe n i większą dyspersję, i czym jest wzór Sellmeiera.
- **Nowe pojęcia (3):** n(λ) jako ogon rezonansu · dyspersja normalna / anomalna · Sellmeier jako suma oscylatorów.
- **(b) Sekcje:**
  1. *Co widzisz:* pryzmat, „ogień” diamentu. Ogon rezonansu (ogniwo 5): niebieski bliżej rezonansu UV, więc większe n; rezonanse IR ciągną n w dół na czerwonym końcu.
  2. *Kształt krzywej:* dyspersja normalna w oknie przezroczystości, anomalna w paśmie absorpcji (zapowiedź związku z κ, R17). Szkła: crown 1,52, flint (ołów, tytan: rezonans bliżej → wyższe n, większa dyspersja), diament 2,42, woda 1,331–1,343.
  3. *Sellmeier:* suma ułamków, bo suma ogonów oscylatorów; Cauchy jako przybliżenie. Liczba Abbego: wzmianka + link Tom 2.
- **Zaawansowane:** brak.
- **(c) Wzory:** n²(λ) = 1 + Σ Bᵢλ²/(λ² − Cᵢ) (Cᵢ kwadrat λ rezonansu, Bᵢ siła oscylatora); n ≈ A + B/λ² (Cauchy).
- **(d) Wizualizacje:**
  - SVG+slider: n(ω) i κ(ω) wokół jednego rezonansu, suwak ω₀, zaznaczone okno widzialne.
  - SVG+slider: dwa rezonanse (UV + IR) → n(λ) w widzialnym.
  - Canvas2D: pryzmat, suwak n i dyspersji.
  - Static SVG: n(λ) wody, BK7, flintu, diamentu (Dodatek I).
  - SVG+slider (opcjonalna): Sellmeier — dodawanie kolejnych składników.
- **(e) Mity:** dyspersja jako wada szkła; „niebieski zwalnia, bo ma więcej energii”.
- **(f) Wymaga:** R9, R15. **Nie rusza:** κ ilościowo (R17), tęczy (R27), aberracji chromatycznej (Tom 2, Rozdział 14), Abbego w liczbach (Tom 2, Dodatek A).
- **(g) Linki:** Dodatek B, Dodatek I; Tom 2, Rozdział 2; Tom 2, Rozdział 14; Tom 2, Dodatek A; https://bartoszskrzypiec.github.io/raytracing-book/
- **(h) Z praktyki:** ile próbek widma trzeba, żeby „ogień” diamentu nie był trzema pasami RGB; typowa wartość Abbego do suwaka dispersion.

### R17 · Absorpcja i zespolone n · `rozdzial-17-absorpcja-i-zespolone-n`
- **(a) Pytanie:** co się dzieje przy rezonansie i jak to zapisać jedną liczbą? Po lekturze znasz ñ = n + iκ, σₐ = 4πκ/λ, prawo Beera–Lamberta i głębokość wnikania.
- **Nowe pojęcia (3):** absorpcja jako odejmowanie fal · ñ = n + iκ · zanik wykładniczy i głębokość wnikania.
- **(b) Sekcje:**
  1. *Co widzisz:* zielony brzeg grubej szyby, woda coraz bardziej niebieska w głąb, wino ciemnieje w grubszym kieliszku. Przy rezonansie fala warstwy jest 180° za padającą i ją odejmuje (ogniwo 6); energia idzie w ciepło.
  2. *Jedna liczba:* strzałka, która się obraca (n) i kurczy (κ); pasmo κ zawsze niesie esowate falowanie n (słownie).
  3. *Beer–Lambert:* zanik wykładniczy, σₐ = 4πκ/λ, δ = λ/(4πκ). Liczby: czerwień w wodzie ≈ 1,5 m, metal ≈ 10 nm. Kolor to to, co zostaje; nasycenie rośnie z grubością.
- **Zaawansowane:** „Kramers–Kronig bez całek” (dlaczego absorpcja i dyspersja są nierozłączne).
- **(c) Wzory:** ñ = n + iκ; I(d) = I₀e^{−σₐd}; σₐ = 4πκ/λ; δ = λ/(4πκ).
- **(d) Wizualizacje:**
  - SVG+slider: fazor fali w ośrodku, suwaki n i κ.
  - SVG+slider: zanik I(d) (violet), suwak σₐ, odczyt δ.
  - Canvas2D: płytka o rosnącej grubości w trzech kanałach → kolor (raster): szkło z żelazem, woda.
  - Static SVG: zanik w metalu (nm) i w wodzie (m) na dwóch skalach.
  - SVG+slider (opcjonalna): widmo absorpcji → widmo przepuszczone → kolor.
- **(e) Mity:** absorpcja jako pochłonięcie i ponowna emisja (wyjątek: fluorescencja, R22); κ jako niezależna własność; κ nazwane „współczynnikiem ekstynkcji” (0.4).
- **(f) Wymaga:** R9, R15, R16. **Nie rusza:** Fresnela dla metali (R18), metalu (R20), chromoforów (R22), wody jako materiału (R19).
- **(g) Linki:** Dodatek H, primer; https://bartoszskrzypiec.github.io/raytracing-book/ (media); https://bartoszskrzypiec.github.io/lookdev-book/
- **(h) Z praktyki:** σₐ = −ln(kolor)/głębokość odniesienia; „transmission color” bez głębokości odniesienia psuje się przy zmianie skali sceny.

### R18 · Granica dwóch ośrodków: Fresnel z mikroskopu · `rozdzial-18-granica-dwoch-osrodkow`
- **(a) Pytanie:** skąd bierze się odbicie i dlaczego metal odbija więcej niż szkło? Po lekturze wiesz, że odbicie to fala wysłana wstecz przez dipole przy granicy, liczysz F₀ z n i κ i wyjaśniasz Brewstera pączkiem dipola.
- **Nowe pojęcia (3):** odbicie jako fala wsteczna dipoli · F₀ z kontrastu n (i κ) · kąt Brewstera.
- **(b) Sekcje:**
  1. *Co widzisz:* szyba odbija słabo na wprost i mocno pod kątem, metal zawsze dużo. Odbicie to fala wsteczna dipoli (ogniwo 8); w głębi się znosi, zostaje wkład przy granicy, więc liczy się kontrast n.
  2. *Ile odbija:* F₀: szkło 4%, woda 2%, diament 17%; dopasowanie n → 0. Metal: duże κ → F₀ > 50%, odbicie kolorowe (zapowiedź R20); dielektryk odbija bez koloru.
  3. *Kąt:* odbicie rośnie ku muskaniu; Brewster: kierunek odbity pokrywa się z osią drgań dipoli → zero dla polaryzacji p (pączek z R11).
- **Zaawansowane:** „Całkowite wewnętrzne odbicie i fala zanikająca” (kąt graniczny 41° dla szkła).
- **(c) Wzory:** F₀ = ((n₁ − n₂)² + κ²)/((n₁ + n₂)² + κ²); tan θ_B = n₂/n₁. Pełne s/p w Dodatku H i Tom 2, Dodatek B; Schlick tylko wzmianka.
- **(d) Wizualizacje:**
  - viz.js: kula dielektryczna kontra metaliczna, suwaki n i κ.
  - SVG+slider: R_s(θ), R_p(θ), suwak n, znacznik Brewstera.
  - Static SVG: dipole przy granicy wysyłają falę wstecz, w głębi znoszenie.
  - Static SVG: Brewster — oś drgań wzdłuż promienia odbitego.
  - SVG+slider (opcjonalna): mapa F₀ w funkcji n i κ z punktami materiałów.
- **(e) Mity:** odbicie „na geometrycznej powierzchni”; „metal błyszczy, bo gładki” (→ R20); Fresnel jako artystyczny rim light.
- **(f) Wymaga:** R3, R11, R15, R17. **Nie rusza:** pełnych wzorów (Tom 2, Rozdział 3; Tom 2, Dodatek B; Dodatek H), powłok (Tom 2, Rozdział 24), koloru metalu (R20), microfacetów (lookdev), mokrych powierzchni (R24).
- **(g) Linki:** Dodatek H, Dodatek J; Tom 2, Rozdział 3; Tom 2, Dodatek B; https://bartoszskrzypiec.github.io/lookdev-book/ ; https://bartoszskrzypiec.github.io/pxrsurface-guide/
- **(h) Z praktyki:** „specular 0,5 = F₀ 4%” — skąd ta konwencja; IOR 1,33 kontra 1,5 to realna różnica (2% kontra 4%), a IOR 3 dla „bardziej błyszczącego plastiku” to fizyczny nonsens.

---

## Część VI — Materiały (R19–R25)

Wspólna metoda części: każdy materiał opisujesz **czterema pytaniami**: (1) gdzie są jego
rezonanse lub przerwa (R6, R9)? (2) czy jest jednorodny w skali λ, czy ma granice (R12, R14)?
(3) co odbija powierzchnia (R18)? (4) co pochłania objętość (R17)? Nie wprowadzaj nowej fizyki —
w tej części „nowe pojęcia” to pojęcia materiałowe. Szczegół shaderowy: link do lookdev/pxrsurface.

### R19 · Gaz, woda, szkło: dlaczego przezroczyste · `rozdzial-19-gaz-woda-szklo`
- **(a) Pytanie:** co musi się zgadzać, żeby materiał był przezroczysty, i skąd bierze się kolor „przezroczystych” w grubości? Po lekturze wymieniasz dwa warunki i wyjaśniasz błękit wody, zieleń szkła, biel śniegu.
- **Nowe pojęcia (3):** okno przezroczystości · biel z granic · kolor z drgań cząsteczek (woda).
- **(b) Sekcje:**
  1. *Co widzisz:* szyba, woda bezbarwna w szklance i niebieska w basenie, śnieg biały, lód przezroczysty. Warunek 1: rezonanse poza widzialnym (szkło E_g ≈ 9 eV, drgania ≈ 9 µm).
  2. *Warunek 2 — jednorodność:* szkło amorficzne, ciecz; pęcherzyki, pęknięcia, kryształki dają biel (śnieg, szron, szkło mleczne).
  3. *Kolor w grubości:* woda niebieska od nadtonów drgań O–H w czerwieni (jedyny powszechny kolor z drgań, nie z elektronów), σₐ ≈ 0,6 1/m przy 700 nm; szkło zielone na brzegu od jonów żelaza.
- **Zaawansowane:** brak.
- **(c) Wzory:** przywołanie I = I₀e^{−σₐd}.
- **(d) Wizualizacje:**
  - Static SVG: okno przezroczystości szkła i wody od UV do IR (pasma absorpcji violet).
  - Canvas2D: głębokość wody → kolor (raster): szklanka 10 cm, basen 2 m, morze 20 m.
  - SVG+slider: lód lity → śnieg (granice na mm), kolor przejścia i odbicia.
  - Static SVG: szyba z boku — droga wzdłuż tafli, zielony brzeg.
  - Static SVG (opcjonalna): widmo absorpcji wody (log) z pasmami O–H.
- **(e) Mity:** „woda niebieska tylko od nieba”; „śnieg biały, bo lód biały”; „bezbarwne = nic nie pochłania”.
- **(f) Wymaga:** R6, R9, R12, R17, R18. **Nie rusza:** plastiku (R23), mokrych powierzchni (R24), chmur i mgły (R26), metalu (R20).
- **(g) Linki:** Dodatek I; https://bartoszskrzypiec.github.io/lookdev-book/ ; https://bartoszskrzypiec.github.io/atmosfera_chmury_book/
- **(h) Z praktyki:** woda w renderze: IOR 1,33 + σₐ(λ) z tabeli daje kolor zależny od głębokości, zamiast barwić refrakcję na niebiesko; śnieg jako objętość z dużym σₛ i prawie zerowym σₐ.

### R20 · Metal: swobodne elektrony, złoto i miedź · `rozdzial-20-metal`
- **(a) Pytanie:** dlaczego metale odbijają prawie wszystko, a złoto i miedź są kolorowe? Po lekturze znasz model elektronów swobodnych, ωₚ, głębokość wnikania ≈ 10 nm i rolę pasma d.
- **Nowe pojęcia (3):** elektrony swobodne (oscylator bez sprężyny) · częstotliwość plazmowa · kolor z przejść z pasma d.
- **(b) Sekcje:**
  1. *Co widzisz:* srebro i aluminium neutralne, złoto żółte, miedź łososiowa; szorstki metal nadal wygląda metalicznie. Elektrony bez sprężyny (ω₀ = 0) odsyłają falę, która wnika tylko na ≈ 10 nm.
  2. *Próg plazmowy:* poniżej ωₚ odbicie, powyżej metal przepuszcza (Al ≈ 15 eV, metale alkaliczne przepuszczają UV).
  3. *Kolor i powierzchnia:* złoto (≈ 2,4 eV) i miedź (≈ 2,1 eV) pochłaniają niebieski przez przejścia z pasma d; srebro ma próg w UV. Szorstkość rozmywa odbicie, nie odbiera metaliczności; metal nie ma dyfuzji podpowierzchniowej; krawędź bieleje przy muskaniu.
- **Zaawansowane:** „Cienka złota folia przepuszcza zieleń” i „patyna to już nie metal” (nowy związek, dielektryk).
- **(c) Wzory:** εᵣ(ω) = 1 − ωₚ²/(ω² + iγω); ωₚ = √(Ne²/(ε₀mₑ)).
- **(d) Wizualizacje:**
  - viz.js: kula metaliczna, presety Ag / Al / Au / Cu / Fe (n, κ z Dodatku I), suwak chropowatości.
  - SVG+slider: R(λ) z Drudego, suwak ωₚ przesuwa próg przez widmo.
  - Static SVG: pasma złota, przeskok z pasma d 2,4 eV.
  - Static SVG: R(λ) srebra, złota, miedzi, aluminium + kolor (raster).
  - SVG+slider (opcjonalna): Fresnel metalu w funkcji kąta (kolor krawędzi).
- **(e) Mity:** „błyszczy, bo polerowany”; złoto żółte od barwnika; „metal ma kolor diffuse”; „rdza to metal”.
- **(f) Wymaga:** R5, R6, R9, R17, R18. **Nie rusza:** wyprowadzenia Drudego (Dodatek G), microfacetów i szczotkowania (lookdev), półprzewodników (R22), sadzy (R21).
- **(g) Linki:** Dodatek G, Dodatek I, Dodatek J; https://bartoszskrzypiec.github.io/lookdev-book/ ; https://bartoszskrzypiec.github.io/pxrsurface-guide/ ; https://bartoszskrzypiec.github.io/raytracing-book/
- **(h) Z praktyki:** complex IOR (n, κ per kanał) kontra „F₀ + edge tint”: skąd obie parametryzacje i gdzie druga gubi fizykę (miedź przy muskaniu).

### R21 · Sadza, węgiel i czerń · `rozdzial-21-sadza-wegiel-czern`
- **(a) Pytanie:** co musi się stać, żeby coś było naprawdę czarne? Po lekturze odróżniasz dwa zadania czerni (pochłonąć całe widmo i nie odbić od powierzchni) i wiesz, czemu sadza jest czarna, a czarny lakier lśni.
- **Nowe pojęcia (3):** absorpcja szerokopasmowa (przerwa ≈ 0) · limit odbicia powierzchni · pułapka geometryczna.
- **(b) Sekcje:**
  1. *Co widzisz:* sadza, węgiel drzewny, czarny lakier (lśni), aksamit (głębszy), grafit (szary połysk). Sieć pierścieni węglowych to sprzężenie bez końca → przerwa ≈ 0 → każdy foton ma dokąd przeskoczyć.
  2. *Powierzchnia wciąż odbija:* czarny plastik F₀ ≈ 4%; mat rozprasza te 4% na boki; grafit w płatkach odbija jak półmetal, sadza w kulkach 20–50 nm tylko pochłania.
  3. *Pułapki:* aksamit, las nanorurek (Vantablack, ≈ 99,96%): każde odbicie zabiera większość, po n odbiciach zostaje Fⁿ.
- **Zaawansowane:** „Płomień świecy jest żółty od rozżarzonej sadzy” (dobry absorber = dobry emiter).
- **(c) Wzory:** R_eff ≈ Fⁿ (F udział odbity w jednym odbiciu, n liczba odbić).
- **(d) Wizualizacje:**
  - viz.js: czarny błyszczący, czarny matowy — czerń też ma speculara.
  - Static SVG: pasma grafitu (brak przerwy) kontra izolator.
  - SVG+slider: pułapka, liczba odbić, pozostałe Fⁿ.
  - Static SVG: morfologia: płatek grafitu, kulki sadzy, las nanorurek.
  - Static SVG (opcjonalna): skala czerni, odbicie w % (log).
- **(e) Mity:** „czarne odbija 0%”; „płomień żółty od gazu”.
- **(f) Wymaga:** R6, R7, R17, R18. **Nie rusza:** pigmentów barwnych (R22), dymu (R26), metalu (R20).
- **(g) Linki:** Dodatek I; https://bartoszskrzypiec.github.io/lookdev-book/
- **(h) Z praktyki:** albedo najczarniejszych realnych materiałów to 0,02–0,04; base color 0 psuje energię sceny; aksamit potrzebuje sheen, nie ciemnego diffuse.

### R22 · Kolor z absorpcji: chromofor, barwnik, pigment · `rozdzial-22-kolor-z-absorpcji`
- **(a) Pytanie:** skąd kolory rzeczy? Po lekturze znasz chemiczne źródła barwnej absorpcji, odróżniasz barwnik od pigmentu i wiesz, jak powstaje kolor strukturalny.
- **Nowe pojęcia (4):** kolor jako to, co zostaje (subtraktywnie) · źródła barwnej absorpcji (sprzężenie, przerwa półprzewodnika) · barwnik kontra pigment · kolor strukturalny.
- **(b) Sekcje:**
  1. *Co widzisz:* pomidor, żółć kadmowa, cynober, bańka mydlana, motyl Morpho. Kolor = widmo po odjęciu pasma absorpcji; mieszanie subtraktywne kontra addytywne.
  2. *Źródła absorpcji:* chromofory sprzężone (R7: karoteny, antocyjany, barwniki azowe); krawędź półprzewodnika: TiO₂ biały, CdS żółty 2,4 eV, HgS czerwony 2,0 eV, CdSe ciemnoczerwony.
  3. *Barwnik i pigment:* barwnik rozpuszczony (tylko absorpcja, przezroczysty); pigment to ziarno o n innym niż spoiwo (absorpcja + rozpraszanie, krycie); rozmiar ziarna zmienia odcień (x z R14).
  4. *Kolor strukturalny:* cienka warstwa (bańka, olej, iryzacja), wielowarstwa (Morpho), quasi-uporządkowana nanostruktura (sójka, niebieska tęczówka — zapowiedź R25). Żadnej barwnej cząsteczki.
- **Zaawansowane:** „Rubin i szmaragd: ten sam jon Cr³⁺” (metale przejściowe) oraz „Fluorescencja: jedyne prawdziwe pochłoń-i-wyślij” (rozjaśniacze; nie ma nic wspólnego z n).
- **(c) Wzory:** λ_krawędzi ≈ 1240/E_g nm; cienka warstwa 2nd·cos θ_t = mλ (wzmocnienie; pełny rachunek z przesunięciem fazy przy odbiciu: Tom 2, Rozdział 24).
- **(d) Wizualizacje:**
  - SVG+slider: pasmo absorpcji (położenie, szerokość) → pozostałe widmo → kolor (raster).
  - SVG+slider: krawędź półprzewodnika, suwak E_g: biały → żółty → pomarańcz → czerwony → czarny.
  - Static SVG: barwnik w roztworze, pigment w spoiwie.
  - Canvas2D: kolor bańki w funkcji grubości i kąta.
  - Static SVG: łuska Morpho (wielowarstwa) i pióro sójki (gąbka).
  - SVG+slider (opcjonalna): mieszanie widm dwóch farb (mnożenie) kontra świateł (dodawanie).
- **(e) Mity:** „kolor to odbita λ”; niebieski pigment w piórach i oczach; „mieszanie farb = mieszanie świateł”.
- **(f) Wymaga:** R3, R6, R7, R14, R17. **Nie rusza:** plastiku, lakieru, farby (R23), drewna i tkanin (R24), melaniny, hemoglobiny, chlorofilu (R25), powłok obiektywu (Tom 2, Rozdział 24), czerni (R21).
- **(g) Linki:** Dodatek L; Tom 2, Rozdział 24; https://bartoszskrzypiec.github.io/lookdev-book/ ; https://bartoszskrzypiec.github.io/raytracing-book/
- **(h) Z praktyki:** multiply dwóch tekstur RGB tylko przybliża mieszanie pigmentów (widma mnożą się per λ); shader thin-film do bańki i oleju.

### R23 · Plastik, lakier, farba · `rozdzial-23-plastik-lakier-farba`
- **(a) Pytanie:** dlaczego kolorowy plastik ma biały odblask, a karoseria dwa odbicia? Po lekturze opisujesz materiał jako spoiwo (n ≈ 1,5) + ziarna + warstwy i wiesz, skąd połysk i mat.
- **Nowe pojęcia (3):** spoiwo + pigment (kolor z objętości, odblask z powierzchni) · warstwa bezbarwna (clear coat) · połysk i mat jako stan powierzchni spoiwa.
- **(b) Sekcje:**
  1. *Co widzisz:* czerwony plastik z białym odblaskiem, mleczny plastik prześwitujący, karoseria z metalikiem. Polimer to dielektryk n ≈ 1,49–1,59, F₀ ≈ 4% bez koloru; amorficzny przezroczysty, półkrystaliczny mleczny (granice krystalitów).
  2. *Kolor z wnętrza:* pigment (TiO₂ n ≈ 2,7, ziarno 0,2–0,3 µm) i barwnik; światło wchodzi, rozprasza się, wraca zabarwione — to „diffuse”.
  3. *Warstwy i farba:* clear coat to druga granica nad bazą (dwa odbicia, baza nasycona i przyciemniona), metalik to płatki aluminium. Farba: spoiwo + pigment + środek matujący; połysk z gładkiego spoiwa, mat z mikroszorstkości. Pigment w oleju ciemniejszy niż suchy proszek (mniejszy kontrast n).
- **Zaawansowane:** „Flop koloru w lakierze metalik” (orientacja płatków).
- **(c) Wzory:** przywołanie F₀ z R18.
- **(d) Wizualizacje:**
  - viz.js: kula plastik kontra lakier dwuwarstwowy.
  - Static SVG: przekrój plastiku z pigmentem: odblask biały z wierzchu, zabarwione światło z wnętrza.
  - Static SVG: przekrój karoserii: podkład, baza, clear coat.
  - SVG+slider: stosunek n pigmentu do n spoiwa → krycie (proszek, olej, akryl).
  - Canvas2D (opcjonalna): mleczny plastik, światło przebijające przez ściankę.
- **(e) Mity:** kolorowy odblask plastiku; „mat to inny materiał”; „lakier tylko błyszczy”.
- **(f) Wymaga:** R7, R12, R14, R17, R18, R22. **Nie rusza:** chemii pigmentów (R22), mokrych materiałów (R24 — tu jedno zdanie), teorii BRDF (lookdev, raytracing).
- **(g) Linki:** Dodatek J; https://bartoszskrzypiec.github.io/lookdev-book/ ; https://bartoszskrzypiec.github.io/pxrsurface-guide/ ; https://bartoszskrzypiec.github.io/raytracing-book/
- **(h) Z praktyki:** karoseria w PxrSurface: baza z płatkami + clearcoat IOR 1,5; sam coat bez nasycenia i przyciemnienia bazy wygląda płasko.

### R24 · Drewno, papier, tkanina · `rozdzial-24-drewno-papier-tkanina`
- **(a) Pytanie:** jak z przezroczystej celulozy powstaje biała kartka, słoje i połysk jedwabiu — i dlaczego mokre ciemnieje? Po lekturze wyjaśniasz biel granicami włókien, żółknięcie ligniną i pełny mechanizm „mokre = ciemniejsze”.
- **Nowe pojęcia (3):** celuloza + lignina · włókno jako źródło bieli i anizotropii · mokre = ciemniejsze.
- **(b) Sekcje:**
  1. *Co widzisz:* biała kartka, tłusta plama prześwituje, żółknące gazety, słoje, lśniący jedwab. Celuloza (n ≈ 1,53) bezbarwna; lignina z pierścieniami aromatycznymi pochłania UV i fiolet → żółto-brązowa, na świetle żółknie i szarzeje.
  2. *Włókna:* papier = sieć włókien + powietrze = biel (wypełniacze CaCO₃, kaolin); drewno = komórki-rurki, ułożone włókna → anizotropowe odbicie, chatoyance; tkanina: przekrój włókna (jedwab trójkątny — połysk, bawełna spłaszczona), aksamit.
  3. *Mokre = ciemniejsze (właściciel wyjaśnienia):* (1) woda w porach zmniejsza kontrast n (1,53/1,33 zamiast 1,53/1,00: F₀ ≈ 0,5% zamiast ≈ 4,4%) → mniej rozpraszania przy wierzchu, światło wchodzi głębiej i częściej jest pochłaniane; (2) warstwa wody na wierzchu odbija wewnętrznie (TIR, 49°) część wracającego światła na kolejną rundę absorpcji; (3) nasycenie rośnie. Woda sama prawie nie pochłania na tej drodze.
- **Zaawansowane:** „Olej na drewnie pogłębia słoje” (dopasowanie n w porach) i „rozjaśniacze optyczne w papierze” (fluorescencja, link R22).
- **(c) Wzory:** przywołanie F₀ z R18 dla par 1,53/1,00 i 1,53/1,33.
- **(d) Wizualizacje:**
  - Static SVG: przekrój kartki: włókna, powietrze, tory wielokrotnego rozpraszania.
  - SVG+slider: wypełnienie porów (powietrze → woda → olej) → biel, prześwit, nasycenie (raster).
  - Canvas2D: chatoyance — pasma jasności przesuwające się z kątem.
  - Static SVG: przekroje włókien (bawełna, jedwab, poliester, wełna).
  - Static SVG: mokre = ciemniejsze — oba mechanizmy na jednym przekroju.
- **(e) Mity:** „mokre ciemniejsze, bo woda pochłania”; „papier biały od wybielacza” (biały z budowy, bielenie usuwa ligninę); „drewno błyszczy od żywicy”.
- **(f) Wymaga:** R7, R12, R17, R18, R22. **Nie rusza:** chemii chromoforów (R22), włosa i wełny w szczegółach (R25), shaderów tkanin (lookdev).
- **(g) Linki:** Dodatek L; https://bartoszskrzypiec.github.io/lookdev-book/ ; https://bartoszskrzypiec.github.io/pxrsurface-guide/
- **(h) Z praktyki:** wetness w shaderze to nie tylko ciemniejsze diffuse i gładszy specular, ale też większe nasycenie i (dla porowatych) więcej prześwitu; maska wilgoci z trzech parametrów.

### R25 · Skóra, włosy, organika · `rozdzial-25-skora-wlosy-organika`
- **(a) Pytanie:** co skóra, włos i liść robią ze światłem? Po lekturze opisujesz skórę jako warstwy z melaniną i hemoglobiną w rozpraszającej tkance, włos jako walec keratyny z łuskami, liść jako chlorofil + komórki z powietrzem.
- **Nowe pojęcia (3):** tkanka jako ośrodek rozpraszająco-pochłaniający (czerwień wędruje najdalej) · dwa barwniki skóry · włos: R, TT, TRT.
- **(b) Sekcje:**
  1. *Co widzisz:* ucho pod światło czerwone, czerwona krawędź cienia, żyły „niebieskie”. Skóra: naskórek z melaniną (eumelanina, feomelanina; pochłanianie rosnące ku krótkim falom), skóra właściwa z hemoglobiną (415, 540, 575 nm) i kolagenem, F₀ ≈ 0,028.
  2. *Błądzenie światła:* droga swobodna ≈ 0,1 mm, dyfuzja na milimetry; czerwień pochłaniana najsłabiej, wędruje najdalej. Żyły: czerwień sięga żyły i ginie, niebieski wraca z płytszych warstw → żyła niebieskawa na tle skóry.
  3. *Włos:* keratyna n ≈ 1,55, łuski ≈ 3° → R przesunięty ku korzeniowi, TT, TRT kolorowy i przesunięty ku końcówce; melanina w korze; siwy = brak melaniny + pustki powietrzne.
  4. *Liść:* chlorofil (430, 660 nm) + komórki gąbczaste z powietrzem; jesienią rozpad chlorofilu odsłania karotenoidy.
- **Zaawansowane:** „Niebieskie oczy i białe twardówki” (rozpraszanie w zrębie, kolagen) oraz „Bliska podczerwień liści” (red edge).
- **(c) Wzory:** przywołanie Beera–Lamberta z R17 per kanał.
- **(d) Wizualizacje:**
  - **sky3d #7:** włos z łuskami, stożki R, TT, TRT; suwaki nachylenia łusek i kąta padania.
  - Static SVG: przekrój skóry z warstwami i torami R/G/B o różnej głębokości.
  - SVG+slider: widma melaniny i hemoglobiny (violet), suwaki stężeń → kolor skóry (raster).
  - Canvas2D: profil dyfuzji plamki światła w trzech kanałach.
  - Static SVG: widmo odbicia liścia 400–900 nm.
- **(e) Mity:** żyły od niebieskiej krwi; rumieniec jako pigment; szary pigment siwych włosów; niebieski pigment oczu; SSS jako „rozmycie diffuse”.
- **(f) Wymaga:** R7, R12, R14, R17, R18, R22. **Nie rusza:** parametrów shaderów skóry i włosów (lookdev, pxrsurface), algorytmów BSSRDF (raytracing), chemii porfiryn (R7).
- **(g) Linki:** Dodatek L, Dodatek J; https://bartoszskrzypiec.github.io/lookdev-book/ ; https://bartoszskrzypiec.github.io/pxrsurface-guide/ ; https://bartoszskrzypiec.github.io/raytracing-book/
- **(h) Z praktyki:** mean free path per kanał: czerwony kilka razy dłuższy od niebieskiego i skąd te proporcje; przesunięcie R i TRT (rzędu nachylenia łusek) jako longitudinal shift.

---

## Część VII — Świat w dużej skali (R26–R27)

### R26 · Atmosfera, chmury, mgła, dym · `rozdzial-26-atmosfera-chmury-mgla-dym`
- **(a) Pytanie:** jak Rayleigh, Mie i Beer–Lambert budują wygląd powietrza w skali kilometrów? Po lekturze wyjaśniasz zachód, perspektywę powietrzną, białą chmurę z ciemną podstawą i dwubarwny dym, i znasz równanie „ekstynkcja + inscattering”.
- **Nowe pojęcia (3):** długość drogi optycznej · perspektywa powietrzna (ekstynkcja + inscatter) · wielokrotne rozpraszanie.
- **(b) Sekcje:**
  1. *Co widzisz:* czerwone Słońce przy horyzoncie, góry w dali coraz bledsze i bardziej niebieskie. Zachód: droga przez atmosferę ≈ 38× dłuższa przy horyzoncie, Beer–Lambert z σₛ ∝ λ⁻⁴ zjada niebieski. Horyzont biały przez wielokrotne rozpraszanie i aerozole.
  2. *Perspektywa powietrzna:* obiekt tłumiony e^{−σₜd} plus światło samego powietrza; ciemne w dali niebieskieją, jasne żółkną; widzialność ≈ 3,9/σₜ.
  3. *Chmury i mgła:* krople ≈ 10 µm → Mie bez koloru, grubość optyczna dziesiątki → biel z wielokrotnego rozpraszania; podstawa ciemna, bo gruba chmura odsyła światło w górę i na boki; mgła to chmura przy ziemi.
  4. *Dym:* 0,1–1 µm, częściowo pochłaniający (sadza, R21): na ciemnym tle niebieskawy (rozproszone), na jasnym brązowawy (przepuszczone); biały dym = krople lub duże cząstki.
- **Zaawansowane:** brak (spektakl nieba: atmosfera_chmury_book).
- **(c) Wzory:** L = L₀e^{−σₜd} + L_tło(1 − e^{−σₜd}) (L radiancja, d odległość, L_tło kolor powietrza w nieskończoności); V ≈ 3,9/σₜ.
- **(d) Wizualizacje:**
  - SVG+slider: kąt Słońca → długość drogi → widmo bezpośrednie → kolor tarczy (raster).
  - Canvas2D: pasma gór w kolejnych planach, suwaki σₜ i koloru powietrza.
  - SVG+slider: dym na ciemnym i jasnym tle, suwak rozmiaru cząstek.
  - Canvas2D: chmura, grubość optyczna → jasność od góry i od dołu (model dwustrumieniowy).
  - Static SVG (opcjonalna): skala cząstek N₂ → aerozol → dym → kropla → kropla deszczu z reżimami.
- **(e) Mity:** zachód czerwony od zanieczyszczeń; chmury szare, bo brudne; mgła to para wodna (para jest niewidzialna); góry niebieskie od lasów.
- **(f) Wymaga:** R12–R14, R17, R21. **Nie rusza:** mechanizmu Rayleigha i polaryzacji nieba (R13 — link), Mie w szczegółach (R14), tęczy i halo (R27), powstawania i typów chmur, modeli nieba (atmosfera_chmury_book).
- **(g) Linki:** Dodatek E; https://bartoszskrzypiec.github.io/atmosfera_chmury_book/ (główne odesłanie); https://bartoszskrzypiec.github.io/raytracing-book/ (volume rendering); Tom 2, Rozdział 22.
- **(h) Z praktyki:** atmosfera w compie z Z-depth: e^{−σₜZ} per kanał (większe σₜ w niebieskim) + kolor nieba jako inscatter; jednolity „fog” z liniowym zanikiem wygląda sztucznie.

### R27 · Tęcza, halo i skąd bierze się kolor świata · `rozdzial-27-tecza-halo-kolor-swiata`
- **(a) Pytanie:** skąd tęcza i halo i jak wszystkie kolory świata sprowadzić do kilku mechanizmów? Po lekturze wyjaśniasz 42°, kolejność barw, łuk wtórny, halo 22° i posługujesz się tabelą mechanizmów jako mapą tomu.
- **Nowe pojęcia (3):** kąt minimalnego odchylenia (skupienie promieni) · tęcza jako stożek dla obserwatora · tabela mechanizmów koloru.
- **(b) Sekcje:**
  1. *Co widzisz:* tęcza zawsze naprzeciw Słońca, łuk wtórny z odwróconymi barwami, ciemne niebo między nimi. Załamanie + jedno odbicie w kropli → skupienie przy 42°; dyspersja wody rozciąga barwy 40,5–42°; stożek wokół punktu antysłonecznego, każdy ma własną tęczę.
  2. *Wtórna i halo:* wtórna 51° (dwa odbicia), pasmo Aleksandra; halo 22° z pryzmatów lodu 60° (n = 1,31), 46° z kąta 90°.
  3. *Tabela mechanizmów (zamknięcie tomu):* kolumny: mechanizm · skala · przykład · rozdział. Wiersze: emisja cieplna (płomień — R21), emisja liniowa (sód, neon — R4), chromofor sprzężony (karoten, chlorofil — R7, R22, R25), jon metalu przejściowego (rubin — R22), przerwa półprzewodnika (kadm, cynober — R6, R22), elektrony swobodne (złoto — R20), drgania cząsteczek (woda — R19), Rayleigh (niebo — R13), Mie i wielokrotne rozpraszanie (chmura, mleko, papier — R14, R24, R26), cienka warstwa (bańka — R22), nanostruktura (Morpho, sójka, oczy — R22, R25), dyspersja (tęcza, halo — R16, R27), fluorescencja (rozjaśniacze — R22). Tabela odsyła, nie tłumaczy od nowa.
- **Zaawansowane:** „Łuki dodatkowe: tęcza jako fala” (interferencja, wynik Mie) oraz „Wieniec i gloria” (dyfrakcja na kroplach, link Tom 2, Rozdział 10).
- **(c) Wzory:** D_min pryzmatu = 2 arcsin(n sin(A/2)) − A (A kąt łamiący; A = 60°, n = 1,31 → ≈ 22°); kąt tęczy 42° jako wynik (wyprowadzenie w Dodatku E).
- **(d) Wizualizacje:**
  - **sky3d #8:** obserwator, cień głowy, punkt antysłoneczny, stożki 42° i 51°.
  - SVG+slider: promień w kropli, suwak parametru zderzenia → kąt wyjścia, zagęszczenie przy minimum.
  - Canvas2D: natężenie w funkcji kąta dla kilku λ → pasma barw i pasmo Aleksandra.
  - SVG+slider: pryzmat lodowy 60°, suwak kąta padania, minimum ≈ 22°.
  - Static SVG: tabela mechanizmów jako diagram skali (atom → cząsteczka → ziarno → kropla).
- **(e) Mity:** tęcza w konkretnym miejscu, „koniec tęczy”; tęcza jako odbicie od chmury; siedem czystych λ.
- **(f) Wymaga:** R3, R14, R16, R18, R26. **Nie rusza:** powstawania kryształków i chmur (atmosfera_chmury_book), dyfrakcji w szczegółach (Tom 2, Rozdział 10), tłumaczenia mechanizmów od nowa.
- **(g) Linki:** Dodatek E; https://bartoszskrzypiec.github.io/atmosfera_chmury_book/ (tęcze, halo, glorie jako zjawiska); Tom 2, Rozdział 10; Tom 2, Rozdział 14; https://bartoszskrzypiec.github.io/raytracing-book/
- **(h) Z praktyki:** tęcza nie wyjdzie z RGB (trzy „krople” zamiast widma); w compie musi być przypięta do punktu antysłonecznego kamery, więc jedzie razem z kamerą.

---

## Dodatki — briefy skrótowe (EXT OF = pole `ext` w spisie)

Dodatki przejmują głębię, której rozdziały nie mieszczą. Rozdział odsyła do dodatku
po konkretny wzór lub liczbę, nigdy „po resztę tematu”.

| Dodatek | EXT OF | Zakres | Nie rusza |
|---|---|---|---|
| A Maxwell bez strachu [WZORY] | R1, R2 | cztery równania słowami i wzorami, fala płaska, c = 1/√(ε₀μ₀), B = E/c, natężenie I ∝ E², liczba „ile V/m ma słońce” | ośrodków (C, F) |
| B Oscylator Lorentza [WZORY] | R8, R9, R16 | mẍ + mγẋ + Kx = −eE, rozwiązanie w e^{−iωt}, amplituda i faza, α(ω), εᵣ(ω), suma oscylatorów → Sellmeier | Drudego (G) |
| C Clausius–Mossotti [WZORY] | R10, R15 | pole lokalne, (εᵣ−1)/(εᵣ+2) = Nα/(3ε₀), Lorentz–Lorenz, sprawdzenie: powietrze, woda, lód | Ewalda–Oseena (F) |
| D Promieniowanie dipola [WZORY] | R11, R13 | pole dalekie, Larmor P = p₀²ω⁴/(12πε₀c³), sin²θ, C_sca Rayleigha, (1 + cos²θ), stopień polaryzacji nieba | Mie (E) |
| E Mie w liczbach [WZORY] | R14, R26, R27 | x, Q_ext/Q_sca/Q_abs, paradoks 2, g, HG, tabela dla dymu, mgły, chmury, mleka; tęcza 42° z minimum odchylenia | pełnych szeregów Mie (tylko struktura) |
| F Ewald–Oseen [WZORY] | R12, R15 | pole warstwy dipoli (opóźnienie 90°), suma warstw, wygaszanie fali padającej, n z sumy | Clausiusa–Mossottiego (C) |
| G Drude i ωₚ [WZORY] | R20 | model, ωₚ z N, R(ω), wnikanie, pasmo d jako poprawka (Au, Cu) | tabel (I) |
| H n, κ, Beer–Lambert [WZORY] | R17, R18 | fala z ñ, σₐ = 4πκ/λ, δ, Fresnel s/p dla zespolonego n, konwencje znaku, TIR i fala zanikająca | powłok (Tom 2, Dodatek B) |
| I Tabela n i κ | R16, R19, R20, R21 | n, κ przy 450/550/650 i 589 nm dla gazów, wody, lodu, szkieł, plastików, metali, węgla; E_g | shaderów (J) |
| J Od n i κ do shadera [CG] | R18, R20, R23, R25 | F₀ z n; F₀ i edge tint z (n, κ); IOR; σₐ, σₛ z danych; mfp skóry; mapa suwaków PxrSurface → mechanizmy tomu | teorii BRDF (lookdev, raytracing) |
| K Poziomy energii i fotony [WZORY] | R4, R6 | fala w pudełku → dyskretne poziomy, E_n ∝ n²/L², od poziomów do pasm, 1240/λ, tabela E_g | formalizmu Schrödingera poza szkicem |
| L Atlas cząsteczek | R5, R7, R22, R24, R25 | SVG: H₂O, CO₂, N₂, O₂, celuloza, lignina (fragment), polietylen, keratyna (fragment), kolagen, melanina (fragment), hem, chlorofil, β-karoten, TiO₂ (sieć); przy każdej jedno zdanie „co robi ze światłem” | mechanizmów (rozdziały) |
| M Słownik PL–EN | R1 | terminy z 0.4 + nowe z rozdziałów | — |

Primer `tom1/matematyka/podstawy-matematyczne.html`: sinusoida (A, λ lub f, φ), faza jako kąt
i fazor, wektor i składowe (E ⊥ B), liczby zespolone jako strzałki, e^{iφ} i mnożenie jako obrót,
potęgi i skala log (λ⁻⁴, 5,9×), zanik wykładniczy (e^{−x}, długość zaniku).

## Uwagi dla recenzentów
- R3 nie ma dodatku (brak `.deeper` albo pusty) — zamierzone; jego „głębiej” to primer.
- Sprawdź łańcuch faz 0.8 w R9, R11, R12, R15, R16, R17, R18 — tu równoległe pisanie najłatwiej produkuje sprzeczność.
- Sprawdź, że liczby z 0.6 nie mają wariantów (szkło 1,52 dla BK7; „ok. 1,5” tylko dla polimerów i spoiw).
- Sprawdź, że rozdział nie wprowadza pojęć spoza swojej listy „Nowe pojęcia” (bramka gęstości).
- Część II: liczby elektronów, konfiguracje, kąty cząsteczek.
- Linki do siostrzanych: absolutne URL-e; do Tomu 2: `../../tom2/...`.
