#
# usage: python n53.py {file name}
#


import os
import sys
import subprocess
import xml.etree.ElementTree as ET


def parse_nlp(fname_parsed, fname):
    if not os.path.exists(fname_parsed):
        subprocess.run(
            'sudo java --add-modules java.se.ee -cp \
            "/usr/local/lib/stanford-corenlp-full-2018-02-27/*"'
            ' -Xmx2g'
            ' edu.stanford.nlp.pipeline.StanfordCoreNLP'
            ' -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref'
            ' -file ' + fname,
            shell=True,
            check=True
        )


if __name__ == '__main__':
    fname = sys.argv[1]
    fname_parsed = fname + '.xml'
    parse_nlp(fname_parsed, fname)
    root = ET.parse(fname_parsed)
    for word in root.iter('word'):
        print(word.text)
