#
# usage: python n70.py rt-polarity.neg rt-polarity.pos
#


import sys
import random


if __name__ == '__main__':
    fneg, fpos = sys.argv[1], sys.argv[2]
    neg, pos = open(fneg).readlines(), open(fpos).readlines()
    neg = ['-1 '+n for n in neg]
    pos = ['+1 '+p for p in pos]

    with open('sentiment.txt', 'w') as fout:
        concatenate = pos + neg
        ncnt, pcnt = 0, 0
        random.shuffle(concatenate)
        for c in concatenate:
            if c[:2] == '-1':
                ncnt += 1
            if c[:2] == '+1':
                pcnt += 1
            fout.write(c)
        print(ncnt, pcnt, len(concatenate))
