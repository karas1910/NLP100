#
# usage: python n54.py {file name}
#


import xml.etree.cElementTree as ET
import sys


if __name__ == '__main__':
    fname = sys.argv[1]
    froot = ET.parse(fname)
    for word, lemma, pos in zip(froot.iter('word'),
                                froot.iter('lemma'),
                                froot.iter('POS')):
        print(word.text + '\t'
              + lemma.text + '\t'
              + pos.text)
