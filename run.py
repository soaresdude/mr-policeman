from app import app
from dynaconf import settings
from livereload import Server


server = Server(app.wsgi_app)
server.serve(debug=settings.DEBUG, port=settings.PORT)
