# -*- coding: utf-8 -*-
"""
Wrapper for ICU word segmentation
"""
import re

from icu import BreakIterator, Locale


def _gen_words(text):
    bd = BreakIterator.createWordInstance(Locale("th"))
    bd.setText(text)
    p = bd.first()
    for q in bd:
        yield text[p:q]
        p = q


def segment(text):
    if not text:
        return []

    text = re.sub("([^\u0E00-\u0E7F\n ]+)", " \\1 ", text)
    return list(_gen_words(text))
