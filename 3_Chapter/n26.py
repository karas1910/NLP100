import re
from n25 import get_basic_info


def remove_simbol(dict):
    dc = {}
    p = re.compile('\'+')
    for k, v in dict.items():
        dc[k] = p.sub('', v)
    return dc


if __name__ == '__main__':
    target = open('./jawiki-country.txt').read()
    dict = get_basic_info(target)
    [print('{0} = {1}'.format(k, v)) for k, v in remove_simbol(dict).items()]
