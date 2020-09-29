#!/usr/lib/python3.8
# -*-coding:utf-8 -*

"""
Alexander DELAPORTE - CRLAO
https://tekipaki.hypotheses.org/
https://github.com/alxdrdelaporte/
https://gitlab.com/alxdrdelaporte

Rewrite multiple files with a different encoding.
INPUT
Path to the repository containing the files
+ Encoding table .tsv file (output from minimal_encoding_table.py script)
OUTPUT
Reencoded files set
"""

import os
import csv

encoding_table_path = 'my_corpus_encoding_table.tsv'

input_rep = "my_corpus"

os.makedirs('my_utf8_corpus', exist_ok=True)
data_rep = 'my_utf8_corpus'


with open(encoding_table_path, 'r') as encoding_table:
    reader = csv.DictReader(encoding_table, delimiter="\t")
    for row in reader:
        filepath = f"{input_rep}/{row['File']}"
        f = open(filepath, 'rb').read()
        if row['Encoding'] != '':
            copy = f"{data_rep}/{row['File']}"
            fnew = open(copy, "w", encoding="utf-8")
            fnew.write(f.decode(row['Encoding'], 'ignore'))
            fnew.close()
            print(f"Processed = {row['File']}")
        else:
            print(f"/!\ Unknown encoding = {row['File']}")
