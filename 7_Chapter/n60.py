#
# usage: python n60 {file name}
#


import sys
import json
import plyvel as pl


if __name__ == '__main__':
    fname = sys.argv[1]
    f = open(fname)
    f_dictl = [json.loads(line) for line in f]
    my_db = pl.DB('n60.ldb', create_if_missing=True)

    for f_dict in f_dictl:
        key = f_dict.get('name')
        value = f_dict.get('area')
        aid = str(f_dict.get('id'))
        if key is not None and value is not None and aid is not None:
            my_db.put((key+'\s'+aid).encode(), value.encode())

    my_db.close()
