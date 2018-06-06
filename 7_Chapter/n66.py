#
# usage: python n66.py
# shell command: use sample -> db.artist.find({'area':'Japan'}).count()
#


from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient()
    db = client.sample
    collection = db.artist

    print(collection.find({'area': 'Japan'}).count())
