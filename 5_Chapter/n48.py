#
# usage: python n48.py {file name}
#
from n41 import load_cabocha_file_chunk
import sys


def syntax_tree(target):
    stl = []
    for t in target:
        for c in t:
            tmp = []
            ml = c.morphs
            for m in ml:
                if m.pos == '名詞' and c.dst != -1:
                    tmp.append(''.join([i.surface for i in ml if i.pos != '記号']))
                    dst = c.dst
                    while(dst != -1):
                        tml = t[dst].morphs
                        tmp.append(''.join([i.surface for i in tml if i.pos != '記号']))
                        dst = t[dst].dst
                if tmp != []:
                    stl.append(tmp)
                    tmp = []
                    break
    return stl


if __name__ == '__main__':
    fn = sys.argv[1]
    target = load_cabocha_file_chunk(fn)
    stl = syntax_tree(target)

    for st in stl:
        print(' -> '.join(st))
