from queue import Queue
from threading import Thread

def producer(clerk: Queue):
    for product in range(10):
        clerk.put(product)
        print(f'店員進貨 ({product})')

def consumer(clerk: Queue):
    for product in range(10):
        print(f'店員賣出 ({clerk.get()})')

clerk: Queue = Queue(1);
Thread(target = producer, args = (clerk, )).start()
Thread(target = consumer, args = (clerk, )).start()
