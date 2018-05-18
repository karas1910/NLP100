#
# usage: python n45.py {file name}
# unix_command:
# sort n45-corpus.txt | uniq -c | sort --numeric-sort --reverse > "all.txt"
# grep "^する\s$" n45-corpus.txt | sort | uniq -c | sort --numeric-sort --reverse > suru.txt
# grep "^見る\s" n45-corpus.txt | sort | uniq -c | sort --numeric-sort --reverse > miru.txt
# grep "^与える\s$" n45-corpus.txt | sort | uniq -c | sort --numeric-sort --reverse > ataeru.txt
#
from n41 import load_cabocha_file_chunk
import sys


def create_corpus(target):
    result = []
    for t in target:
        for c in t:
            tmp = []
            ml = c.morphs
            for m in ml:
                if m.pos == '動詞':
                    for i in c.srcs:
                        jml = t[i].morphs
                        for jm in jml:
                            if jm.pos == '助詞':
                                tmp.append(jm.base)
                    if tmp != []:
                        result.append([m.base, tmp])
                        tmp = []
    return result


if __name__ == '__main__':
    fn = sys.argv[1]
    target = load_cabocha_file_chunk(fn)
    corpus = create_corpus(target)

    with open('n45-corpus.txt', 'w') as f:
        for k, vl in corpus:
            f.write(k + '\t')
            for i in range(len(vl)):
                if i == 0:
                    f.write(vl[i])
                else:
                    f.write(' ' + vl[i])
            f.write('\n')
