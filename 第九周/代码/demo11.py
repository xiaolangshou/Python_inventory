
class Manager:
    def work(self):
        print("i am  working so hard")
    def talk(self):
        print("i have a meeting...")

class Proxy:
    def __init__(self):
        self.busy = True
    def call(self):
        if self.busy:
            return 'Manager is very busy!'
        else:
            self.manager = Manager()
            self.manager.work()
            self.manager.talk()

p = Proxy()
print(p.call())
print("###")
p.busy = False
p.call()