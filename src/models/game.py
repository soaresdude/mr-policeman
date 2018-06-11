from src.models.database import Database
from tkinter import *


class Game:
    def __init__(self, master=None):
        Database.initialize()


root = Tk()
Game(root)
root.mainloop()
