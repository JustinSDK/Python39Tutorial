from random import choice
from threading import Thread

class Tortoise(Thread):
    def __init__(self, total_step: int) -> None:
        super().__init__()
        self.total_step = total_step

    def run(self):
        step = 0
        while step < self.total_step:
            step += 1
            print('烏龜跑了 {} 步...'.format(step))

class Hare(Thread):
    def __init__(self, total_step: int) -> None:
        super().__init__()
        self.total_step = total_step

    def run(self):
        step = 0
        while step < self.total_step:
            if choice([True, False]):
                print('兔子睡著了zzzz')
            else:
                step += 2
                print('兔子跑了 {}  步...'.format(step))

Tortoise(10).start()
Hare(10).start()

