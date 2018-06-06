#
# usaga: python n65.py
#


import json
from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient()
    fdb = client.sample
    collection = fdb.artist

    for v in collection.find({'name': 'Queen'}):
        print(json.dumps(v, indent='\t', default=str))
