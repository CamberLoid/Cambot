import asyncio
async def test():
    print('1')
    await asyncio.sleep(1)
loop=asyncio.get_event_loop()
loop.run_forever()
