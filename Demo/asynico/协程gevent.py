import gevent
import time
import random


# def foo():
#     print('func 1 start...')
#     gevent.sleep(3)
#     print('func 1 end...')
#
#
# def bar():
#     print('func 2 start...')
#     gevent.sleep(1)
#     print('func 2 end...')
#
#
# if __name__ == '__main__':
#     a = time.time()
#     gevent.joinall([gevent.spawn(foo), gevent.spawn(bar)])
#     b = time.time()
#     print("cost time is %s" %(b - a))

def task(i):
    sleep = random.randint(1, 2)
    gevent.sleep(sleep)
    print("task %s sleep %ss" % (i, sleep))


def ssync():
    for i in range(1, 5):
        task(i)


def aasync():
    result = []
    for i in range(1, 5):
        result.append(gevent.spawn(task, i))
    gevent.joinall(result)


if __name__ == '__main__':
    beg = time.time()
    ssync()
    end = time.time()
    print('sync cost time %s' % (end - beg))

    beg = time.time()
    aasync()
    end = time.time()
    print('async cost time %s' % (end - beg))
