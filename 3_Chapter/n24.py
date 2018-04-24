import re
from n23 import sec_level



target = open('./jawiki-country.txt').readlines()
result = sec_level(target)
[print('sec = {0}, Lv = {1}'.format(s.replace('\n', ''), n)) for s, n in (l for l in result)]


