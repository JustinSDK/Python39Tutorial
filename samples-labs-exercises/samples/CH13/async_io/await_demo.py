import asyncio
import time
import random

async def asyncFoo(n: float):
    time.sleep(n)
    return n * random.random()

async def asyncTasks():
    r1 = await asyncFoo(1)
    r2 = await asyncFoo(r1)
    r3 = await asyncFoo(r2)
    print(r3)

asyncio.run(asyncTasks())