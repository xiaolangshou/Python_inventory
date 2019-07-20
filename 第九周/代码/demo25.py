from abc import ABCMeta, abstractmethod

class cash_money(metaclass=ABCMeta):
    @abstractmethod
    def accept_money(self, *args, **kwargs):
        pass

class cash_normal(cash_money):
    def accept_money(self, value):
        return value
class cash_discount(cash_money):
    def __init__(self, percent):
        self.percent = percent
    def accept_money(self, value):
        return value * self.percent

class  cash_cheap(cash_money):
    def __init__(self, money, cheap):
        self.money =money  #满xx
        self.cheap = cheap #减xx
    def accept_money(self, value):
        if value < self.money:
            return value
        else:
            x = value - int(value / self.money) * self.cheap
            return x

class machine:
    def __init__(self, policy):
        self.policy = policy

    def getResult(self, value):
        print("You name pay %s"%self.policy.accept_money(value))

normal = cash_normal()
discount = cash_discount(0.8)
cheap = cash_cheap(100, 20)

x = machine(cheap)
x.getResult(310)


