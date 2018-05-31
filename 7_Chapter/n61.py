#
# usage: python n61.py {file name}
#


import sys
import plyvel as pl


if __name__ == '__main__':
    dbname = sys.argv[1]
    my_db = pl.DB(dbname)
    aname = input('Input artist name : ').encode()

    for key, value in my_db.iterator(prefix=aname+b'\s'):
        key, aid = key.decode().split('\s')
        value = value.decode()
        print('(name, area, id) : ({}, {}, {})'.format(key, value, aid))
