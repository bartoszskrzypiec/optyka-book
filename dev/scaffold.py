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

Przy siedemdziesięciu stronach z ręcznie utrzymywaną nawigacją "sprawdz"
to jedyny sposób, żeby złapać literówkę w linku "Następny →".

Zaadaptowane z atmosfera_chmury_book/dev/scaffold.py. Różnice: nie ma
katalogu teren/, jest matematyka/, strony ładują widgets.css i viz3d.css
obok style.css, a kontrola pilnuje dodatkowo, żeby każdy .formula
definiował swoje symbole.
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
SPIS = json.load(open(os.path.join(ROOT, 'dev', 'spis.json'), encoding='utf-8'))

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700'
    '&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">'
)
MARKA = SPIS['marka']

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


def head(title, depth=1):
    up = '../' * depth
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


def topnav(links, depth=1):
    up = '../' * depth
    inner = '\n  '.join(f'<a href="{h}">{t}</a>' for t, h in links)
    return (
        '<nav class="topnav">\n'
        f'  <a class="topnav__brand" href="{up}index.html">{MARKA[0]} <span>{MARKA[1]}</span></a>\n'
        f'  <div class="topnav__links">\n  {inner}\n  </div>\n'
        '</nav>\n'
    )


def readout(chips):
    inner = ''.join(f'<span>{c}</span>' for c in chips)
    return f'  <div class="viewport-readout">\n    {inner}\n  </div>\n'


def deeper_block(items, depth=1):
    """Blok 'Idź głębiej'. Budowany z odwrotności mapy EXT OF."""
    if not items:
        return ''
    up = '../' * depth
    rows = '\n    '.join(
        f'<a href="{up}dodatki/{d["slug"]}.html">Dodatek {d["l"].upper()} — {d["tytul"]}</a>'
        for d in items
    )
    return f'  <div class="deeper">\n    <div class="deeper-label">Idź głębiej</div>\n    {rows}\n  </div>\n'


def rozdzial_page(ch, prev_ch, next_ch, dodatki_for):
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
        head(f'Rozdział {ch["nr"]} — {ch["tytul"]}')
        + topnav(links)
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
        + '<script src="../assets/interactive.js"></script>\n'
        + '</body>\n</html>\n'
    )


def dodatek_page(d, ch_by_nr):
    first = ch_by_nr[d['ext'][0]]
    ext_label = 'EXT OF · ' + ', '.join(f'R.{n}' for n in d['ext'])
    chips = ['Dodatek ' + d['l'].upper(),
             'Wzory · tak' if d.get('wzory') else ('Warstwa · CG' if d.get('cg') else 'Wzory · nie'),
             'Poziom · głębiej',
             ext_label]
    links = [('← Spis treści', '../index.html')]
    return (
        head(f'Dodatek {d["l"].upper()} — {d["tytul"]}')
        + topnav(links)
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
        + '<script src="../assets/interactive.js"></script>\n'
        + '</body>\n</html>\n'
    )


def matematyka_page(m):
    """Primer 'Zanim zaczniesz' — jedyna strona poza rozdziałami i dodatkami."""
    links = [('← Spis treści', '../index.html')]
    return (
        head(f'{m["tytul"]} — {SPIS["tytul"]}')
        + topnav(links)
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
        + '<script src="../assets/interactive.js"></script>\n'
        + '</body>\n</html>\n'
    )


def reverse_ext():
    """Mapa: numer rozdziału -> lista dodatków, które go rozwijają."""
    m = {}
    for d in SPIS['dodatki']:
        for n in d['ext']:
            m.setdefault(n, []).append(d)
    return m


def cmd_szkielet():
    # Puste katalogi nie sa sledzone przez gita, wiec na swiezym klonie
    # moze ich nie byc. Tworzymy je tutaj zamiast trzymac .gitkeep.
    for sub in ('rozdzialy', 'dodatki', 'matematyka'):
        os.makedirs(os.path.join(ROOT, sub), exist_ok=True)

    rozdz = SPIS['rozdzialy']
    ch_by_nr = {c['nr']: c for c in rozdz}
    rev = reverse_ext()
    made, skipped = [], []

    for i, ch in enumerate(rozdz):
        path = os.path.join(ROOT, 'rozdzialy', ch['slug'] + '.html')
        if os.path.exists(path):
            skipped.append(ch['slug'])
            continue
        prev_ch = rozdz[i - 1] if i > 0 else None
        next_ch = rozdz[i + 1] if i < len(rozdz) - 1 else None
        open(path, 'w', encoding='utf-8', newline='\n').write(
            rozdzial_page(ch, prev_ch, next_ch, rev.get(ch['nr'], [])))
        made.append(ch['slug'])

    for d in SPIS['dodatki']:
        path = os.path.join(ROOT, 'dodatki', d['slug'] + '.html')
        if os.path.exists(path):
            skipped.append(d['slug'])
            continue
        open(path, 'w', encoding='utf-8', newline='\n').write(dodatek_page(d, ch_by_nr))
        made.append(d['slug'])

    for m in SPIS.get('matematyka', []):
        path = os.path.join(ROOT, 'matematyka', m['slug'] + '.html')
        if os.path.exists(path):
            skipped.append(m['slug'])
            continue
        open(path, 'w', encoding='utf-8', newline='\n').write(matematyka_page(m))
        made.append(m['slug'])

    print(f'utworzone: {len(made)}, pominiete (juz istnieja): {len(skipped)}')
    for s in made:
        print('  +', s)


# ---------------------------------------------------------------- sprawdz

def all_pages():
    pages = []
    for sub in ('rozdzialy', 'dodatki', 'matematyka'):
        d = os.path.join(ROOT, sub)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if f.endswith('.html'):
                pages.append(os.path.join(d, f))
    idx = os.path.join(ROOT, 'index.html')
    if os.path.exists(idx):
        pages.append(idx)
    return pages


def cmd_sprawdz():
    problems = []
    rozdz = SPIS['rozdzialy']
    rev = reverse_ext()

    # 1. martwe linki wzgledne
    for path in all_pages():
        html = open(path, encoding='utf-8').read()
        base = os.path.dirname(path)
        for href in re.findall(r'href="([^"#:]+\.html)(?:#[^"]*)?"', html):
            target = os.path.normpath(os.path.join(base, href))
            if not os.path.exists(target):
                problems.append(f'MARTWY LINK  {os.path.relpath(path, ROOT)} -> {href}')

    # 2. nawigacja gorna musi zgadzac sie z dolna
    for i, ch in enumerate(rozdz):
        path = os.path.join(ROOT, 'rozdzialy', ch['slug'] + '.html')
        if not os.path.exists(path):
            problems.append(f'BRAK PLIKU   rozdzialy/{ch["slug"]}.html')
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
                problems.append(f'NAWIGACJA    R.{ch["nr"]}: brak bloku {nazwa}')

        for label, slug in (('Poprzedni', prev_s), ('Nastepny', next_s)):
            if slug is None:
                continue
            for nazwa, tresc in bloki.items():
                if tresc is None:
                    continue
                n = tresc.count(f'href="{slug}"')
                if n != 1:
                    problems.append(
                        f'NAWIGACJA    R.{ch["nr"]}: link {label} ({slug}) w bloku '
                        f'{nazwa} wystepuje {n}x, a powinien 1x')

    # 3. EXT OF <-> "Idz glebiej", obustronnie
    for d in SPIS['dodatki']:
        path = os.path.join(ROOT, 'dodatki', d['slug'] + '.html')
        if not os.path.exists(path):
            problems.append(f'BRAK PLIKU   dodatki/{d["slug"]}.html')
            continue
        html = open(path, encoding='utf-8').read()
        if 'EXT OF' not in html:
            problems.append(f'BRAK EXT OF  dodatki/{d["slug"]}.html')

    for ch in rozdz:
        path = os.path.join(ROOT, 'rozdzialy', ch['slug'] + '.html')
        if not os.path.exists(path):
            continue
        html = open(path, encoding='utf-8').read()
        for d in rev.get(ch['nr'], []):
            if d['slug'] not in html:
                problems.append(
                    f'BRAK ODNOSNIKA R.{ch["nr"]} nie linkuje do Dodatku {d["l"].upper()}, '
                    f'ktory deklaruje EXT OF R.{ch["nr"]}')

    # 4. bloki obowiazkowe w rozdzialach
    wymagane = [('TL;DR', 'TL;DR'), ('Z praktyki', 'Z praktyki'),
                ('Slowniczek', 'Słowniczek'), ('Co dalej', 'Co dalej')]
    for ch in rozdz:
        path = os.path.join(ROOT, 'rozdzialy', ch['slug'] + '.html')
        if not os.path.exists(path):
            continue
        html = open(path, encoding='utf-8').read()
        if '<!-- TRESC -->' in html:
            problems.append(f'PUSTY        R.{ch["nr"]} {ch["slug"]} — sam szkielet, brak tresci')
            continue
        for label, needle in wymagane:
            if needle not in html:
                problems.append(f'BRAK BLOKU   R.{ch["nr"]}: {label}')

    # 5. modal wymaga hosta na stronie
    for path in all_pages():
        html = open(path, encoding='utf-8').read()
        if 'data-modal-target' in html and 'id="modal-overlay"' not in html:
            problems.append(f'MODAL BEZ HOSTA {os.path.relpath(path, ROOT)}')
        if 'data-modal-target' in html and 'interactive.js' not in html:
            problems.append(f'MODAL BEZ JS    {os.path.relpath(path, ROOT)}')

    # 6. widget 3D wymaga fallbacku i wartownika
    for path in all_pages():
        html = open(path, encoding='utf-8').read()
        n_viz = html.count('class="viz3d"')
        n_fb = html.count('viz3d__fallback')
        if n_viz != n_fb:
            problems.append(
                f'FALLBACK     {os.path.relpath(path, ROOT)}: {n_viz} widgetow 3D, '
                f'{n_fb} blokow zastepczych')
        if n_viz and 'sky3d-fallback.js' not in html:
            problems.append(
                f'BRAK WARTOWNIKA {os.path.relpath(path, ROOT)}: widget 3D bez '
                f'sky3d-fallback.js (pusty prostokat przy file://)')

    # 6b. .subsection musi lezec wewnatrz .section
    #     Osierocona podsekcja miedzy sekcjami renderuje sie prawie poprawnie,
    #     wiec przechodzi wzrokowo, ale lamie strukture strony i wypada
    #     z licznika slow. Latwo o to przy wstawianiu tresci skryptem.
    #     Liczymy WSZYSTKIE divy, nie tylko sekcyjne — inaczej kazdy
    #     .diagram-frame czy .formula rozjezdza licznik zagniezdzenia.
    for path in all_pages():
        html = open(path, encoding='utf-8').read()
        stos = []
        for m in re.finditer(r'<div([^>]*)>|</div>', html):
            if m.group(0) == '</div>':
                if stos:
                    stos.pop()
                continue
            kl = re.search(r'class="([^"]*)"', m.group(1) or '')
            klasy = kl.group(1).split() if kl else []
            if 'subsection' in klasy and 'section' not in stos:
                problems.append(
                    f'PODSEKCJA    {os.path.relpath(path, ROOT)}: .subsection poza .section '
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
            path = os.path.join(ROOT, 'rozdzialy', ch['slug'] + '.html')
            if not os.path.exists(path):
                continue
            if '<!-- TRESC -->' in open(path, encoding='utf-8').read():
                continue                      # szkielet, liczy go kontrola 4
            sl, wiz = slowa.zlicz(path)
            if not (slowa.CEL_SLOW[0] <= sl <= slowa.CEL_SLOW[1]):
                problems.append(
                    f'DLUGOSC      R.{ch["nr"]}: {sl} slow, cel '
                    f'{slowa.CEL_SLOW[0]}-{slowa.CEL_SLOW[1]}')
            if not (slowa.CEL_WIZ[0] <= wiz <= slowa.CEL_WIZ[1]):
                problems.append(
                    f'WIZUALIZACJE R.{ch["nr"]}: {wiz}, cel '
                    f'{slowa.CEL_WIZ[0]}-{slowa.CEL_WIZ[1]}')
    except Exception as e:
        problems.append(f'DLUGOSC      nie udalo sie sprawdzic: {e}')

    # 7. znaczniki stanu w spisie tresci musza zgadzac sie z rzeczywistoscia
    #    Bez tego czytelnik klika w rozdzial oznaczony jako gotowy i trafia
    #    na szkielet. Naprawa: python dev/stan.py
    try:
        import stan
        for href in stan.sprawdz():
            problems.append(
                f'STAN W SPISIE index.html: wiersz {href} ma zly znacznik '
                f'(napraw: python dev/stan.py)')
    except Exception as e:
        problems.append(f'STAN W SPISIE nie udalo sie sprawdzic: {e}')

    # 8. wzor musi definiowac swoje symbole
    #    Zasada rodziny: kiedy .formula wprowadza zmienna, trzeba powiedziec,
    #    co ona znaczy. Mechanicznie da sie sprawdzic tylko obecnosc .sub —
    #    definicja w prozie obok jest rownie dobra, wiec to ostrzezenie,
    #    nie blad. Stad osobna lista.
    ostrzezenia = []
    for path in all_pages():
        html = open(path, encoding='utf-8').read()
        # Wzor w <template> to wnetrze modala "Wyjasnij ten wzor" — tam symbole
        # objasnia otaczajaca proza, wiec .sub bylby powtorzeniem.
        bez_szablonow = re.sub(r'<template.*?</template>', '', html, flags=re.S)
        for m in re.finditer(r'<div class="formula"[^>]*>(.*?)</div>', bez_szablonow, re.S):
            if 'class="sub"' not in m.group(1):
                frag = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(1))).strip()[:60]
                ostrzezenia.append(
                    f'WZOR BEZ .sub {os.path.relpath(path, ROOT)}: "{frag}" — '
                    f'upewnij sie, ze symbole sa zdefiniowane w prozie obok')

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
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'sprawdz'
    if cmd == 'szkielet':
        cmd_szkielet()
    elif cmd == 'sprawdz':
        cmd_sprawdz()
    else:
        print(__doc__)
        sys.exit(2)
