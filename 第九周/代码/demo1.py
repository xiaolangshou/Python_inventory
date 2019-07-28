from abc import ABCMeta, abstractmethod


class Book(metaclass=ABCMeta):
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    @abstractmethod
    def get_price(self):
        pass

    def __str__(self):
        s = "书名: %s 作者: %s  价格:%s" % (self.name, self.author, self.price)
        return s


class DiscountBook1(Book):
    def get_price(self):
        if self.price >= 50:
            self.price = self.price * 0.8
        else:
            self.price = self.price * 0.9


class DiscountBook2(Book):
    def get_price(self):
        if self.price >= 40:
            self.price = self.price * 0.7
        else:
            self.price = self.price * 0.8


b = DiscountBook1("红楼梦", "曹雪芹", 60)
b.get_price()
print(b)
