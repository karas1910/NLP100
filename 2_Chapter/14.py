import sys
sys.path.append('../../mymodule')
import mm

def printN(target, N):
    for n in range(0, N):
        print(target[n], end='')
    result = target[0:N]
    mm.chkprint(result)

if __name__ == '__main__':
    f = open('./hightemp.txt')
    target = f.readlines()
    N = int(input('自然数Nを入力してください > '))
    printN(target, N)
