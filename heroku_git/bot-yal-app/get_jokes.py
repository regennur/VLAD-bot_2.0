import sqlite3
import json
import random


def get_jok():
    con = sqlite3.connect("jokes_db.db")
    cur = con.cursor()
    JOKE_result = cur.execute("""SELECT * FROM baseWord1 
                WHERE typeWord = 'JOKE' """).fetchone()
    result1 = json.loads(JOKE_result[1])
    joke = random.choice(list(result1))

    return {'joke': joke}
