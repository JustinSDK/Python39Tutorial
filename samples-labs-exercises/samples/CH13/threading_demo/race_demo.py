from threading import Thread

def setTo1(data: dict[str, int]):
    while True:
        data['Justin'] = 1
        if data['Justin'] != 1:
            raise ValueError(f'setTo1 資料不一致：{data}')

def setTo2(data: dict[str, int]):
    while True:
        data['Justin'] = 2
        if data['Justin'] != 2:
            raise ValueError(f'setTo2 資料不一致：{data}')

data: dict[str, int] = {}

t1 = threading.Thread(target = setTo1, args = (data, ))
t2 = threading.Thread(target = setTo2, args = (data, ))

t1.start()
t2.start()

