#
# usage: python n51.py {file name}
#


import re
import sys


def create_sentence_list(fdata):
    split_pattern, sub_pattern = (re.compile('([.;:?!])\s([A-Z])'),
                                  re.compile('\n+'))
    fdata_sub = sub_pattern.sub(' ', fdata)
    fdata_split = split_pattern.split(fdata_sub)
    tmp = [''] + [s.strip() for s in fdata_split] + ['']
    # '[A-Z] or ""' + 'sentence' + '. or ; or : or ? or !'
    fsentence_list = [''.join(tmp[i:i+3]) for i in range(0, len(tmp), 3)]
    return fsentence_list


if __name__ == '__main__':
    fname = sys.argv[1]
    fdata = open(fname).read()
    fsentence_list = create_sentence_list(fdata)

    for fs in fsentence_list:
        print(fs)
