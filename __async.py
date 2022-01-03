import asyncio

async def Show():
    print("Hello...")
    await asyncio.sleep(1)
    print("...world")

asyncio.run(Show())