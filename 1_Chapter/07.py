import sys
sys.path.append("../../mymodule")
import mm

def xyz(x, y, z):
    print('{0}時の{1}は{2}'.format(x,y,z))


if __name__ == '__main__':
    x, y, z = 12, "気温", 22.4
    xyz(x, y, z)
