#!/usr/bin/env python3
"""Licznik prozy i wizualizacji. Trwaly plik, nie skrypt z brudnopisu —
Atmosfera stracila porownywalnosc wynikow miedzy sesjami przez to, ze
licznika nie zapisala.

    python dev/slowa.py                  — wszystkie rozdzialy
    python dev/slowa.py rozdzialy/x.html — jedna strona

Liczy WYLACZNIE proze w <div class="section">: pomija TL;DR, "Z praktyki",
Slowniczek, "Co dalej", nawigacje i podpisy pod diagramami. Cel na rozdzial:
2000-3500 slow i 5-8 wizualizacji.
"""
import io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CEL_SLOW = (2000, 3500)
CEL_WIZ = (5, 8)


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
    cele = sys.argv[1:]
    if not cele:
        d = os.path.join(ROOT, 'rozdzialy')
        cele = [os.path.join(d, f) for f in sorted(os.listdir(d)) if f.endswith('.html')]
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
