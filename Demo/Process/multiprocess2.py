import time
import multiprocessing


def f1():
    time.sleep(3)
    print('this is f1')


def f2():
    time.sleep(1)
    print('this is f2')


if __name__ == '__main__':
    beg = time.time()
    # f1()
    # f2()
    p1 = multiprocessing.Process(target=f1)
    p2 = multiprocessing.Process(target=f2)

    for i in [p1, p2]:
        i.start()

    for j in [p1, p2]:
        j.join()

    end = time.time()
    print('cost time is %s' % (end - beg))
