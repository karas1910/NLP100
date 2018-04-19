import sys
sys.path.append('../../mymodule')
import mm

if __name__ == '__main__':
    f = open('./col1.txt').readlines()
    result = set(f)
    mm.chkprint(result)

