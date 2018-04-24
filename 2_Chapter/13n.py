import sys
sys.path.append('../../mymodule')
import mm

def merge(data1, data2):
    result = open('./merge.txt', 'w')
    c1c2 = []
    for c1, c2 in zip(data1, data2):
        c1 = c1.replace('\n', '')
        result.write(c1 + '\t' + c2)
        c1c2.append(c1 + '\t' +c2)
    mm.chkprint(c1c2)

if __name__ == '__main__':
    col1 = open('./col1.txt').readlines()
    col2 = open('./col2.txt').readlines()
    merge(col1, col2)
