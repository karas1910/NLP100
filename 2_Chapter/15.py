import sys
sys.path.append('../../mymodule')
import mm

def tailN(target, n):
    for i in range(len(target)-n, len(target)):
        print(target[i], end='')
    result = target[len(target)-n:len(target)]
    mm.chkprint(result)


if __name__ == '__main__':
    f = open('./hightemp.txt').readlines()
    n = int(input('自然数Nを入力してください > '))
    tailN(f, n)
