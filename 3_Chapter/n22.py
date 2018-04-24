import re


def getc_name(target):
    p = re.compile('\[\[Category:(.*)(\|?\*?\]\])')
    return [m.group(1) for m in (p.match(l) for l in target) if not m]


if __name__ == '__main__':
    target = open('./jawiki-country.txt').readlines()
    result = getc_name(target)
    [print(l) for l in result]
