#
# usage: python n68.py
#


from pymongo import MongoClient
import pymongo


if __name__ == '__main__':
    client = MongoClient()
    db = client.sample
    collection = db.artist

    dance = collection.find({'tags.value': 'dance'})
    dance = dance.sort('rating.count', pymongo.DESCENDING)

    for i, v in enumerate(dance[:10], start=1):
        vname, vrating = v['name'], str(v['rating']['count'])
        print("{0:2d}".format(i), vname.ljust(20), vrating)


