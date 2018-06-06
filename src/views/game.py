from flask import url_for, render_template, request, Blueprint
from werkzeug.utils import redirect
from src.models.game import Game


game_blueprint = Blueprint('game', __name__)


@game_blueprint.route('/game', methods=['GET'])
def game_index():
    if request.method == 'GET':
        return render_template('game.jinja2')