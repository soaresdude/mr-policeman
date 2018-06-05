from flask import Flask, render_template
from src.models.database import Database
from dynaconf import settings


app = Flask(__name__)
app.secret_key = settings.SECRET_KEY
app.debug = True


@app.before_first_request
def init_database():
    Database.initialize()


@app.route('/')
def home():
    return render_template('home.jinja2')
