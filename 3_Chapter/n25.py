import re


def get_basic_info(target):
    dict = {}
    p1 = re.compile('{{基礎情報 国\n(.*)\n}}\n', re.S)
    p2 = re.compile('\n?\|(.*) = (.*)')
    matchDB = p1.findall(target)[0].split('\n')

    for l in matchDB:
        tmp = p2.match(l)
        if tmp:
            dict[tmp.group(1)] = tmp.group(2)
    return dict


if __name__ == '__main__':
    target = open('./jawiki-country.txt').read()
    result = get_basic_info(target)
    [print('{0} = {1}'.format(k, v)) for k, v in result.items()]
