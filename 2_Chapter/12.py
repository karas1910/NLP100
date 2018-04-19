import sys
sys.path.append('../../mymodule')
import mm

def cut(target):
    col1 = open('./col1.txt', 'w')
    col2 = open('./col2.txt', 'w')
    c1, c2 = [], []
    for t in target:
        tmp = t.split(' ')
        col1.write(tmp[0]+'\n')
        c1.append(tmp[0])
        col2.write(tmp[1]+'\n')
        c2.append(tmp[1])
    mm.chkprint(c1)
    mm.chkprint(c2)
    col1.close()
    col2.close()

if __name__ == '__main__':
    f = open('./hightemp-11.txt')
    target = f.readlines()
    cut(target)
