import sys
sys.path.append("../../mymodule")
import mm
import random


def typoglycemia(target):
    result = []
    for s in target:
        if len(s) > 4:
            tmp = []
            for i in range(1,len(s)-1):
                tmp.append(s[i])
            random.shuffle(tmp)
            wd = ''.join(tmp)
            result.append(s[0] + wd + s[-1])
        else:
            result.append(s)
    print(' '.join(result))


if __name__ == '__main__':
    target = input().split(" ")
    typoglycemia(target)
