from dataclasses import dataclass
import os.path
import sqlite3

db_name = 'dvd_lib.sqlite3'

def connect(name: str) -> sqlite3.Connection:
    create = not os.path.exists(name)
    conn = sqlite3.connect(name)
    if create:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE dvds ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, "
            "title TEXT NOT NULL, "
            "year INTEGER NOT NULL, "
            "duration INTEGER NOT NULL, "
            "director_id TEXT NOT NULL)")
        conn.commit()

    return conn

@dataclass
class DVD:
    title: str
    year: int
    duration: int
    director: str

    def save(self):
        with connect(db_name) as conn:
            conn.cursor().execute("INSERT INTO dvds (title, year, duration, director_id) VALUES (?, ?, ?, ?)",
                                  (self.title, self.year, self.duration, self.director))

    @staticmethod
    def load(title: str) -> 'DVD':
        with connect(db_name) as conn:
            c = conn.cursor()
            fields = c.execute('SELECT title, year, duration, director_id FROM dvds WHERE title =?', (title,)).fetchone()
            return DVD(*fields)

dvd1 = DVD('Birds', 2020, 9, 'Justin Lin')
dvd1.save()
dvd2 = DVD.load('Birds')
print(dvd2) # 顯示 DVD(title='Birds', year=2020, duration=9, director='Justin Lin')

