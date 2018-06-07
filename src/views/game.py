from flask import render_template, Blueprint


game_blueprint = Blueprint('game', __name__)


@game_blueprint.route('/game')
def index():
    return render_template('game.jinja2')