import os


def f1():
    print('my process is is %s' % os.getpid())

    pid = os.fork()

    if pid == 0:
        print('pid is %s my father is %s' % (os.getpid(), os.getppid()))
    else:
        print('I has a son process pid is %s' % pid)


if __name__ == '__main__':
    f1()


