#
# usage: python n81.py {file name1} {file name2}
#


import sys


def change_country_name(corpus, countries):
    with open(countries) as ctr:
        with open(corpus) as cps:
            with open('n81-corpus.txt', 'w') as n81_corpus:
                for cp in cps:
                    for ct in ctr:
                        cp = cp.replace(ct, ct.replace(' ', '_'))
                    n81_corpus.write(cp)


if __name__ == '__main__':
    corpus, countries = sys.argv[1:]
    change_country_name(corpus, countries)
