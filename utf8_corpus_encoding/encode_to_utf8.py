#!/usr/lib/python3.8
# -*-coding:utf-8 -*

"""
Alexander DELAPORTE
https://tekipaki.hypotheses.org/
https://github.com/alxdrdelaporte/Tekipaki

More about this script (French) :
https://tekipaki.hypotheses.org/478

INPUT = HTML files directory with any character encoding
OUTPUT =
* 'utf8_files' directory (contents from html/text MIME type text files with utf-8 encoding)
* 'encoding_none' text file (for verification purposes)
"""


# system functions
import os
# regex
import re
# character encoding detection
import chardet


"""
DIRECTORIES & COUNTERS
"""
# input directory path
rootdir = 'raw_files'

# create 'utf-8_files' directory
os.makedirs('utf8_files', exist_ok=True)
datadir = 'utf8_files'

# counters
files_nb = 0
none_enco = 0


"""
PROCESSING
"""
# iterate through each file
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        files_nb += 1
        """
        GET FILEPATH
        """
        filepath = subdir + os.sep + file
        """
        MIME TYPE FILTER
        """
        # MIME type detection
        mimetype = os.popen("file --mime-type -b " + filepath).read()
        mimetype = mimetype.strip()
        if mimetype == "text/html":
            """
            WRITE FILES IN NEW 'utf8_files' DIRECTORY
            """
            # prepare new filepath
            fileid = re.sub("/", "REMOVEDSLASH", filepath)
            copy = datadir + "/" + fileid
            print(f"Processing {filepath}")
            try:
                # try to utf-8 decode file
                f = open(filepath, "r", 1000, encoding="utf-8").read()
                # copy in new file
                fnew = open(copy, "w", encoding="utf-8")
                fnew.write(f)
                fnew.close()
            # if decoding error encounter (= encoding is not utf-8)
            except UnicodeDecodeError:
                # encoding detection
                f = open(filepath, "rb").read()
                res = chardet.detect(f)
                enc = res['encoding']
                if enc is not None:
                    try:
                        # copy in new file with utf-8 encoding
                        fnew = open(copy, "w", encoding="utf-8")
                        fnew.write(f.decode(enc, 'ignore'))
                        fnew.close()
                    except UnicodeDecodeError:
                        print(f"Decoding error on {filepath}")
                    except UnicodeEncodeError:
                        print(f"Encoding error on {filepath}")
                    except TypeError:
                        print(f"Type error on {filepath}")
                # list of files with 'None' encoding
                else:
                    none_enco += 1
                    nope = open("encoding_none.txt", "a")
                    nope.write(filepath + "\n")
                    nope.close()
print(f"{files_nb} files read\n{none_enco} file(s) couldn't be re-encoded into utf-8 (see encoding_none.txt)")
