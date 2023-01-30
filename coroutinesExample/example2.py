# Build a coroutine called fetch_data that simulates collecting data from a db , this returns a dummy json 
# concurrentlly print out 10 to 1 every 2 seconds

import asyncio
import random

async def fetch_data():
    await asyncio.sleep(8)
    return ({"data": "result"})

async def print_nums():
    for i in range(0, 10):
        await asyncio.sleep(2)
        print(i)


async def main():
    x = asyncio.create_task(fetch_data())
    y = asyncio.create_task(print_nums())
    
    print(await x)
    await y

asyncio.run(main())