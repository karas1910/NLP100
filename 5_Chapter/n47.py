#
# usage: python n47.py {file name} {output file name}
#
from n41 import load_cabocha_file_chunk
import sys


def create_corpus(target):
    result = []
    for t in target:
        for c in t:
            tmp1, tmp2, tmp3 = [], [], []
            cnt = 0
            flag = True
            ml = c.morphs
            for m in ml:
                if m.pos == '動詞' and flag:
                    sl = c.srcs
                    for s in sl:
                        jml = t[s].morphs
                        cnt = 0
                        for jm in jml:
                            if jm.pos1 == 'サ変接続':
                                tmp1.append(jm.surface)
                                cnt += 1
                            if jm.pos == '助詞' and jm.surface == 'を':
                                tmp1.append(jm.surface)
                                cnt += 1
                            if jm.pos == '助詞' and jm.surface != 'を':
                                st = ''.join([jm.surface for jm in jml if jm.pos != '記号'])
                                if st in tmp3:
                                    tmp2[-1] = jm.surface
                                else:
                                    tmp2.append(jm.surface)
                                    tmp3.append(st)
                        if cnt == 2:
                            tmp1.append(m.base)
                            cnt = 0
                    if len(tmp1) >= 2 and 'を' in tmp1 and tmp2 != [] and tmp3 != []:
                        result.append([tmp1, tmp2, tmp3])
                        flag = False
                    tmp1, tmp2, tmp3 = [], [], []

    return result


if __name__ == '__main__':
    fn, wfn = sys.argv[1], sys.argv[2]
    target = load_cabocha_file_chunk(fn)
    corpus = create_corpus(target)

    with open(wfn, 'w') as f:
        for t in corpus:
            f.write(''.join(t[0]))
            f.write('\t')
            f.write(' '.join(t[1]))
            f.write('\t')
            f.write(' '.join(t[2]))
            f.write('\n')
