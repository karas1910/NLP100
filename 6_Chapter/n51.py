#
# usage: python n51.py {file name}
#


import sys
from n50 import create_sentence_list


def get_word_list(sentence_list):
    word_list = []
    for s in sentence_list:
        tmp = s.split()
        word_list.append(tmp)
    return word_list


if __name__ == '__main__':
    fname = sys.argv[1]
    fdata = open(fname).read()
    fsentence_list = create_sentence_list(fdata)
    fword_list = get_word_list(fsentence_list)

    for sentence_i, fw in enumerate(fword_list):
        print('[{}]'.format(sentence_i+1))
        for w in fw:
            print(w)
        print()
