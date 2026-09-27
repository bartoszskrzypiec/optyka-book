#!/usr/bin/env python3
"""Licznik prozy i wizualizacji. Trwaly plik, nie skrypt z brudnopisu —
Atmosfera stracila porownywalnosc wynikow miedzy sesjami przez to, ze
licznika nie zapisala.

    python dev/slowa.py                  — rozdzialy wszystkich tomow
    python dev/slowa.py --tom 2          — rozdzialy tylko Tomu 2
    python dev/slowa.py tom2/rozdzialy/x.html — jedna strona (dowolna sciezka)

"Tom" to katalog tomN/ obok dev/spis-tomN.json. Bez --tom skrypt znajduje
kazdy tom, dla ktorego taki plik istnieje (dzis tylko tom2, tom1 dolaczy
sam, gdy powstanie dev/spis-tom1.json).

Liczy WYLACZNIE proze w <div class="section">: pomija TL;DR, "Z praktyki",
Slowniczek, "Co dalej", nawigacje i podpisy pod diagramami. Cel na rozdzial:
1200-1600 slow i 4-6 wizualizacji.

Prog obnizony 2026-09-02 z 2000-3500. Powod: rozdzialy w starym formacie
wychodzily za geste dla artysty — R.7 upychal osiem nowych pojec naraz.
Nadmiar nie ginie: krotkie rozwiniecia ida do blokow "Zaawansowane" na tej
samej stronie, duze tematy z wlasnym rachunkiem do dodatkow z mapy "ext"
w spis-tomN.json.
"""
import io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CEL_SLOW = (1200, 1600)
CEL_WIZ = (4, 6)


def find_volumes():
    """Numery tomow, dla ktorych istnieje dev/spis-tomN.json."""
    ns = []
    dev_dir = os.path.join(ROOT, 'dev')
    for fn in os.listdir(dev_dir):
        m = re.match(r'spis-tom(\d+)\.json$', fn)
        if m:
            ns.append(int(m.group(1)))
    return sorted(ns)


def rozdzialy_dir(n):
    return os.path.join(ROOT, f'tom{n}', 'rozdzialy')


def zlicz(path):
    html = io.open(path, encoding='utf-8').read()
    slowa = 0
    for m in re.finditer(r'<div class="section">(.*?)(?=<div class="section">|<div class="panel|<div class="deeper|<div class="site-nav)', html, re.S):
        tekst = re.sub(r'<(script|style|svg)\b.*?</\1>', ' ', m.group(1), flags=re.S)
        tekst = re.sub(r'<[^>]+>', ' ', tekst)
        slowa += len(re.findall(r'[0-9A-Za-zĄąĆćĘęŁłŃńÓóŚśŹźŻż]+', tekst))
    wiz = html.count('<svg') + html.count('class="viz3d"') + html.count('class="sim"')
    return slowa, wiz


def flaga(v, lo, hi):
    return '  ' if lo <= v <= hi else ('!!' if v < lo else '++')


def main():
    argv = sys.argv[1:]
    tom = None
    cele = []
    i = 0
    while i < len(argv):
        if argv[i] == '--tom':
            tom = int(argv[i + 1])
            i += 2
        else:
            cele.append(argv[i])
            i += 1

    if not cele:
        tomy = [tom] if tom is not None else find_volumes()
        for n in tomy:
            d = rozdzialy_dir(n)
            if os.path.isdir(d):
                cele += [os.path.join(d, f) for f in sorted(os.listdir(d)) if f.endswith('.html')]

    razem_s = razem_w = 0
    for p in cele:
        s, w = zlicz(p)
        razem_s += s
        razem_w += w
        print('%s %5d slow  %s %2d wiz   %s' % (
            flaga(s, *CEL_SLOW), s, flaga(w, *CEL_WIZ), w, os.path.relpath(p, ROOT)))
    if len(cele) > 1:
        print('-' * 52)
        print('   %5d slow      %2d wiz   razem, %d stron (sr. %d slow)' % (
            razem_s, razem_w, len(cele), razem_s // max(1, len(cele))))
    print('\n!! ponizej celu   ++ powyzej celu   cel: %d-%d slow, %d-%d wiz' % (
        CEL_SLOW[0], CEL_SLOW[1], CEL_WIZ[0], CEL_WIZ[1]))


if __name__ == '__main__':
    main()
