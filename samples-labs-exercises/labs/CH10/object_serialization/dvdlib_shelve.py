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

	# 實作 save、all、load、remove
	


dao = DvdDao('dvdlib.shelve')
dvd1 = DVD('Birds', 2018, 1, 'Justin Lin')
dvd2 = DVD('Dogs', 2018, 7, 'Monica Huang')

dao.save(dvd1)
dao.save(dvd2)
print(dao.all())
print(dao.load('Birds'))
dao.remove('Birds')
print(dao.all())
