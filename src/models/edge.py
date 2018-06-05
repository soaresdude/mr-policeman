from src.models.database import Database
import uuid


class Edge(object):
    def __init__(self, start_node, end_node, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.centrality = 0
        self.start_node = start_node
        self.end_node = end_node

    def __repr__(self):
        return f"<Edge _id: {self._id}, Start Node _id: {self.start_node}, " \
               f"End Node _id: {self.end_node} and Centrality: {self.centrality}>"

    def save(self):
        Database.save_to_mongo('edges', self.__dict__)