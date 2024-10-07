import sqlite3
import string
import random

class Database():
    def __init__(self, path, password) -> None:
        self.base = sqlite3.connect(path)
        self.cursor = self.base.cursor()
        self.password = password

    def showPass() -> list:
        pass

    def storePass() -> None:
        pass

    def deletePass() -> None:
        pass

