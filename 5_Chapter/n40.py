import sys


class Morph:
    def __init__(self, dc):
        self.surface = dc['surface']
        self.base = dc['base']
        self.pos = dc['pos']
        self.pos1 = dc['pos1']


def load_cabocha_file(fn):
    result = []
    with open(fn) as cf:
        tmp = []
        sentenceL = cf.readlines()
        for s in sentenceL:
            if s == 'EOS\n':
                if tmp != []:
                    result.append(tmp)
                    tmp = []
            elif s[0] != '*':
                s = s.replace('\t', ',')
                s = s.split(',')
                tmp.append({'surface': s[0], 'base': s[7], 'pos': s[1], 'pos1': s[2]})
    return result


if __name__ == '__main__':
    fn = sys.argv[1]
    target = load_cabocha_file(fn)

    result = []
    for t in target:
        tmp = []
        for tt in t:
            tmp.append(Morph(tt))
        result.append(tmp)

    print([r.__dict__ for r in result[2]])
