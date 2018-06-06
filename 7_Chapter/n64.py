#
# usaga: python n64.py {file name}
#


import sys
import json
import pymongo
from pymongo import MongoClient


if __name__ == '__main__':
    fname = sys.argv[1]
    with open(fname) as f:
        fdictl = [json.loads(line) for line in f]
        client = MongoClient()
        db = client.sample
        collection = db.artist
        collection.insert_many(fdictl)

        collection.create_index([('name', pymongo.ASCENDING)])
        collection.create_index([('aliases.name', pymongo.ASCENDING)])
        collection.create_index([('tags.value', pymongo.ASCENDING)])
        collection.create_index([('rating.value', pymongo.ASCENDING)])
