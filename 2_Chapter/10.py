import sys
sys.path.append("../../mymodule")
import mm

def wc(target):
    print(len(target))

if __name__ == '__main__':
    f = open('hightemp.txt')
    target = f.readlines()
    wc(target)

