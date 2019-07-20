class Tea:
    def getName(self):
        return "茶"
    def getPrice(self):
        return 2

class Orange:
    def add_orange_name(self):
        return "金桔"
    def add_orange_price(self):
        return 2

class Lemon:
    def add_lenmon_name(self):
        return "柠檬"
    def add_lemon_price(self):
        return 3

class Ice:
    def add_ice_name(self):
        return "冰"
    def add_ice_price(self):
        return 0.5


class orange_lemon_tea(Orange, Lemon, Tea):
    def get_name(self):
        return Orange.add_orange_name(self) + Lemon.add_lenmon_name(self) + Tea.getName(self)
    def get_price(self):
        return Orange.add_orange_price(self) + Lemon.add_lemon_price(self) + Tea.getPrice(self)

class lemon_tea(Lemon,Tea):
    def get_name(self):
        return Lemon.add_lenmon_name(self) + Tea.getName(self)
    def get_price(self):
        return Lemon.add_lemon_price(self) + Tea.getPrice(self)
# t1 = orange_lemon_tea()
# print(t1.get_name())
# print(t1.get_price())
#
# t2 = lemon_tea()
# print(t2.get_name())
# print(t2.get_price())

