import time
import random
import threading


def loop(time=0):
    print('%s is start running...' % threading.current_thread().name)
    time.sleep(time)
    print('%s is end running...' % threading.current_thread().name)


if __name__ == '__main__':

    task = []

    for i in range(5):
        t = threading.Thread(target=loop, args=i, name='LoopThread')
        task.append(t)

    print('%s is running...' % threading.current_thread().name)
    for j in task:
        j.start()
        j.join()

    print('%s ended.' % threading.current_thread().name)
