import pymongo

from conf import settings


class MongoDriver:

    def __init__(self, db=None, col=None, hots=None, port=None):
        hots = settings.MONGO_HOST if not hots else hots
        port = settings.MONGO_PORT if not port else port
        self.client = pymongo.MongoClient(host=hots, port=int(port))
        self.db = self.client[settings.MONGO_DB] if not db else db
        self.col = self.db[settings.MONGO_COLL] if not col else col

    def get_data(self):
        datas = self.col.find()
        for data in datas:
            yield data

    def save_data(self, data):
        if data.get('digest'):
            filter = {"digest": data["digest"]}
            self.col.update_one(filter, {'$setOnInsert': data}, upsert=True)
        else:
            self.col.update_one({"_id": data["_id"]}, {'$setOnInsert': data}, upsert=True)


if __name__ == '__main__':
    MongoDriver().get_data()
