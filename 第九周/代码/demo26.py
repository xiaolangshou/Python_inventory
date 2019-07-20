from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass

class Low(Base):
    def __init__(self):
        self.name = "低级别告警。。"

    def run(self, value):
        print("当前的指标数值为:%s"%value)
        print("不做具体的操作!")

class High(Base):
    def __init__(self):
        self.name = "高级别的告警.."

    def run(self, value):
        print("当前指标的数值为:%s" %value)
        print("发送邮件..")

class status:
    def __init__(self):
        self.value = 0.1
        self.low = Low()
        self.high = High()

    def monitor(self):
        if self.value <= 0.5:
            self.low.run(self.value)
        else:
            self.high.run(self.value)

if __name__ == '__main__':
    x = status()
    x.monitor()
    print("##" * 10)
    x.value = 0.6
    x.monitor()