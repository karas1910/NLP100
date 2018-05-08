from n30 import sentence_mapping
from n37 import get_feq_word
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    with open('./neko.txt.mecab') as f:
        num = 0
        sentenceL = [s for s in f.read().split('EOS\n') if s != '']
        target = sentence_mapping(sentenceL)
        result, num = get_feq_word(target, num)

        rank = len(set([tmp[1] for tmp in result]))
        x = range(1, rank+1)
        feq = np.array(list(set([ch[1] for ch in result])))

        plt.plot(x, feq, 'o')
        plt.xlabel('Ranking')
        plt.ylabel('Feq')
        plt.yscale('log')
        plt.title('Zipfの法則')
        plt.show()
