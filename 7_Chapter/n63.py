#
# usage: python n63.py {file name}
#        Input artist name : {artist name}
#


import sys
import json
import plyvel as pl


def search_aritist_tag(my_db, aname):
    flag = 0
    for key, value in my_db.iterator(prefix=aname+b'\s'):
        flag = 1
        key, aid = key.decode().split('\s')
        values = json.loads(value.decode())

        print('Name, ID = {}, {}'.format(key, aid))

        if values is None:
            print("No tags information\n")
            continue
        for value in values:
            cnt = value.get('count')
            v = value.get('value')
            print('{}({})'.format(v, cnt))

    if flag == 0:
        print('Artist name is not registered')


if __name__ == '__main__':
    fname = sys.argv[1]
    f = open(fname)
    fdictl = [json.loads(line) for line in f]
    try:
        my_db = pl.DB('n63.ldb', create_if_missing=False)
    except pl.Error:
        my_db = pl.DB('n63.ldb', create_if_missing=True)
        for fdict in fdictl:
            kname, kid = fdict.get('name'), str(fdict.get('id'))
            key = (kname + '\s' + kid).encode()
            value = json.dumps(fdict.get('tags')).encode()
            if key is not None and value is not None:
                my_db.put(key, value)
    finally:
        aname = input('Input artist name : ').encode()
        search_aritist_tag(my_db, aname)
