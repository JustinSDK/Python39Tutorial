from typing import Optional
from dataclasses import dataclass
import shelve

@dataclass
class DVD:
    title: str
    year: int
    duration: int
    director: str
    
class DvdDao:
    def __init__(self, dbname: str) -> None:
        self.dbname = dbname

    def save(self, dvd: DVD):
        with shelve.open(self.dbname) as shelve_db:
            shelve_db[dvd.title] = dvd

    def all(self) -> list[DVD]:
        with shelve.open(self.dbname) as shelve_db:
            return [shelve_db[title]
                        for title in sorted(shelve_db, key = str.lower)]

    def load(self, title: str) -> Optional[DVD]:
        with shelve.open(self.dbname) as shelve_db:
            if title in shelve_db:
                return shelve_db[title]
        return None

    def remove(self, title: str):
        with shelve.open(self.dbname) as shelve_db:
            del shelve_db[title]


dao = DvdDao('dvdlib.shelve')
dvd1 = DVD('Birds', 2020, 1, 'Justin Lin')
dvd2 = DVD('Dogs', 2020, 7, 'Monica Huang')

dao.save(dvd1)
dao.save(dvd2)
print(dao.all())
print(dao.load('Birds'))
dao.remove('Birds')
print(dao.all())
