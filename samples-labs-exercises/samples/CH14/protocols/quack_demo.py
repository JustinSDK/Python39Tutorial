from typing import Protocol

class Duck(Protocol):
    def quack(self):
        pass
        
class Human:
    def quack(self):
        print('我會呱呱叫')
        
human: Duck = Human()
human.quack()