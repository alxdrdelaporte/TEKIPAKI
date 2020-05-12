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

# https://pypi.org/project/PyNLPIR/
import pynlpir

# initiate PyNLPIR
pynlpir.open(encoding_errors='replace')

# input file path
plain_text = '皇帝企鹅_text.txt'
# output file path
pos_tagged_text = '皇帝企鹅_text_PosTaggedPyNLPIR.txt'

with open(plain_text, 'r') as penguin, open(pos_tagged_text, 'w') as tagged_penguin:
    for line in penguin:
        if len(line) > 1:
            # POS tagging with raw NLPIR pos names (returns list of tuples)
            postag = pynlpir.segment(line, pos_names='raw')
            # converting tuples list to original NLPIR-like tags
            for segment in postag:
                tagged_segment = ""
                for word, part_of_speech in postag:
                    # if a tag is available, create tagged word
                    try:
                        tagged_word = f"{word}/{part_of_speech} "
                    # if no tag can be found, create tagged word with "None" type
                    except TypeError:
                        tagged_word = f"{word}/None "
                    tagged_segment += tagged_word
            tagged_segment = f"{tagged_segment}\n"
            tagged_penguin.write(tagged_segment)

# close PyNLPIR
pynlpir.close()
