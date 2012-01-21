#!/usr/bin/env/python
# -*- coding: utf-8 -*-

from xml.dom.minidom import parse
from collections import defaultdict
import os

""" A class for parsing KANJIDIC2 XML file """

KANJIDIC2_DATAFILE = 'path_to_kanjidic2 xml file'
EDICT_DATAFILE = 'path_to_edict_file'

class KanjiToday():
    def __init__(self):
        self.elements = []
        self.definitions = defaultdict(list)
        self.kanji = []
        self.setup()

    def _open_kanjidic2_file_get_elements(self):
        if os.path.exists(KANJIDIC2_DATAFILE):
            dom = parse(KANJIDIC2_DATAFILE)
            self.elements = dom.getElementsByTagName("character")
        else:
            raise IOError('Could not open file %s' % KANJIDIC2_DATAFILE)

    def get_kanji(self):
        for element in self.elements:
            self.kanji.append(Kanji(element))

    # This is broken, had to be fixed manually, only accounts for lines of the dictionary file with single kanji (for example, 亜) but not kanji combined with hiragana (for example for verbs, like 亜ぐ)
    def _open_edict_file_get_definitions(self):
        if os.path.exists(EDICT_DATAFILE):
            lines = open(EDICT_DATAFILE, 'r').readlines()
            for line in lines:
                k, v = line.split(' ', 1)
                k, v = (k.decode('utf-8'), v.decode('utf-8'))
                self.definitions[k].append(v)
            for kanji in self.kanji:
                kanji.definitions = self.definitions[kanji.literal]
        else:
            raise IOError('Could not open file %s' % EDICT_DATAFILE)

    def setup(self):
        self._open_kanjidic2_file_get_elements()
        self.get_kanji()
        self._open_edict_file_get_definitions()

class Kanji():
    def __init__(self, element):
        self.element = element
        self.literal = ''
        self.grade = None
        self.stroke_count = 0
        self.on = []
        self.kun = []
        self.meanings = []
        self.nanori = []
        self.definitions = []
        self.setup()

    def get_literal(self):
        self.literal = self.element.getElementsByTagName("literal")[0].childNodes[0].data

    def get_grade(self):
        try: self.grade = self.element.getElementsByTagName("grade")[0].childNodes[0].data
        except: pass

    def get_stroke_count(self):
        self.stroke_count = self.element.getElementsByTagName("stroke_count")[0].childNodes[0].data

    def get_on_and_kun(self):
        for reading in self.element.getElementsByTagName("reading"):
            self.on.append(u''.join([on for on in reading.childNodes[0].data if reading.getAttribute('r_type') == 'ja_on']))
            self.kun.append(u''.join([on for on in reading.childNodes[0].data if reading.getAttribute('r_type') == 'ja_kun']))
        self.on = filter(lambda x: x, self.on)
        self.kun = filter(lambda x: x, self.kun)

    def get_meanings(self):
        # meanings that have attributes are in non-English languages
        try: self.meanings = [meaning.childNodes[0].data for meaning in self.element.getElementsByTagName("meaning") if not meaning.hasAttributes()]
        except: pass

    def get_nanori(self):
        try: self.nanori = [nanori.childNodes[0].data.encode('utf-8') for nanori in self.element.getElementsByTagName("nanori")]
        except: pass

    def setup(self):
        self.get_literal()
        self.get_grade()
        self.get_stroke_count()
        self.get_on_and_kun()
        self.get_meanings()
        self.get_nanori()

if __name__ == '__main__':
    kanjidic = KanjiToday()
    for k in kanjidic.kanji:
        print k.definitions, k.literal, '\n'
