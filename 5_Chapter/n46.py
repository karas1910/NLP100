#
# usage: python n46.py {file name}
#
from n41 import load_cabocha_file_chunk
import sys


def create_corpus(target):
    result = []
    for t in target:
        for c in t:
            tmp1, tmp2, tmp3 = [], [], []
            ml = c.morphs
            for m in ml:
                if m.pos == '動詞':
                    for i in c.srcs:
                        jml = t[i].morphs
                        for jm in jml:
                            if jm.pos == '助詞':
                                tmp1.append(jm.base)
                                if tmp2 == []:
                                    for jm in jml:
                                        tmp2.append(jm.surface)
                        if tmp2 != []:
                            tmp3.append(''.join(tmp2))
                            tmp2 = []
                    if tmp1 != []:
                        result.append([m.base, tmp1, tmp3])
                        tmp3 = []
                        tmp1 = []
    return result


if __name__ == '__main__':
    fn = sys.argv[1]
    target = load_cabocha_file_chunk(fn)
    corpus = create_corpus(target)

    with open('n46-corpus.txt', 'w') as f:
        for k, vl1, vl2 in corpus:
            f.write(k + '\t')
            for i in range(len(vl1)):
                if i == 0:
                    f.write(vl1[i])
                else:
                    f.write(' ' + vl1[i])
            f.write('\t')
            for j in range(len(vl2)):
                if i == 0:
                    f.write(vl2[j])
                else:
                    f.write(' ' + vl2[j])
            f.write('\n')
