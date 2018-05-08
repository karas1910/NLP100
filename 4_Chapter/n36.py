from n30 import sentence_mapping
from collections import Counter
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
    if num <= 0 or num > len(counter):
        num = len(counter)
    return counter.most_common(num), num


if __name__ == '__main__':
    with open('./neko.txt.mecab') as f:
        num = int(input('Input number(0: all): '))
        senteceL = [s for s in f.read().split('EOS\n') if s != '']
        target = sentence_mapping(senteceL)
        result, num = get_feq_word(target, num)
        for word, cnt in result:
            print('word: {0}, count: {1}'.format(word, cnt))
