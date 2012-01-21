#!/usr/bin/env python

from kanji.models import *
from parser import kanjidic2

kdic = kanjidic2.KanjiToday()

for k in kdic.kanji:
    ko = Kanji(literal=k.literal, grade=k.grade, stroke_count=k.stroke_count)
    ko.save()
    for on in k.on:
        ono = Onyomi(kanji=ko, literal=on)
        ono.save()
    for kun in k.kun:
        kuno = Kunyomi(kanji=ko, literal=kun)
        kuno.save()
    for meaning in k.meanings:
        mean = Meaning(kanji=ko, text=meaning)
        mean.save()
    for nan in k.nanori:
        nano = Nanori(kanji=ko, text=nan)
        nano.save()
    for d in k.definitions:
        do = Definition(kanji=ko, text=d)
        do.save()

