#!/usr/lib/python3.8
# -*-coding:utf-8 -*

"""
Alexander DELAPORTE - CRLAO
https://tekipaki.hypotheses.org/
https://github.com/alxdrdelaporte/
https://gitlab.com/alxdrdelaporte

Detect encoding with chardet for multiple files and create a .tsv file with output.
INPUT
Path to the repository containing the files (browsed recursively)
OUTPUT
.tsv file (3 columns = file number, encoding, confidence)
"""


from chardet.universaldetector import UniversalDetector
import glob
import csv


input_path = "corpus/**/*.html"
output_path = "encoding_table_test.tsv"


# write output file
with open(output_path, 'w', encoding='utf-8', newline='') as table:
    file_num = 0
    # output file headers
    fieldnames = ['File number', 'Encoding', 'Confidence']
    writer = csv.DictWriter(table, fieldnames=fieldnames, delimiter='\t')
    writer.writeheader()
    detector = UniversalDetector()
    # browse input repository
    for filename in glob.glob(input_path, recursive=True):
        file_num += 1
        print(filename.ljust(60))
        detector.reset()
        for line in open(filename, 'rb'):
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        print(detector.result)
        # data = one line of data in output .tsv file
        data = {'File number': file_num, 'Encoding': detector.result['encoding'],
                'Confidence': detector.result['confidence']}
        writer.writerow(data)
