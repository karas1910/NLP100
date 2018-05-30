import sys
import xml.etree.cElementTree as ET

if __name__ == '__main__':
    fname = sys.argv[1]
    froot = ET.parse(fname)
    for ner, hname in zip(froot.iter('NER'), froot.iter('word')):
        if ner.text == 'PERSON':
            print(hname.text)
