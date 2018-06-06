from src.models.database import Database
import uuid


class Node(object):
    def __init__(self, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return f"<Node _id: {self._id}>"

    def save(self):
        Database.save_to_mongo('nodes', self.__dict__)
