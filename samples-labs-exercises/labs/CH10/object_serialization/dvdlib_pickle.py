from dataclasses import dataclass
import pickle

@dataclass
class DVD:
    title: str
    year: int
    duration: int
    director: str

    # 實作 save 與 load


dvd1 = DVD('Birds', 2020, 8, 'Justin Lin')
dvd1.save()
dvd2 = DVD.load('Birds.pickle')
print(dvd2)
