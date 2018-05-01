import urllib.request, urllib.parse
from n25 import get_basic_info
from n26 import remove_simbol
from n27 import remove_link_simbol
from n28 import remove_markups
import requests
import re


def get_url(dc):
    url_base = 'https://commons.wikimedia.org/w/api.php?'
    url_prefix = 'action=query&titles=File:'
    url_file = dc['国旗画像'].replace(' ', '_')
    url_suffix = '&prop=imageinfo&iiprop=url&format=json'
    url = url_base + url_prefix + url_file + url_suffix

    data = requests.get(url)
    print(data.text)
    return re.search(r'"url":"(.+?)"', data.text).group(1)


if __name__ == '__main__':
    target = open('./jawiki-country.txt').read()
    target = remove_simbol(get_basic_info(target))
    dict = remove_markups(remove_link_simbol(target))
    print(get_url(dict))
