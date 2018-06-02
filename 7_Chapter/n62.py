#
# usage: python n62.py {db name}
#

import sys
import plyvel as pl


if __name__ == '__main__':
    dbname = sys.argv[1]
    my_db = pl.DB(dbname)
    area = input('Input area : ').encode()
    acnt = 0

    for key, value in my_db.iterator():
        if value == area:
            acnt += 1
    print(acnt)
