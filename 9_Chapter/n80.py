#
# usage: python n80.py {file name}
#


import sys
import re


def remove_simbol(fname):
    with open(fname) as f:
        pattern = re.compile('[\.,!\?;:\(\)\[\]\'"]')
        for sentence in f:
            sentence = sentence.strip()
            wordl = sentence.split()
            result = (re.sub(pattern, '', w) for w in wordl
                      if re.sub(pattern, '', w) != '')
            yield ' '.join(result)


if __name__ == '__main__':
    fname = sys.argv[1]
    print('creating corpus...')
    corpus = remove_simbol(fname)
    with open('n80-corpus.txt', 'w') as out:
        out.write(' '.join(corpus))
