#coding:utf8
from abc import ABCMeta, abstractmethod
class Reveiver(metaclass=ABCMeta):
    @abstractmethod
    def buy(self):
        pass

    @abstractmethod
    def sell(self):
        pass

class tencent_receiver(Reveiver):
    def buy(self):
        print("买腾讯股票")

    def sell(self):
        print("卖腾讯股票.")


class alibaba_receiver(Reveiver):
    def buy(self):
        print("买阿里股票..")
    def sell(self):
        print("卖阿里股票..")

class Command(metaclass=ABCMeta):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def stock_buy(self):
        pass
    @abstractmethod
    def stock_sell(self):
        pass

class tencent_stock_command(Command):
    def stock_buy(self):
        self.receiver.buy()

    def stock_sell(self):
        self.receiver.sell()

class alibaba_stock_command(Command):
    def stock_buy(self):
        self.receiver.buy()

    def stock_sell(self):
        self.receiver.sell()


class Invoke:
    def set_command(self, command):
        self._command = command

    def issue_command(self):
        self._command.stock_buy()

    def undo_command(self):
        self._command.stock_sell()


if __name__ == '__main__':
    zhangsan = Invoke()

    qq_recv = tencent_receiver()
    tb_recv = alibaba_receiver()

    cmd = tencent_stock_command(qq_recv)
    zhangsan.set_command(cmd)
    zhangsan.issue_command()
    zhangsan.undo_command()

    print("##"*10)

    cmd = alibaba_stock_command(tb_recv)
    zhangsan.set_command(cmd)
    zhangsan.issue_command()
    zhangsan.undo_command()



