from abc import ABCMeta, abstractmethod
class Tea:
    def getName(self):
        return "茶"
    def getPrice(self):
        return 2

class Ingredients(metaclass=ABCMeta):
    def __init__(self, drink):
        self.drink = drink
    @abstractmethod
    def getName(self):
        pass
    @abstractmethod
    def getPrice(self):
        pass

class Orange(Ingredients):
    def add_orange_name(self):
        return "金桔"
    def add_orange_price(self):
        return 2
    def getName(self):
        return self.add_orange_name() + self.drink.getName()
    def getPrice(self):
        return self.add_orange_price() + self.drink.getPrice()



class Lemon(Ingredients):
    def add_lenmon_name(self):
        return "柠檬"
    def add_lemon_price(self):
        return 3
    def getName(self):
        return self.add_lenmon_name() + self.drink.getName()
    def getPrice(self):
        return self.add_lemon_price() + self.drink.getPrice()

class Ice(Ingredients):
    def add_ice_name(self):
        return "冰"
    def add_ice_price(self):
        return 0.5
    def getName(self):
        return self.add_ice_name() + self.drink.getName()
    def getPrice(self):
        return self.add_ice_price() + self.drink.getPrice()

t3 = Lemon(Ice(Tea()))
print(t3.getName())
print(t3.getPrice())

# t4 = Orange(Lemon(Ice(Tea())))
# print(t4.getName())
# print(t4.getPrice())

# t1 = Tea()
# print(t1.getName())
# print(t1.getPrice())
#
# t2 = Orange(Tea())
# print(t2.getName())
# print(t2.getPrice())
#
# t3 = Orange(Lemon(Tea()))
# print(t3.getName())
# print(t3.getPrice())

# t1 = Lemon(Tea())
# print(t1.getName())
# print(t1.getPrice())
#
# t2 = Ice(Tea())
# print(t2.getName())
# print(t2.getPrice())

# t4 = Ice(Te)
# print(t4.getName())
# print(t4.getPrice())
