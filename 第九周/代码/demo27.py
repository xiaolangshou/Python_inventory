#coding;utf8
from abc import ABCMeta, abstractmethod
class Person(metaclass=ABCMeta):
    def __init__(self):
        self.observe = []
        self.status = "white flag"

    @abstractmethod
    def attach(self):
        pass
    @abstractmethod
    def detach(self):
        pass
    @abstractmethod
    def notify(self):
        pass


class FaZheng(Person):
    def attach(self, person):
        self.observe.append(person)
    def detach(self, person):
        self.observe.remove(person)

    def notify(self):
        print(self.status)
        if self.status == "white flag":
            print("你们继续休息...")
        else:
            for j in self.observe:
                j.run()
            print("信号发送完毕. 大家冲啊...")


class ShiBing(metaclass=ABCMeta):
    def __init__(self, name, sub):
        self.name = name
        self.sub = sub

    @abstractmethod
    def run(self):
        pass

class JiangJun(ShiBing):
    def run(self):
        s = "我是%s 状态变成了%s, 拿起大刀冲下去!" %(self.name, self.sub.status)
        print(s)

class XiaoBing(ShiBing):
    def run(self):
        s = "我是%s状态变成了%s, 冲啊..." %(self.name, self.sub.status)
        print(s)


if __name__ ==  "__main__":
    fazheng = FaZheng()
    huangzhong = JiangJun("黄忠", fazheng)
    gongjianshou = XiaoBing("弓箭手", fazheng)
    qibing = XiaoBing("骑兵", fazheng)

    fazheng.attach(huangzhong)
    fazheng.attach(gongjianshou)
    fazheng.attach(qibing)
    fazheng.notify()

    print("##" * 10)

    fazheng.status = "red flag"
    fazheng.notify()


