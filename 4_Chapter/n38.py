from n30 import sentence_mapping
from n37 import get_feq_word
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    with open('./neko.txt.mecab') as f:
        num = int(input('Input number(0: all): '))
        sentenceL = [s for s in f.read().split('EOS\n') if s != '']
        target = sentence_mapping(sentenceL)
        result, num = get_feq_word(target, num)
        for word, cnt in result:
            print('word: {0}, count: {1}'.format(word, cnt))
        x = range(num)
        feq = np.array([ch[1] for ch in result])

        plt.hist(feq, log=True)
        plt.title('Histgram')
        plt.xlabel('feq')
        plt.ylabel('Vocabulary')
        plt.show()
