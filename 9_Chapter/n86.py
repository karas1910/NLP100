#
# usage: python n86.py n85-mat_xtc_300.mat
#


import pickle
from collections import OrderedDict
from scipy import io
import sys


if __name__ == '__main__':
    fname_mat300 = sys.argv[1]
    with open('./n83/n83-t', 'rb') as data_file:
        counter_t = pickle.load(data_file)

    matrix_x300 = io.loadmat(fname_mat300)['matrix_x300']
    dict_index_t = OrderedDict((key, i) for i, key in
                               enumerate(counter_t.keys()))
    print(matrix_x300[dict_index_t['States']])
