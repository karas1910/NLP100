import re


def getc(target):
    ptn = re.compile('\[\[Category:')
    return [l for l in target if ptn.match(l)]


if __name__ == '__main__':
    target = open('./jawiki-country.txt').readlines()
    result = getc(target)
    [print(l, end='') for l in result]
