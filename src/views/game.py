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
    return render_template('game.jinja2')