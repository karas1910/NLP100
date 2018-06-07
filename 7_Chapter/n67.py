#
# usage: python n67.py
#


from pymongo import MongoClient
import json


if __name__ == '__main__':
    name = input('Input artist name: ')
    client = MongoClient()
    db = client.sample
    collection = db.artist

    for v in collection.find({'aliases.name': name}):
        print(json.dumps(v, indent='\t', default=str))
