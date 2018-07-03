#
# usage: python n85.py n83-mat_xtc.mat
#


from scipy import io
import sklearn.decomposition
import sys


if __name__ == '__main__':
    fname_matrix_x = sys.argv[1]
    fname_matrix_x300 = 'n85-mat_xtc_300'

    matrix_x = io.loadmat(fname_matrix_x)['mat_xtc']

    clf = sklearn.decomposition.TruncatedSVD(300)
    matrix_x300 = clf.fit_transform(matrix_x)
    io.savemat(fname_matrix_x300, {'matrix_x300': matrix_x300})
