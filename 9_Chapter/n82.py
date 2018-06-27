#
# usage: python n82.py {file name}
#


import sys
import random


def pair_word_context(fname):
    with open(fname) as corpus:
        with open('n82-corpus.txt', 'w') as fout:
            for corpus_i, line in enumerate(corpus):
                if corpus_i % 10**4 == 0:
                    print('{}...'.format(corpus_i))
                sentence = line.strip().split()

                for si, word in enumerate(sentence):

                    width = random.randint(1, 5)
                    for s_context_i in range(max(0, si-width),
                                             min(len(sentence), si+width+1)):
                        if s_context_i != si:
                            print('{}\t{}'.format(word, sentence[s_context_i]),
                                  file=fout)


if __name__ == '__main__':
    fname = sys.argv[1]
    pair_word_context(fname)
