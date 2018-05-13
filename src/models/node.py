import uuid
import json
import networkx as nx


class Node(object):
    def __init__(self, name, value, edges=None, _id=None):
        self.name = name
        self.value = value
        self.edges = None if edges is None else edges
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return f"<Node name {self.name} node value {self.value} and node " \
               f"edges {self.edges}>"

    def serialize(self):
        return json.dumps(self.__dict__)

    def save(self):
        pass

    def initialize_node(self):
        node = nx.Graph()
        node.add_node(self)

