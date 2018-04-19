import sys
sys.path.append('../../mymodule/')
import mm

def splitN(target, n):
    result, tmp = [], []
    count, flag = 0, True

    for t in target:
        if flag:
            tmp.append(t)
            count += 1
            if count == n:
                flag = False
                count = 0
        if not flag or t == target[-1]:
            result.append(tmp)
            tmp = []
            flag = True

    for v, k in zip(result, range(0, len(result))):
        f = open('./hightemp-15({0}).txt'.format(k+1), 'w')
        for i in v:
            f.write(i)
            print(i, end='')
        f.close()
        print('')
    mm.chkprint(result)




if __name__ == '__main__':
    f = open('./hightemp.txt').readlines()
    n = int(input('自然数Nを入力してください > '))
    splitN(f, n)
