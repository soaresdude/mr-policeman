from src.models.database import Database
from src.models.constants import NODE_COLLECTION
from string import ascii_lowercase
import uuid


class Node(object):
    def __init__(self, name, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.name = name

    def __repr__(self):
        return f"<Node _id: {self._id} and name: {self.name}>"

    def save(self):
        Database.save_to_mongo(NODE_COLLECTION, self.__dict__)

    @staticmethod
    def fill_mongo():
        for c in ascii_lowercase[:-1]:
            node = Node(c)
            node.save()
