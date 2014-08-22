import json
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('localhost', 27017)
    db = client.db
    for d in db.document.find():
        print json.dumps(d, indent=4)

    if len(list(db.people.find({'name': 'jake'}))) == 0:
        db.people.save({
            'name': 'jake',
            'cool': True,
            'num': 1,
        })

    if len(list(db.people.find({'name': 'bob'}))) == 0:
        db.people.save({
            'name': 'bob',
            'cool': False,
            'num': 9
        })

    if len(list(db.people.find({'name': 'ted'}))) == 0:
        db.people.save({
            'name': 'ted',
            'cool': False,
            'num': 21
        })

    for person in db.people.find({'cool': False}):
        print person
