#!/usr/lib/python3.8
# -*-coding:utf-8 -*

"""
Alexander DELAPORTE - CRLAO
https://tekipaki.hypotheses.org/
https://github.com/alxdrdelaporte/
https://gitlab.com/alxdrdelaporte

Detect encoding with chardet for multiple files and creates a .tsv file with output.
INPUT
Path to the repository containing the files (browsed recursively)
OUTPUT
.tsv file (2 columns = file path, encoding)
"""


from chardet.universaldetector import UniversalDetector
import glob
import csv

input_rep = "my_corpus"
input_path = f"{input_rep}/**/*.html"
output_path = "my_corpus_encoding_table.tsv"

# write output file
with open(output_path, 'w', encoding='utf-8', newline='') as table:
    # output file headers
    fieldnames = ['File', 'Encoding']
    # DictWriter object
    writer = csv.DictWriter(table, fieldnames=fieldnames, delimiter='\t')
    writer.writeheader()
    # UniversalDetector object
    detector = UniversalDetector()
    # browse input repository
    for filename in glob.glob(input_path, recursive=True):
        detector.reset()
        # detect encoding
        for line in open(filename, 'rb'):
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        # data = one line of data in output .tsv file
        current_file = str.replace(filename, f"{input_rep}\\", "")
        data = {'File': current_file, 'Encoding': detector.result['encoding']}
        # write line in output file
        writer.writerow(data)
        print(current_file)
