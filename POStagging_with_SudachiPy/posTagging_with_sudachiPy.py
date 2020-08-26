#!/usr/lib/python3.8
# -*-coding:utf-8 -*

"""
Alexander DELAPORTE - CRLAO
https://tekipaki.hypotheses.org/
https://github.com/alxdrdelaporte/
https://gitlab.com/alxdrdelaporte

POS-tagging a text file with SudachiPy (https://github.com/WorksApplications/SudachiPy).
INPUT
よさこい_text.txt Japanese UTF-8 text file
Text extracted from the following Wikipedia page
https://ja.wikipedia.org/wiki/%E3%82%88%E3%81%95%E3%81%93%E3%81%84
Wikipedia textual contents are available under the Creative Commons Attribution-ShareAlike License
クリエイティブ・コモンズ 表示-継承 3.0 非移植
https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License
OUTPUT
POS tagged text file (よさこい_text_PosTaggedSudachiPy.txt), 'token/tag' format
"""

from sudachipy import tokenizer
from sudachipy import dictionary

txt = open('よさこい_text.txt', 'r', encoding='utf-8').read()

my_tokenizer = dictionary.Dictionary().create()
mode = tokenizer.Tokenizer.SplitMode.A
"""
mode = tokenizer.Tokenizer.SplitMode.B
mode = tokenizer.Tokenizer.SplitMode.C
print([m.surface() for m in tokenizer_obj.tokenize(txt, mode)])
print([m.part_of_speech() for m in tokenizer_obj.tokenize(txt, mode)])
"""

with open('よさこい_text_PosTaggedSudachiPy.txt', 'w', encoding='utf-8') as pos_tagged:
    for m in my_tokenizer.tokenize(txt, mode):
        pos_tagged.write(f"{m.surface()}/{m.part_of_speech()[0]} ")
