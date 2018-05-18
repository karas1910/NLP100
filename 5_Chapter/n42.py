from n41 import load_cabocha_file_chunk
import sys


def print_sd(target):
    for t in target:
        for c in t:
            ml = c.morphs
            ml2 = t[c.dst].morphs
            for m in ml:
                if m.pos != '記号' and c.dst != -1:
                    print(m.surface, end='')
            print('\t', end='')
            for m in ml2:
                if m.pos != '記号' and c.dst != -1:
                    print(m.surface, end='')
            print()


if __name__ == '__main__':
    fn = sys.argv[1]
    result = load_cabocha_file_chunk(fn)

    print_sd(result)
