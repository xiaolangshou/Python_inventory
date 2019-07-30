import asyncio
import time


async def f1(x):
    print('this is %s' % x)
    await asyncio.sleep(x)
    return 'task done! %s' % x


c1 = f1(1)
c2 = f1(2)
c3 = f1(3)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(c1), loop.create_task(c2), loop.create_task(c3)]
    print(tasks)

    beg = time.time()

    for t in tasks:
        loop.run_until_complete(t)

    for t in tasks:
        print(t.result())

    end = time.time()

    print("cost time is %s" % (end - beg))
