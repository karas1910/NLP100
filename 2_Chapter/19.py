from collections import Counter
import sys
sys.path.append('../../mymodule')
import mm

if __name__ == '__main__':
    f = open('./col1.txt')
    target = f.readlines()
    counter = Counter(target)
    for word, cnt in counter.most_common():
        word = word[0:-1]
        mm.chkprint(word, cnt)
