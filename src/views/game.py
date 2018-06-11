from flask import render_template, Blueprint
from src.models.node import *
from src.models.edge import *


game_blueprint = Blueprint('game', __name__)


@game_blueprint.route('/')
def index():
    Database.initialize()
    Database.remove(NODE_COLLECTION)
    Database.remove(EDGE_COLLECTION)
    Node.fill_mongo()
    Edge.fill_mongo()

    list_of_nodes = []
    beginning_node = [doc for doc in Node.fetch_nodes({'name':'l'})]

    for e in range(5):
        edges = [doc for doc in Edge.fetch_edges({
            'start_node':beginning_node[0]['name']})]
        seq = [doc['centrality'] for doc in edges]
        used_edge = Database.find_one(EDGE_COLLECTION, {'start_node':
                                                            beginning_node[
                                                                0]['name'],
                                                        'centrality': max(seq)})
        list_of_nodes.append(beginning_node[0]['name'] + '->')
        beginning_node[0]['name'] = used_edge['end_node']

    return render_template('game.jinja2', list=list_of_nodes)