import sqlite3
from sqlite3 import *


db = sqlite3.connect('bazadanna_admin.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS admin(login TEXT,password TEXT)""")

db.commit()
db.close()

def add_admin(user_id):
    db = sqlite3.connect('bazadanna_admin.db')
    sql = db.cursor()
    sql.execute(f"insert into users values (?, 0, 0)", (user_id,))
    db.commit()
    db.close()



def proverka_admin(user_id):
    db = sqlite3.connect('bazadanna_admin.db')
    sql = db.cursor()
    global proverka_tablica
    vce = sql.execute("SELECT login From users WHERE login == ?", (user_id, )).fetchone()
    return vce
    db.commit()
    db.close()

