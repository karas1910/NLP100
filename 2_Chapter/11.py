import sys
sys.path.append("../../mymodule/")
import mm

def ttos(target):
    result = open("./hightemp-11.txt",'w')
    for t in target:
        t = t.replace('\t',' ')
        print(t, end="")
        result.write(t)
    result.close()


if __name__ == '__main__':
    f = open("./hightemp.txt")
    target = f.readlines()
    ttos(target)
    f.close()
