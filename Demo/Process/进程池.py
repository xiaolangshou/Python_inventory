import multiprocessing
import time
import os


def func(msg):
    time.sleep(1)
    return 'return msg %s' % msg


pool = multiprocessing.Pool(processes=3)
beg = time.time()
jobs = []
for i in range(4):
    msg = 'hello %s' % i
    jobs.append(pool.apply_async(func, (msg,)))
pool.close()
pool.join()
end = time.time()
print('cost time %s' % (end - beg))
print('subprocess done!')

for j in jobs:
    print(j.get())
