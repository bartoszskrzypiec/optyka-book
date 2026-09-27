#!/usr/bin/env python3
"""
Narzędzie deweloperskie. NIE jest krokiem budowania — książka to statyczne
pliki HTML i nic ich nie generuje w locie.

Robi dwie rzeczy:

  python dev/scaffold.py szkielet   — tworzy BRAKUJĄCE strony z pełnym
        nagłówkiem, nawigacją i stopką, zostawiając w środku znacznik
        <!-- TRESC -->. Istniejących plików NIE RUSZA, nigdy. Treść pisze
        się potem ręcznie, w miejscu.

  python dev/scaffold.py sprawdz    — kontrola spójności: martwe linki,
        zgodność nawigacji górnej z dolną, obustronna zgodność EXT OF
        z blokami "Idź głębiej", brakujące bloki obowiązkowe, wzory bez
        definicji symboli, widgety 3D bez fallbacku.

Obie komendy przyjmują opcjonalny argument --tom N (np. "sprawdz --tom 2").
Bez niego działają na KAŻDYM tomie, dla którego istnieje dev/spis-tomN.json
— dziś tylko tom2 (tom2/rozdzialy, tom2/dodatki, tom2/matematyka,
tom2/index.html), tom1 dołączy się sam, gdy powstanie dev/spis-tom1.json
i katalog tom1/. assets/ zostaje wspólne w katalogu głównym repo — strony
tomów sięgają do niego przez ../../assets/, bo są dwa poziomy niżej.

Przy siedemdziesięciu stronach z ręcznie utrzymywaną nawigacją "sprawdz"
to jedyny sposób, żeby złapać literówkę w linku "Następny →".

Zaadaptowane z atmosfera_chmury_book/dev/scaffold.py. Różnice: nie ma
katalogu teren/, jest matematyka/, strony ładują widgets.css i viz3d.css
obok style.css, kontrola pilnuje dodatkowo, żeby każdy .formula
definiował swoje symbole, a od podziału na tomy wszystko liczone jest
per wolumin (tom2/, docelowo też tom1/).
"""

import json
import os
import re
import sys

# Narzedzia dev importuja sie nawzajem, a Python cache'uje bytecode. Po edycji
# slowa.py (np. zmianie progu) scaffold.py potrafil wczytac STARY .pyc i
# raportowac nieaktualny wynik - co przy kontroli, ktora ma byc brama przed
# commitem, jest gorsze niz brak kontroli. Zadnych .pyc dla tych skryptow.
sys.dont_write_bytecode = True

# Konsola Windows startuje w cp1250 i wywraca sie na pierwszym lepszym n₁,
# − albo →, a tresc ksiazki jest ich pelna. Bez tego "sprawdz" potrafi
# przerwac raport w polowie wyjatkiem zamiast pokazac problemy.
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700'
    '&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">'
)

# Komunikaty awarii widgetu 3D po polsku. sky3d-fallback.js ma domyslne
# angielskie; ustawiamy je PRZED zaladowaniem tego skryptu, zgodnie
# z kontraktem opisanym w learning-materials/docs/INTEGRATION.md.
SKY3D_MSG = """<script>
window.SKY3D_MESSAGES = {
  file:   { title: 'Widget 3D nie uruchamia sie z pliku na dysku',
            why:   'Strona jest otwarta spod adresu file://, a przegladarka nie wczytuje stamtad silnika 3D. Otworz ksiazke przez lokalny serwer — na przyklad rozszerzeniem Live Server w VS Code.' },
  siec:   { title: 'Nie udalo sie wczytac silnika 3D',
            why:   'Plik assets/sky3d.js albo three.js nie doladowal sie. Reszta rozdzialu jest kompletna bez widgetu.' },
  webgl:  { title: 'Ten widget potrzebuje WebGL',
            why:   'Przegladarka nie udostepnia WebGL-a.' },
  shader: { title: 'Karta graficzna odrzucila ten widget',
            why:   'Sterownik nie skompilowal shadera sceny. W konsoli jest pelny komunikat.' }
};
</script>"""


# ------------------------------------------------------------------ wolumin

class Volume:
    """Jeden tom: jego spis, katalog i o ile poziomow glebiej niz katalog
    glowny repo (dla stron tomu, ktore musza siegac do wspolnego assets/)."""

    def __init__(self, n):
        self.n = n
        spis_path = os.path.join(ROOT, 'dev', f'spis-tom{n}.json')
        self.spis = json.load(open(spis_path, encoding='utf-8'))
        self.sub = f'tom{n}'
        self.root = os.path.join(ROOT, self.sub)
        # Liczba segmentow katalogu tomu ponizej ROOT (dzis zawsze 1: "tomN").
        self.extra = len([p for p in os.path.relpath(self.root, ROOT).split(os.sep) if p])
        self.index = os.path.join(self.root, 'index.html')
        self.marka = self.spis['marka']
        self.label = f'T{n}'


def find_volumes():
    """Numery tomow, dla ktorych istnieje dev/spis-tomN.json, rosnaco."""
    ns = []
    dev_dir = os.path.join(ROOT, 'dev')
    for fn in os.listdir(dev_dir):
        m = re.match(r'spis-tom(\d+)\.json$', fn)
        if m:
            ns.append(int(m.group(1)))
    return sorted(ns)


def load_volumes(tom=None):
    if tom is not None:
        return [Volume(tom)]
    vols = [Volume(n) for n in find_volumes()]
    if not vols:
        sys.exit('BLAD: brak dev/spis-tomN.json — nie ma czego sprawdzac ani budowac')
    return vols


# ------------------------------------------------------------------ szablony

def head(title, asset_depth=1):
    up = '../' * asset_depth
    return (
        '<!DOCTYPE html>\n<html lang="pl">\n<head>\n'
        '<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'<title>{title}</title>\n'
        f'{FONTS}\n'
        f'<link rel="stylesheet" href="{up}assets/style.css">\n'
        f'<link rel="stylesheet" href="{up}assets/widgets.css">\n'
        f'<link rel="stylesheet" href="{up}assets/viz3d.css">\n'
        f'{SKY3D_MSG}\n'
        f'<script src="{up}assets/sky3d-fallback.js"></script>\n'
        '</head>\n<body>\n'
    )


def topnav(links, marka, depth=1):
    # depth tutaj jest wzgledem KORZENIA TOMU (gdzie lezy tomN/index.html),
    # nie wzgledem ROOT repo — rozdzialy/dodatki/matematyka sa zawsze jeden
    # poziom pod korzeniem tomu, wiec depth=1 bez wzgledu na to, ile poziomow
    # ponizej ROOT lezy sam tom.
    up = '../' * depth
    inner = '\n  '.join(f'<a href="{h}">{t}</a>' for t, h in links)
    return (
        '<nav class="topnav">\n'
        f'  <a class="topnav__brand" href="{up}index.html">{marka[0]} <span>{marka[1]}</span></a>\n'
        f'  <div class="topnav__links">\n  {inner}\n  </div>\n'
        '</nav>\n'
    )


def readout(chips):
    inner = ''.join(f'<span>{c}</span>' for c in chips)
    return f'  <div class="viewport-readout">\n    {inner}\n  </div>\n'


def deeper_block(items, depth=1):
    """Blok 'Idź głębiej'. Budowany z odwrotności mapy EXT OF. depth wzgledem
    korzenia tomu, jak w topnav() — dodatki/ jest siostrzanym katalogiem
    rozdzialy/ pod tym samym korzeniem."""
    if not items:
        return ''
    up = '../' * depth
    rows = '\n    '.join(
        f'<a href="{up}dodatki/{d["slug"]}.html">Dodatek {d["l"].upper()} — {d["tytul"]}</a>'
        for d in items
    )
    return f'  <div class="deeper">\n    <div class="deeper-label">Idź głębiej</div>\n    {rows}\n  </div>\n'


def rozdzial_page(vol, ch, prev_ch, next_ch, dodatki_for):
    asset_depth = 1 + vol.extra
    up_assets = '../' * asset_depth

    links = [('Spis treści', '../index.html')]
    if prev_ch:
        links.append(('← Poprzedni', f'{prev_ch["slug"]}.html'))
    if next_ch:
        links.append(('Następny →', f'{next_ch["slug"]}.html'))

    nav_rows = []
    if prev_ch:
        nav_rows.append(f'      <a class="nav-prev" href="{prev_ch["slug"]}.html">← Poprzedni</a>')
    nav_rows.append('      <a class="nav-toc" href="../index.html">Spis treści</a>')
    if next_ch:
        nav_rows.append(f'      <a class="nav-next" href="{next_ch["slug"]}.html">Następny →</a>')

    return (
        head(f'Rozdział {ch["nr"]} — {ch["tytul"]}', asset_depth)
        + topnav(links, vol.marka)
        + '\n<div class="page">\n\n'
        + readout(ch['readout'])
        + f'\n  <div class="eyebrow">Rozdział {ch["nr"]} / {ch["eyebrow"]}</div>\n'
        + f'  <h1>{ch["tytul"]}</h1>\n'
        + f'  <p class="subtitle">{ch["hook"]}</p>\n\n'
        + '  <!-- TRESC -->\n\n'
        + deeper_block(dodatki_for)
        + '\n  <div class="site-nav chapter-nav">\n'
        + '\n'.join(nav_rows)
        + '\n  </div>\n\n'
        + '</div>\n\n'
        + f'<script src="{up_assets}assets/interactive.js"></script>\n'
        + '</body>\n</html>\n'
    )


def dodatek_page(vol, d, ch_by_nr):
    asset_depth = 1 + vol.extra
    up_assets = '../' * asset_depth

    first = ch_by_nr[d['ext'][0]]
    ext_label = 'EXT OF · ' + ', '.join(f'R.{n}' for n in d['ext'])
    chips = ['Dodatek ' + d['l'].upper(),
             'Wzory · tak' if d.get('wzory') else ('Warstwa · CG' if d.get('cg') else 'Wzory · nie'),
             'Poziom · głębiej',
             ext_label]
    links = [('← Spis treści', '../index.html')]
    return (
        head(f'Dodatek {d["l"].upper()} — {d["tytul"]}', asset_depth)
        + topnav(links, vol.marka)
        + '\n<div class="page">\n\n'
        + readout(chips)
        + f'\n  <div class="eyebrow">Dodatek {d["l"].upper()} / Głębiej</div>\n'
        + f'  <h1>{d["tytul"]}</h1>\n'
        + f'  <p class="subtitle">{d["opis"]}</p>\n\n'
        + '  <!-- TRESC -->\n\n'
        + '  <div class="site-nav">\n'
        + '    <a href="../index.html">← Spis treści</a>\n'
        + f'    <a href="../rozdzialy/{first["slug"]}.html">↑ Rozdział {first["nr"]}: {first["tytul"]}</a>\n'
        + '  </div>\n\n'
        + '</div>\n\n'
        + f'<script src="{up_assets}assets/interactive.js"></script>\n'
        + '</body>\n</html>\n'
    )


def matematyka_page(vol, m):
    """Primer 'Zanim zaczniesz' — jedyna strona poza rozdziałami i dodatkami."""
    asset_depth = 1 + vol.extra
    up_assets = '../' * asset_depth

    links = [('← Spis treści', '../index.html')]
    return (
        head(f'{m["tytul"]} — {vol.spis["tytul"]}', asset_depth)
        + topnav(links, vol.marka)
        + '\n<div class="page">\n\n'
        + readout(['Zanim zaczniesz', 'Poziom · podstawy', 'Wzory · tak', 'Wracaj tu w razie czego'])
        + '\n  <div class="eyebrow">Zanim zaczniesz</div>\n'
        + f'  <h1>{m["tytul"]}</h1>\n'
        + f'  <p class="subtitle">{m["opis"]}</p>\n\n'
        + '  <!-- TRESC -->\n\n'
        + '  <div class="site-nav">\n'
        + '    <a href="../index.html">← Spis treści</a>\n'
        + '  </div>\n\n'
        + '</div>\n\n'
        + f'<script src="{up_assets}assets/interactive.js"></script>\n'
        + '</body>\n</html>\n'
    )


def reverse_ext(vol):
    """Mapa: numer rozdziału -> lista dodatków, które go rozwijają (w danym tomie)."""
    m = {}
    for d in vol.spis['dodatki']:
        for n in d['ext']:
            m.setdefault(n, []).append(d)
    return m


def cmd_szkielet(tom=None):
    for vol in load_volumes(tom):
        # Puste katalogi nie sa sledzone przez gita, wiec na swiezym klonie
        # moze ich nie byc. Tworzymy je tutaj zamiast trzymac .gitkeep.
        for sub in ('rozdzialy', 'dodatki', 'matematyka'):
            os.makedirs(os.path.join(vol.root, sub), exist_ok=True)

        rozdz = vol.spis['rozdzialy']
        ch_by_nr = {c['nr']: c for c in rozdz}
        rev = reverse_ext(vol)
        made, skipped = [], []

        for i, ch in enumerate(rozdz):
            path = os.path.join(vol.root, 'rozdzialy', ch['slug'] + '.html')
            if os.path.exists(path):
                skipped.append(ch['slug'])
                continue
            prev_ch = rozdz[i - 1] if i > 0 else None
            next_ch = rozdz[i + 1] if i < len(rozdz) - 1 else None
            open(path, 'w', encoding='utf-8', newline='\n').write(
                rozdzial_page(vol, ch, prev_ch, next_ch, rev.get(ch['nr'], [])))
            made.append(ch['slug'])

        for d in vol.spis['dodatki']:
            path = os.path.join(vol.root, 'dodatki', d['slug'] + '.html')
            if os.path.exists(path):
                skipped.append(d['slug'])
                continue
            open(path, 'w', encoding='utf-8', newline='\n').write(dodatek_page(vol, d, ch_by_nr))
            made.append(d['slug'])

        for m in vol.spis.get('matematyka', []):
            path = os.path.join(vol.root, 'matematyka', m['slug'] + '.html')
            if os.path.exists(path):
                skipped.append(m['slug'])
                continue
            open(path, 'w', encoding='utf-8', newline='\n').write(matematyka_page(vol, m))
            made.append(m['slug'])

        print(f'{vol.label}: utworzone: {len(made)}, pominiete (juz istnieja): {len(skipped)}')
        for s in made:
            print('  +', s)


# ---------------------------------------------------------------- sprawdz

def all_pages(vol):
    pages = []
    for sub in ('rozdzialy', 'dodatki', 'matematyka'):
        d = os.path.join(vol.root, sub)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if f.endswith('.html'):
                pages.append(os.path.join(d, f))
    if os.path.exists(vol.index):
        pages.append(vol.index)
    return pages


def _sprawdz_wolumin(vol, problems, ostrzezenia):
    L = vol.label
    rozdz = vol.spis['rozdzialy']
    rev = reverse_ext(vol)
    strony = all_pages(vol)

    # 1. martwe linki wzgledne
    for path in strony:
        html = open(path, encoding='utf-8').read()
        base = os.path.dirname(path)
        for href in re.findall(r'href="([^"#:]+\.html)(?:#[^"]*)?"', html):
            target = os.path.normpath(os.path.join(base, href))
            if not os.path.exists(target):
                problems.append(f'{L} MARTWY LINK  {os.path.relpath(path, ROOT)} -> {href}')

    # 2. nawigacja gorna musi zgadzac sie z dolna
    for i, ch in enumerate(rozdz):
        path = os.path.join(vol.root, 'rozdzialy', ch['slug'] + '.html')
        if not os.path.exists(path):
            problems.append(f'{L} BRAK PLIKU   rozdzialy/{ch["slug"]}.html')
            continue
        html = open(path, encoding='utf-8').read()
        prev_s = rozdz[i - 1]['slug'] + '.html' if i > 0 else None
        next_s = rozdz[i + 1]['slug'] + '.html' if i < len(rozdz) - 1 else None
        # Liczymy w DWOCH konkretnych blokach, nie na calej stronie. Proza
        # rozdzialu legalnie odsyla do sasiadow ("w nastepnym rozdziale
        # zajmiemy sie..."), a liczenie globalne uznawalo kazdy taki odsylacz
        # za zdublowana nawigacje.
        bloki = {}
        mt = re.search(r'<nav class="topnav">.*?</nav>', html, re.S)
        bloki['topnav'] = mt.group(0) if mt else None
        ms = re.search(r'<div class="site-nav[^"]*">.*?</div>', html, re.S)
        bloki['site-nav'] = ms.group(0) if ms else None

        for nazwa, tresc in bloki.items():
            if tresc is None:
                problems.append(f'{L} NAWIGACJA    R.{ch["nr"]}: brak bloku {nazwa}')

        for label, slug in (('Poprzedni', prev_s), ('Nastepny', next_s)):
            if slug is None:
                continue
            for nazwa, tresc in bloki.items():
                if tresc is None:
                    continue
                n = tresc.count(f'href="{slug}"')
                if n != 1:
                    problems.append(
                        f'{L} NAWIGACJA    R.{ch["nr"]}: link {label} ({slug}) w bloku '
                        f'{nazwa} wystepuje {n}x, a powinien 1x')

    # 3. EXT OF <-> "Idz glebiej", obustronnie
    for d in vol.spis['dodatki']:
        path = os.path.join(vol.root, 'dodatki', d['slug'] + '.html')
        if not os.path.exists(path):
            problems.append(f'{L} BRAK PLIKU   dodatki/{d["slug"]}.html')
            continue
        html = open(path, encoding='utf-8').read()
        if 'EXT OF' not in html:
            problems.append(f'{L} BRAK EXT OF  dodatki/{d["slug"]}.html')

    for ch in rozdz:
        path = os.path.join(vol.root, 'rozdzialy', ch['slug'] + '.html')
        if not os.path.exists(path):
            continue
        html = open(path, encoding='utf-8').read()
        for d in rev.get(ch['nr'], []):
            if d['slug'] not in html:
                problems.append(
                    f'{L} BRAK ODNOSNIKA R.{ch["nr"]} nie linkuje do Dodatku {d["l"].upper()}, '
                    f'ktory deklaruje EXT OF R.{ch["nr"]}')

    # 4. bloki obowiazkowe w rozdzialach
    wymagane = [('TL;DR', 'TL;DR'), ('Z praktyki', 'Z praktyki'),
                ('Slowniczek', 'Słowniczek'), ('Co dalej', 'Co dalej')]
    for ch in rozdz:
        path = os.path.join(vol.root, 'rozdzialy', ch['slug'] + '.html')
        if not os.path.exists(path):
            continue
        html = open(path, encoding='utf-8').read()
        if '<!-- TRESC -->' in html:
            problems.append(f'{L} PUSTY        R.{ch["nr"]} {ch["slug"]} — sam szkielet, brak tresci')
            continue
        for label, needle in wymagane:
            if needle not in html:
                problems.append(f'{L} BRAK BLOKU   R.{ch["nr"]}: {label}')

    # 4b. dodatek bez tresci
    # Kontrola dopisana 2026-09-03: przez cala prace nad ksiazka brama
    # sprawdzala PUSTY tylko dla rozdzialow, wiec Dodatek AG przelezal
    # nienapisany az do konca i wyszedl dopiero przy recznym przegladzie.
    for d in vol.spis['dodatki']:
        path = os.path.join(vol.root, 'dodatki', d['slug'] + '.html')
        if not os.path.exists(path):
            continue
        html = open(path, encoding='utf-8').read()
        if '<!-- TRESC -->' in html or 'class="section"' not in html:
            problems.append(f'{L} PUSTY        Dodatek {d["l"].upper()} {d["slug"]} — sam szkielet, brak tresci')

    # 5. modal wymaga hosta na stronie
    for path in strony:
        html = open(path, encoding='utf-8').read()
        if 'data-modal-target' in html and 'id="modal-overlay"' not in html:
            problems.append(f'{L} MODAL BEZ HOSTA {os.path.relpath(path, ROOT)}')
        if 'data-modal-target' in html and 'interactive.js' not in html:
            problems.append(f'{L} MODAL BEZ JS    {os.path.relpath(path, ROOT)}')

    # 6. widget 3D wymaga fallbacku i wartownika
    for path in strony:
        html = open(path, encoding='utf-8').read()
        n_viz = html.count('class="viz3d"')
        n_fb = html.count('viz3d__fallback')
        if n_viz != n_fb:
            problems.append(
                f'{L} FALLBACK     {os.path.relpath(path, ROOT)}: {n_viz} widgetow 3D, '
                f'{n_fb} blokow zastepczych')
        if n_viz and 'sky3d-fallback.js' not in html:
            problems.append(
                f'{L} BRAK WARTOWNIKA {os.path.relpath(path, ROOT)}: widget 3D bez '
                f'sky3d-fallback.js (pusty prostokat przy file://)')

    # 6b. .subsection musi lezec wewnatrz .section
    #     Osierocona podsekcja miedzy sekcjami renderuje sie prawie poprawnie,
    #     wiec przechodzi wzrokowo, ale lamie strukture strony i wypada
    #     z licznika slow. Latwo o to przy wstawianiu tresci skryptem.
    #     Liczymy WSZYSTKIE divy, nie tylko sekcyjne — inaczej kazdy
    #     .diagram-frame czy .formula rozjezdza licznik zagniezdzenia.
    for path in strony:
        html = open(path, encoding='utf-8').read()
        stos = []
        for m in re.finditer(r'<div([^>]*)>|</div>', html):
            if m.group(0) == '</div>':
                if stos:
                    stos.pop()
                continue
            kl = re.search(r'class="([^"]*)"', m.group(1) or '')
            klasy = kl.group(1).split() if kl else []
            if 'subsection' in klasy and 'section' not in stos:
                problems.append(
                    f'{L} PODSEKCJA    {os.path.relpath(path, ROOT)}: .subsection poza .section '
                    f'(znak {m.start()})')
            stos.append('section' if 'section' in klasy else '-')

    # 6c. napisany rozdzial musi miescic sie w zalozonym przedziale
    #     To NIE jest kosmetyka. Trzy razy w tej ksiazce zdarzylo sie, ze
    #     commit deklarowal osiagniety prog, bo liczbe wpisano z pamieci
    #     sprzed ostatniej edycji. Kontrola dyscypliny zawiodla trzy razy,
    #     wiec zastepujemy ja brama: rozdzial ponizej progu nie przechodzi
    #     "sprawdz", a "sprawdz" jest warunkiem commita.
    try:
        import slowa
        for ch in rozdz:
            path = os.path.join(vol.root, 'rozdzialy', ch['slug'] + '.html')
            if not os.path.exists(path):
                continue
            if '<!-- TRESC -->' in open(path, encoding='utf-8').read():
                continue                      # szkielet, liczy go kontrola 4
            sl, wiz = slowa.zlicz(path)
            if not (slowa.CEL_SLOW[0] <= sl <= slowa.CEL_SLOW[1]):
                problems.append(
                    f'{L} DLUGOSC      R.{ch["nr"]}: {sl} slow, cel '
                    f'{slowa.CEL_SLOW[0]}-{slowa.CEL_SLOW[1]}')
            if not (slowa.CEL_WIZ[0] <= wiz <= slowa.CEL_WIZ[1]):
                problems.append(
                    f'{L} WIZUALIZACJE R.{ch["nr"]}: {wiz}, cel '
                    f'{slowa.CEL_WIZ[0]}-{slowa.CEL_WIZ[1]}')
    except Exception as e:
        problems.append(f'{L} DLUGOSC      nie udalo sie sprawdzic: {e}')

    # 7. znaczniki stanu w spisie tresci musza zgadzac sie z rzeczywistoscia
    #    Bez tego czytelnik klika w rozdzial oznaczony jako gotowy i trafia
    #    na szkielet. Naprawa: python dev/stan.py
    try:
        import stan
        for href in stan.sprawdz_tom(vol.n):
            problems.append(
                f'{L} STAN W SPISIE tom{vol.n}/index.html: wiersz {href} ma zly znacznik '
                f'(napraw: python dev/stan.py)')
    except Exception as e:
        problems.append(f'{L} STAN W SPISIE nie udalo sie sprawdzic: {e}')

    # 8. divy musza sie domykac
    #    Przegladarka wybacza nadmiarowy </div> i strona wyglada poprawnie,
    #    wiec taki blad potrafi przelezec przez cala sesje niezauwazony —
    #    w R.5 przelezal. Skutki widac dopiero pozniej: sekcja domknieta za
    #    wczesnie wyrzuca swoje diagramy poza .section, a wtedy licznik slow
    #    i kontrola podsekcji mierza co innego, niz widzi czytelnik.
    for path in strony:
        html = open(path, encoding='utf-8').read()
        glebokosc, nadmiar = 0, None
        for m in re.finditer(r'<div\b[^>]*>|</div>', html):
            glebokosc += 1 if m.group(0).startswith('<div') else -1
            if glebokosc < 0 and nadmiar is None:
                nadmiar = html[:m.start()].count('\n') + 1
                break
        rel = os.path.relpath(path, ROOT)
        if nadmiar is not None:
            problems.append(f'{L} DIVY         {rel}: nadmiarowy </div> w linii {nadmiar}')
        elif glebokosc != 0:
            problems.append(f'{L} DIVY         {rel}: {glebokosc} niedomknietych <div>')

    # 9. wzor musi definiowac swoje symbole
    #    Zasada rodziny: kiedy .formula wprowadza zmienna, trzeba powiedziec,
    #    co ona znaczy. Mechanicznie da sie sprawdzic tylko obecnosc .sub —
    #    definicja w prozie obok jest rownie dobra, wiec to ostrzezenie,
    #    nie blad. Stad osobna lista.
    for path in strony:
        html = open(path, encoding='utf-8').read()
        # Wzor w <template> to wnetrze modala "Wyjasnij ten wzor" — tam symbole
        # objasnia otaczajaca proza, wiec .sub bylby powtorzeniem.
        bez_szablonow = re.sub(r'<template.*?</template>', '', html, flags=re.S)
        for m in re.finditer(r'<div class="formula"[^>]*>(.*?)</div>', bez_szablonow, re.S):
            if 'class="sub"' not in m.group(1):
                frag = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(1))).strip()[:60]
                ostrzezenia.append(
                    f'{L} WZOR BEZ .sub {os.path.relpath(path, ROOT)}: "{frag}" — '
                    f'upewnij sie, ze symbole sa zdefiniowane w prozie obok')


def cmd_sprawdz(tom=None):
    problems = []
    ostrzezenia = []
    for vol in load_volumes(tom):
        _sprawdz_wolumin(vol, problems, ostrzezenia)

    if ostrzezenia:
        print(f'{len(ostrzezenia)} ostrzezen (nie blokuja):\n')
        for o in ostrzezenia:
            print(' ', o)
        print()

    if problems:
        print(f'ZNALEZIONO {len(problems)} problemow:\n')
        for p in problems:
            print(' ', p)
        sys.exit(1)
    print('Wszystko spojne: linki, nawigacja, EXT OF, bloki, modale, fallbacki.')


if __name__ == '__main__':
    argv = sys.argv[1:]
    cmd = argv[0] if argv else 'sprawdz'
    tom = None
    rest = argv[1:]
    i = 0
    while i < len(rest):
        if rest[i] == '--tom':
            tom = int(rest[i + 1])
            i += 2
        else:
            i += 1

    if cmd == 'szkielet':
        cmd_szkielet(tom)
    elif cmd == 'sprawdz':
        cmd_sprawdz(tom)
    else:
        print(__doc__)
        sys.exit(2)
