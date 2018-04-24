import re


def sec_level(target):
    p = re.compile('(==*)(.*)==*')
    return [[l, len(p.match(l).group(1))-1] for l in target if p.match(l)]


if __name__ == '__main__':
    target = open('./jawiki-country.txt').readlines()
    resutl = sec_level(target)
    [print('sec = {0}, Lv = {1}'.format(s.replace('\n', ''), n)) for s, n in (l for l in resutl)]
