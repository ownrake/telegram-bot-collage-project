import sqlite3 as sq
from app.admin.admin_handlers import string as txt

db = sq.connect("app/database/schlude.db")
cur = db.cursor()

async def db_start():
    cur.execute("""CREATE TABLE IF NOT EXISTS evenWeek(
                even_id INTEGER PRIMARY KEY AUTOINCREMENT,
                lesson INTEGER NOT NULL,
                timeLesson VARCHAR(255) NOT NULL,
                nameLesson VARCHAR(255) NOT NULL,
                cabinet INTEGER NOT NULL,
                speaker VARCHAR(255) NOT NULL
                );""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS oddWeek(
                odd_id INTEGER PRIMARY KEY AUTOINCREMENT,
                lesson INTEGER NOT NULL,
                timeLesson VARCHAR(255) NOT NULL,
                nameLesson VARCHAR(255) NOT NULL,
                cabinet INTEGER NOT NULL,
                speaker VARCHAR(255) NOT NULL
                );""")
    

    cur.execute("INSERT INTO evenWeek VALUES (11, 1, '08:20–09:40', 'ЕН.01 Элементы высшей математики', 407, 'Волкова Е. Д.')")
    cur.execute("INSERT INTO oddWeek VALUES (21, 3, '11:20–12:40', 'ОП.15 Основы проектной деятельности', 628, 'Мохначева М. Г.')")

    

    db.commit()
    db.close()

