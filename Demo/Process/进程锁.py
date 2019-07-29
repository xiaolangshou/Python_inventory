import time
import multiprocessing
import sys


def f1(stream):
    # with lock:
    #     time.sleep(0.1)
        stream.write("hello!!!\n")


def f2(stream):
    # with lock:
    #     time.sleep(1)
        stream.write("world!!!\n")


lock = multiprocessing.Lock()
task = []

for _ in range(5):
    # m1 = multiprocessing.Process(target=f1, args=(sys.stdout, lock))
    # m2 = multiprocessing.Process(target=f2, args=(sys.stdout, lock))
    m1 = multiprocessing.Process(target=f1, args=(sys.stdout,))
    m2 = multiprocessing.Process(target=f2, args=(sys.stdout,))
    task.extend([m1, m2])

for j in task:
    j.start()

for j in task:
    j.join()
