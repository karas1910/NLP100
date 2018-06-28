#
# usage: python n84.py n83-tc n83-t n83-c
#


import sys
import pickle
from collections import OrderedDict
from scipy import sparse, io
from math import log


if __name__ == '__main__':
    fname_tc, fname_t, fname_c = sys.argv[1:]
    N = 68156709
    with open(fname_tc, 'rb') as ftc:
        with open(fname_t, 'rb') as ft:
            with open(fname_c, 'rb') as fc:
                print('reading file')
                counter_tc = pickle.load(ftc)
                print('complete reading {}'.format(fname_tc))
                counter_t = pickle.load(ft)
                print('complete reading {}'.format(fname_t))
                counter_c = pickle.load(fc)
                print('complete reading {}'.format(fname_c))

    t_dic = OrderedDict((key, i) for i, key in enumerate(counter_t.keys()))
    c_dic = OrderedDict((key, i) for i, key in enumerate(counter_c.keys()))

    mat_xtc = sparse.lil_matrix((len(t_dic), len(c_dic)))

    for i, (stc, ftc) in enumerate(counter_tc.items()):
        if ftc >= 10:
            t, c = stc.strip().split('\t')
            ft, fc = counter_t[t], counter_c[c]
            numerator, denominator = N*ftc, ft*fc

            x = ppmi = max(log(numerator/denominator), 0)
            mat_xtc[t_dic[t], c_dic[c]] = x

    io.savemat('n83-mat_xtc', {'mat_xtc': mat_xtc})
