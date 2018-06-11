from dynaconf import settings
import pymongo


class Database(object):
    URI = settings.URI
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['mr_policeman-development']

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection, query=None):
        Database.DATABASE[collection].remove(query)

    @staticmethod
    def save_to_mongo(collection, data):
        Database.DATABASE[collection].update({"_id": data['_id']}, data, upsert=True)