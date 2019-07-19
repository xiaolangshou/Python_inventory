class Tea:


    def get_name(self):
        return "茶"
    def get_price(self):
        return 2
    def __str__(self):
        s = "品名: %s 价格: %s" %(self.name, self.price)
        return s

class Orange:

    def add_orange_name(self):
        return "金桔"
    def add_orange_price(self):
        return 1


class Lemon:

    def add_lemon_name(self):
        return "柠檬"
    def add_lemon_price(self):
        return 3


class Ice:

    def add_ice_name(self):
        return "冰"
    def add_ice_price(self):
        return 0.5


#
class orange_lemon_ice_tea(Orange, Lemon, Ice, Tea):
    def get_name(self):

#
        return Orange.add_orange_name(self) + Lemon.add_lemon_name(self) + Ice.add_ice_name(self) + Tea.get_name(self)
#
    def get_price(self):
        return Orange.add_orange_price(self) + Lemon.add_lemon_price(self) + Ice.add_ice_price(self) + Tea.get_price(self)

x = orange_lemon_ice_tea()
print(x.get_name())
print(x.get_price())
#
#

