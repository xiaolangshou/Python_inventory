import threading
import time
# class single:
#     lock = threading.Lock()
#     def __init__(self, *args, **kwargs):
#         time.sleep(1)
#         pass
#     @classmethod
#     def instance(cls, *args, **kwargs):
#         single.lock.acquire()
#         if not hasattr(single, '_instance'):
#             single._instance = single(*args, **kwargs)
#         single.lock.release()
#         return single._instance

class single:
    lock = threading.Lock()
    def __init__(self, *args, **kwargs):
        time.sleep(1)
    def __new__(cls, *args, **kwargs):
        single.lock.acquire()
        if not hasattr(single, '_instance'):
            single._instance = object.__new__(cls)
        single.lock.release()
        return single._instance


def task():
    x = single()
    print(id(x))
#
tasks = []
for _ in range(10):
    t = threading.Thread(target=task)
    tasks.append(t)
for j in tasks:
    j.start()
for j in tasks:
    j.join()


