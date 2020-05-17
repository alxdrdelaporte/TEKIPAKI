#!/usr/lib/python3.7
# -*-coding:utf-8 -*

"""
Alexander DELAPORTE - CRLAO
https://tekipaki.hypotheses.org/
https://github.com/alxdrdelaporte/CRLAO

POS tagging a text in Chinese with PyNLPIR (NLPIR/ICTCLAS Python wrapper)

INPUT
皇帝企鹅_text.txt file
Text extracted from the following Wikipedia page
https://zh.wikipedia.org/wiki/%E7%9A%87%E5%B8%9D%E4%BC%81%E9%B9%85

Wikipedia contents are available under the Creative Commons Attribution-ShareAlike License
维基百科 = CC BY-SA 3.0协议
https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License

OUTPUT
POS tagged .txt file
"""


# https://github.com/fxsjy/jieba
import jieba.posseg as pseg


with open('皇帝企鹅_text.txt', 'r', encoding="utf8") as penguin,\
        open('皇帝企鹅_text_PosTaggedJieba.txt', 'w', encoding="utf8") as tagged_penguin:
    for line in penguin:
        if len(line) > 1:
            line = line.replace("\n", "")
            # POS tagging with jieba
            words = pseg.cut(line)
            # reconstruct line
            tagged_segment = ""
            for w in words:
                # add tagged word + space to segment (= line)
                tagged_segment += f"{w} "
            tagged_segment = f"{tagged_segment}\n"
            # write line in output file
            tagged_penguin.write(tagged_segment)
