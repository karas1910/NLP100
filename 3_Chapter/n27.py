from n26 import remove_simbol
from n25 import get_basic_info
import re


def remove_link_simbol(dict):
    p1 = re.compile('\[+')
    p2 = re.compile('\]+')
    for k, v in dict.items():
        dict[k] = p1.sub('', dict[k])
        dict[k] = p2.sub('', dict[k])
    return dict


if __name__ == '__main__':
    target = open('./jawiki-country.txt').read()
    target = get_basic_info(target)
    dict = remove_simbol(target)
    [print('{0} = {1}'.format(k, v)) for k, v in remove_link_simbol(dict).items()]
