#
# usage: python n72 sentiment.txt
#


from n71.n71 import jadge_stopword
import re
import sys


if __name__ == '__main__':
    fname = sys.argv[1]
    sentiment = open(fname)
    pattern = re.compile('[a-zA-Z0-9]')

    with open('n72-feature.txt', 'w') as feature:
        for st in sentiment:
            wl = st.split()
            wl.pop(0)
            for w in wl:
                if re.match(pattern, w) is not None:
                    if jadge_stopword(w) is False:
                        feature.write(w+'\n')
