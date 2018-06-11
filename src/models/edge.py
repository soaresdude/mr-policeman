from src.models.database import Database
from src.models.constants import EDGE_COLLECTION
import uuid


class Edge(object):
    def __init__(self, start_node, end_node, direction, centrality, name,
                 _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.centrality = centrality
        self.start_node = start_node
        self.end_node = end_node
        self.direction = direction
        self.name = name
        self.visited = False

    def __repr__(self):
        return f"<Edge _id: {self._id}, Start Node _id: {self.start_node}, " \
               f"End Node _id: {self.end_node} and Centrality: {self.centrality}>"

    def save(self):
        Database.save_to_mongo(EDGE_COLLECTION, self.__dict__)

    @staticmethod
    def fill_mongo():
        Edge.seed_mongo()

    @staticmethod
    def fetch_edges(query=None):
        return Database.find(EDGE_COLLECTION, query)

    @classmethod
    def seed_mongo(cls):
        cls.save(Edge(centrality=3, start_node='k', end_node='l',
                      direction='right', name='kl'))
        cls.save(Edge(centrality=5, start_node='l', end_node='m',
                      direction='right', name='lm'))
        cls.save(Edge(centrality=8, start_node='m', end_node='n',
                      direction='right', name='mn'))
        cls.save(Edge(centrality=6, start_node='n', end_node='i',
                      direction='up', name='ni'))
        cls.save(Edge(centrality=7, start_node='i', end_node='d',
                      direction='up', name='id'))
        cls.save(Edge(centrality=5, start_node='d', end_node='e',
                      direction='right', name='de'))
        cls.save(Edge(centrality=2, start_node='a', end_node='b',
                      direction='right', name='ab'))
        cls.save(Edge(centrality=1, start_node='b', end_node='c',
                      direction='right', name='bc'))
        cls.save(Edge(centrality=2, start_node='c', end_node='d',
                      direction='right', name='cd'))
        cls.save(Edge(centrality=5, start_node='g', end_node='f',
                      direction='left', name='gf'))
        cls.save(Edge(centrality=4, start_node='h', end_node='g',
                      direction='left', name='hg'))
        cls.save(Edge(centrality=3, start_node='i', end_node='h',
                      direction='left', name='ih'))
        cls.save(Edge(centrality=8, start_node='j', end_node='i',
                      direction='left', name='ji'))
        cls.save(Edge(centrality=7, start_node='q', end_node='p',
                      direction='left', name='qp'))
        cls.save(Edge(centrality=2, start_node='r', end_node='q',
                      direction='left', name='rq'))
        cls.save(Edge(centrality=6, start_node='s', end_node='r',
                      direction='left', name='sr'))
        cls.save(Edge(centrality=1, start_node='t', end_node='s',
                      direction='left', name='ts'))
        cls.save(Edge(centrality=4, start_node='u', end_node='v',
                      direction='right', name='uv'))
        cls.save(Edge(centrality=8, start_node='v', end_node='w',
                      direction='right', name='vw'))
        cls.save(Edge(centrality=9, start_node='w', end_node='x',
                      direction='right', name='wx'))
        cls.save(Edge(centrality=3, start_node='x', end_node='y',
                      direction='right', name='xy'))
        cls.save(Edge(centrality=2, start_node='a', end_node='f',
                      direction='down', name='af'))
        cls.save(Edge(centrality=4, start_node='f', end_node='k',
                      direction='down', name='fk'))
        cls.save(Edge(centrality=7, start_node='k', end_node='p',
                      direction='down', name='kp'))
        cls.save(Edge(centrality=6, start_node='p', end_node='u',
                      direction='down', name='pu'))
        cls.save(Edge(centrality=5, start_node='v', end_node='q',
                      direction='up', name='vq'))
        cls.save(Edge(centrality=6, start_node='q', end_node='l',
                      direction='up', name='ql'))
        cls.save(Edge(centrality=9, start_node='l', end_node='g',
                      direction='up', name='lg'))
        cls.save(Edge(centrality=3, start_node='g', end_node='b',
                      direction='up', name='gb'))
        cls.save(Edge(centrality=4, start_node='c', end_node='h',
                      direction='down', name='ch'))
        cls.save(Edge(centrality=2, start_node='h', end_node='m',
                      direction='down', name='hm'))
        cls.save(Edge(centrality=5, start_node='m', end_node='r',
                      direction='down', name='mr'))
        cls.save(Edge(centrality=8, start_node='r', end_node='w',
                      direction='down', name='rw'))
        cls.save(Edge(centrality=5, start_node='x', end_node='s',
                      direction='up', name='xs'))
        cls.save(Edge(centrality=6, start_node='s', end_node='n',
                      direction='up', name='sn'))
        cls.save(Edge(centrality=7, start_node='e', end_node='j',
                      direction='down', name='ej'))
        cls.save(Edge(centrality=4, start_node='j', end_node='o',
                      direction='down', name='jo'))
        cls.save(Edge(centrality=3, start_node='o', end_node='t',
                      direction='down', name='ot'))
        cls.save(Edge(centrality=1, start_node='t', end_node='y',
                      direction='down', name='ty'))
        cls.save(Edge(centrality=2, start_node='n', end_node='o',
                      direction='right', name='no'))
