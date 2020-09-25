from random import choice
from threading import Thread

def tortoise(total_step: int):
    step = 0
    while step < total_step:
        step += 1
        print('烏龜跑了 {} 步...'.format(step))

def hare(total_step: int):
    step = 0
    flags = [True, False]
    while step < total_step:
        if choice([True, False]):
            print('兔子睡著了zzzz')
        else:
            step += 2
            print('兔子跑了 {}  步...'.format(step))

t = Thread(target = tortoise, args = (10,))
h = Thread(target = hare, args = (10,))

t.start()
h.start()
