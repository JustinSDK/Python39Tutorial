from typing import Protocol
from abc import abstractmethod

class Duck(Protocol):
    @abstractmethod
    def quack(self):
        pass
        
class Donald(Duck):
    def quack(self):
        print('我會呱呱叫')
        
duck: Duck = Donald()
duck.quack()
