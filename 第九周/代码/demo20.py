from abc import ABCMeta, abstractmethod

class Bike:
    @property
    def tire(self):
        return self.__tire
    @tire.setter
    def tire(self, value):
        self.__tire = value
    @property
    def frame(self):
        return self.__frame
    @frame.setter
    def frame(self, value):
        self.__frame = value
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

class bike_bulder(metaclass=ABCMeta):
    @abstractmethod
    def build_frame(self):
        pass

    @abstractmethod
    def build_tire(self):
        pass

    @abstractmethod
    def build_color(self):
        pass

class ofo_bike_bulder(bike_bulder):
    def __init__(self):
        self.bike = Bike()
    def build_color(self):
        self.bike.color = "yello"
    def build_frame(self):
        self.bike.frame = "small"
    def build_tire(self):
        self.bike.tire = "black"
    def __str__(self):
        s = "颜色: %s 框架:%s 轮胎:%s"%(self.bike.color,  self.bike.frame, self.bike.tire)
        return s

class mb_bike_bulder(bike_bulder):
    def __init__(self):
        self.bike = Bike()

    def build_tire(self):
        self.bike.tire = "sliver"
    def build_frame(self):
        self.bike.frame = "big"
    def build_color(self):
        self.bike.color = "orange"
    def __str__(self):
        s = "颜色: %s 框架:%s 轮胎:%s"%(self.bike.color,  self.bike.frame, self.bike.tire)
        return s

class xm_bike_bulder(bike_bulder):
    def __init__(self, bikeObj):
        self.bikeObj = bikeObj


class bike_builder_factory:
    def __init__(self, bikeObj):
        self.bikeObj = bikeObj
    def make(self):
        self.bikeObj.build_tire()
        self.bikeObj.build_frame()
        self.bikeObj.build_color()

o1 = ofo_bike_bulder()
o1_build = bike_builder_factory(o1)
o1_build.make()
print(o1)
