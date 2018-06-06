from src.models.database import Database


class Game(object):
    def __init__(self):
        Database.initialize()
        pass
