import re
from n25 import get_basic_info
from n26 import remove_simbol
from n27 import remove_link_simbol


def remove_markups(dict):
    p1 = re.compile('\{\{(.*\||)(.*)\}\}(.*)')
    p2 = re.compile('<ref(.*)?\/?>(.*)?(<\/ref>)?')
    for k, v in dict.items():
        dict[k] = p1.sub(r'\2', dict[k])
        dict[k] = p2.sub('', dict[k])
        dict[k] = dict[k].replace('<br />', '')
    return dict


if __name__ == '__main__':
    target = open('./jawiki-country.txt').read()
    target = remove_simbol(get_basic_info(target))
    dict = remove_markups(remove_link_simbol(target))
    [print('{0} = {1}'.format(k, v)) for k, v in dict.items()]
