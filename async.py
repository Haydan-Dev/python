import asyncio
import time

async def function1():
    await asyncio.sleep(2)
    print("punc-1")

async def function2():
    await asyncio.sleep(2)
    print("func-2")

async def function3():
    await asyncio.sleep(2)
    print("Func-3")

async def main():
    task = asyncio.create_task(function1())
    await function1()
    await function2()
    await function3()

asyncio.run(main())