#create 3 coroutines t1, t2, t3 that prints the name of the coroutine. Call the first coroutine on main
#have t2 print out first, t1 second and t3 third
import asyncio

async def t1():
    asyncio.create_task(t2())
    await asyncio.sleep(1)
    print('t1')
    t3Res = asyncio.create_task(t3())
    await t3Res

async def t2():
    print('t2')

async def t3():
    await asyncio.sleep(2)
    print('t3')

async def main():
    #print('test')
    t1Res = await asyncio.create_task(t1())

asyncio.run(main())