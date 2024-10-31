import sqlite3

class Database():
    def __init__(self, path, password) -> None:
        self.DATABASE = sqlite3.connect(path)
        self.CURSOR = self.DATABASE.cursor()
        self.TABLENAME = "Senhas"
        
        self.password = password

        self.verifyTable()

    def verifyTable(self) -> None:
        self.CURSOR.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.TABLENAME}'")
        if self.CURSOR.fetchone() is None:
            self.CURSOR.execute(f"CREATE TABLE {self.TABLENAME} (id INTEGER PRIMARY KEY, email TINYTEXT, site TINYTEXT, password TINYTEXT)")
            self.DATABASE.commit()
    
    def showPass(self) -> list:
        return self.CURSOR.execute(f"SELECT * FROM {self.TABLENAME}")

    def storePass(self, cryptPassword, cryptSite, cryptUser) -> None:
        self.CURSOR.execute(f"INSERT INTO {self.TABLENAME} (email, site, password) VALUES (?, ?, ?)", (cryptUser, cryptSite, cryptPassword))
        self.DATABASE.commit()

    def deletePass(self) -> None:
        pass

