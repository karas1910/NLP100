import sys
sys.path.append('../../mymodule')
import mm

if __name__ == '__main__':
    f = open('./hightemp-11.txt').readlines()
    result = []
    for i in range(0, len(f)):
        result.append(tuple(f[i].split(' ')))
    sorted(result, key=lambda result: result[2])

    for v in result:
        print(v)

