import pymongo
import redis

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


class RedisDriver:
    def __init__(self, hots=None, port=None, pwd=None):
        hots = settings.REDIS_HOST if not hots else hots
        port = settings.REDIS_PORT if not port else port
        pwd = settings.REDIS_PSW if not pwd else pwd
        self.r = redis.Redis(host=hots, port=port, db=0, password=pwd)

    def set(self, k, v, timeout:int = None):
        if not timeout:
            self.r.set(k, v)
        elif type(timeout) is int:
            self.r.setex(k, timeout, v)
        else:
            print('格式错误')

    def get(self, k):
        v = self.r.get(k)
        if v:
            return v.decode('utf-8')
        return v


if __name__ == '__main__':
    # MongoDriver().get_data()
    redis_col = RedisDriver()
    redis_col.set('abc', 123)
    print(redis_col.get('abc'))
