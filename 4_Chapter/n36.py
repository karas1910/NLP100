from n30 import sentence_mapping
from collections import Counter
from matplotlib.font_manager import FontProperties
import tkinter
import numpy as np
import matplotlib.pyplot as plt


def make_wordlist(target):
    wordlist = []
    for t in target:
        for l in t:
            wordlist.append(l['surface'])
    return wordlist


def get_feq_word(target, num):
    wordlist = make_wordlist(target)
    counter = Counter(wordlist)
    for word, cnt in counter.most_common(num):
        print('word: {0}, count: {1}'.format(word, cnt))
    return counter.most_common(num)


if __name__ == '__main__':
    with open('./neko.txt.mecab') as f:
        num = int(input('Input: '))
        senteceL = [s for s in f.read().split('EOS\n') if s != '']
        target = sentence_mapping(senteceL)
        result = get_feq_word(target, num)

        x = range(num)
        ch = [ch[0] for ch in result]
        feq = np.array([ch[1] for ch in result])

        fp = FontProperties(fname='/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf')
        plt.bar(x, feq)
        plt.xticks(x, ch, FontProperties=fp)
        plt.title('頻出単語 TOP10', FontProperties=fp)
        plt.show()
