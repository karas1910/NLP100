from n30 import sentence_mapping
from n36 import get_feq_word
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    with open('./neko.txt.mecab') as f:
        num = 10
        sentenceL = [s for s in f.read().split('EOS\n') if s != '']
        target = sentence_mapping(sentenceL)
        result, num = get_feq_word(target, num)
        for word, cnt in result:
            print('word: {0}, count: {1}'.format(word, cnt))
        x = range(num)
        ch = [ch[0] for ch in result]
        feq = np.array([ch[1] for ch in result])

        plt.bar(x, feq)
        plt.xticks(x, ch)
        plt.title('頻出単語 TOP10')
        plt.show()
