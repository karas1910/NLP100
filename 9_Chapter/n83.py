#
# usage: python n83.py n82-corpus.txt n83-tc n83-t n83-c
#


import sys
import pickle
from collections import Counter


if __name__ == '__main__':
    fname_in, fname_tc, fname_t, fname_c = sys.argv[1:]
    counter_tc, counter_t, counter_c = Counter(), Counter(), Counter()
    N = 0
    with open(fname_in) as fin:
        for i, sentence in enumerate(fin):
            N += 1
            sentence_t_c = sentence.strip().split('\t')
            sentence_l = [sentence]
            counter_tc.update(sentence_l)
            counter_t.update(sentence_t_c[:1])
            counter_c.update(sentence_t_c[1:])

    with open(fname_tc, 'wb') as ftc:
        with open(fname_t, 'wb') as ft:
            with open(fname_c, 'wb') as fc:
                pickle.dump(counter_tc, ftc)
                pickle.dump(counter_t, ft)
                pickle.dump(counter_c, fc)
    print(N)
