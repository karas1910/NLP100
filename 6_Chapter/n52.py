#
# usage: python n52.py {file name}
#


import sys
from nltk.stem.porter import PorterStemmer as PS
from n50 import create_sentence_list
from n51 import get_word_list


if __name__ == '__main__':
    fname = sys.argv[1]
    fdata = open(fname).read()
    fsentence_list = create_sentence_list(fdata)
    fword_list = get_word_list(fsentence_list)

    ps = PS()
    for fword in fword_list:
        for w in fword:
            stemw = ps.stem(w)
            if w.replace(stemw, '') != '':
                print(stemw + '\t' + w.replace(stemw, ''))
            else:
                print(w)
        print()
