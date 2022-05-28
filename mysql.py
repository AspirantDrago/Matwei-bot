import sqlite3
from sqlite3 import *


proverka_tablica = False

db = sqlite3.connect('bazadanna.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    promo TEXT,
    cash BIGINT

)""")

db.commit()
db.close()


def add(user_id):
    db = sqlite3.connect('bazadanna.db')
    sql = db.cursor()
    sql.execute(f"insert into users values (?, 0, 0)", (user_id,))
    db.commit()
    db.close()


def proverka(user_id):
    db = sqlite3.connect('bazadanna.db')
    sql = db.cursor()
    global proverka_tablica
    vce = sql.execute("SELECT login From users WHERE login == ?", (user_id, )).fetchone()
    return vce
    db.commit()
    db.close()

