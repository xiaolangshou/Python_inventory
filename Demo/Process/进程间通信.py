import multiprocessing
import time

pipe = multiprocessing.Pipe()
print(pipe)


def proc1(pipe):
    for i in range(3):
        print('send: %s' % i)
        pipe.send(i)
    pipe.close()


def proc2(pipe):
    while True:
        try:
            print('proc2 rev: %s' % pipe.recv())
            if not pipe.poll():
                break
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=proc1, args=(pipe[0],))
    p2 = multiprocessing.Process(target=proc2, args=(pipe[1],))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
