from n40 import Morph


class Chunk:
    def __init__(self, morphs, dst):
        self.morphs = morphs
        self.dst = dst
        self.srcs = []


def load_cabocha_file_chunk(fn):
    result = []
    with open(fn) as cf:
        tmp, ml, dst = [], [], 0
        sl = cf.readlines()
        for s in sl:
            if s == 'EOS\n':
                if ml != []:
                    c = Chunk(ml, dst)
                    tmp.append(c)
                    ml = []
                if tmp != []:
                    result.append(tmp)
                    tmp = []
            elif s[0] == '*':
                if ml != []:
                    c = Chunk(ml, dst)
                    tmp.append(c)
                    ml = []
                s = s.split(' ')
                dst = int(s[2][:-1])
            else:
                s = s.replace('\t', ',')
                s = s.split(',')
                t = {'surface': s[0], 'base': s[7], 'pos': s[1], 'pos1': s[2]}
                ml.append(Morph(t))

    for rl in result:
        cnt = 0
        for c in rl:
            if c.dst != -1 and c.dst < len(rl):
                rl[c.dst].srcs.append(cnt)
            cnt += 1

    return result


if __name__ == '__main__':
    fn, num = input("file name: "), int(input("number: "))
    result = load_cabocha_file_chunk(fn)

    for c in result[num-1]:
        ml = c.morphs
        for m in ml:
            if m.pos != '記号':
                print(m.surface, end='')
        print('', c.dst)
