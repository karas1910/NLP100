import re


def get_media_file(target):
    p = re.compile('(.*)ファイル:(.*\....g?)(.*)')
    return [m.group(2) for m in (p.match(l) for l in target) if m]


if __name__ == '__main__':
    target = open('./jawiki-country.txt').readlines()
    result = get_media_file(target)
    [print(l) for l in result]
