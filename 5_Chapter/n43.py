from n41 import load_cabocha_file_chunk
import sys


if __name__ == '__main__':
    fn = sys.argv[1]
    target = load_cabocha_file_chunk(fn)

    for t in target:
        for c in t:
            ml, ml2, flag1, flag2 = c.morphs, t[c.dst].morphs, False, False
            s1, s2 = [], []
            if c.dst == -1:
                continue
            for m1, m2 in zip(ml, ml2):
                if m1.pos == '名詞':
                    flag1 = True
                if m2.pos == '動詞':
                    flag2 = True
                if m1.pos != '記号':
                    s1.append(m1.surface)
                if m2.pos != '記号':
                    s2.append(m2.surface)
            if flag1 and flag2:
                [print(m, end='') for m in s1]
                print('\t', end='')
                [print(m, end='') for m in s2]
                print()
        print()
