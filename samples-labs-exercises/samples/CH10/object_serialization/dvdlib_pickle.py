from dataclasses import dataclass
import pickle

@dataclass
class DVD:
    title: str
    year: int
    duration: int
    director: str

    def save(self):
        filename = self.title.replace(' ', '_') + '.pickle'
        with open(filename, 'wb') as fh:
            pickle.dump(self, fh)

    @staticmethod
    def load(filename: str) -> 'DVD':
        with open(filename, 'rb') as fh:
            return pickle.load(fh)

dvd1 = DVD('Birds', 2020, 8, 'Justin Lin')
dvd1.save()
dvd2 = DVD.load('Birds.pickle')
print(dvd2)
