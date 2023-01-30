import sqlite3
import json
import random


def get_random_world():
    con = sqlite3.connect("words_db.db")

    cur = con.cursor()

    ADJF_result = cur.execute("""SELECT * FROM baseWord 
                WHERE typeWord = 'ADJF' """).fetchone()
    result1 = json.loads(ADJF_result[1])
    adf = random.choice(list(result1))

    NOUN_result = cur.execute("""SELECT * FROM baseWord
                WHERE typeWord = 'NOUN' """).fetchone()
    result2 = json.loads(NOUN_result[1])
    non = random.choice(list(result2))

    VERB_result = cur.execute("""SELECT * FROM baseWord
                WHERE typeWord = 'VERB' """).fetchone()
    result3 = json.loads(VERB_result[1])
    veb = random.choice(list(result3))

    return {'adf': adf, 'non': non, 'veb': veb}
