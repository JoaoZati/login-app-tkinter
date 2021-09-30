from tkinter import *
import sqlite3


class Database:
    def __init__(self, database):
        self.conection = sqlite3.connect(database)
        self.cursor = self.conection.cursor()
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS 'users' "
                            "(id INTEGER PRIMARY KEY, user TEXT NOT NULL UNIQUE, password TEXT NOT NULL)")
        self.conection.commit()

    def select_data(self):
        self.cursor.execute(f"SELECT * FROM users")
        rows = self.cursor.fetchall()
        return rows

    def insert_data(self, username: str, password: str):
        self.cursor.execute(f"INSERT INTO users VALUES (NULL, '{username}', '{password}')")
        self.conection.commit()

    def search_data(self, username="", password=""):
        self.cursor.execute(f"SELECT * FROM users WHERE user='{username}' AND password='{password}'")
        rows = self.cursor.fetchall()
        if rows:
            return True

    def delete_data(self, id: int):
        self.cursor.execute("DELETE FROM users WHERE id=?", (id,))
        rows = self.cursor.fetchall()
        self.conection.commit()
        return rows

    def __del__(self):
        self.conection.close()


if __name__ == '__main__':
    users = Database('users.db')
    # users.insert_data('joaozati', '123')
    # users.insert_data('molina', '456')
    # users.delete_data(3)
    print(users.select_data())
    # print(bool(users.search_data('joaozati', '123')))
    
