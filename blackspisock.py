import sqlite3
from sqlite3 import *





db = sqlite3.connect('black.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users(
    login TEXT
)""")

db.commit()
db.close()


def add_black(user_id):
    db = sqlite3.connect('black.db')
    sql = db.cursor()
    sql.execute(f"insert into users values (?)", (user_id))
    db.commit()
    db.close()




def black_spisok(user_id):
    db = sqlite3.connect('black.db')
    sql = db.cursor()
    sql.execute(f"insert into users values (?)", (user_id,))
    db.commit()
    db.close()


black_spisok(15)