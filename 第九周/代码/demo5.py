
##司机张三 有一辆奔驰GLC260

# class Driver:
#     def __init__(self, name):
#         self.name = name
#
#     def drive(self, benz):
#         print("司机%s driving benz" %self.name)   ##现有的方法非常不灵活
#         benz.run()

from abc import ABCMeta, abstractmethod

class Driver(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def drive(self, car):
        pass


class CarDriver(Driver):
    def drive(self, car):
        print("司机%s driving  %s" %(self.name, car.name))   ##现有的方法非常不灵活
        car.run()


class Car(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def run(self):
        pass

class Benz(Car):
    def run(self):
        print("%s is running" %self.name)

class BMW(Car):
    def run(self):
        print("%s is running"%self.name)

benz = Benz("GLC260")
bmw = BMW("x5")
d = CarDriver("张三")
d.drive(benz)
d.drive(bmw)
