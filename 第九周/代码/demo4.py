

class t:
    def f1(self):
        print("t f1")

    def f2(self):
        print("t f2")

class s(t):
    def talk(self):
        print('this is f talk')


# o1 = s()  ##s是子类
# o2 = t()  ##t是基类
# # 代码中引用基类的地方 都可以 用子类做替换 反之 不行
# # 不行的 代码中引用子类的地方可以用父类来做替换 (不行的)
#
# # o1.f1()
# # o1.f2()
# #
# # o1.talk()  ##子类中有talk方法
# # o2.talk() ##报错的  因为o2中没有talk方法

#子类应该对父类做扩展而不要改变父类的原有的功能
## 里氏替换原则
#  1. 子类应该对父类做扩展而不要改变父类的原有的功能
#  2. 在代码中引用基类的地方都可以用其子类做替换.


##如何


# class A:
#     def func1(self, a, b):
#         return a - b

# a1 = A()
# print("3 - 2 = %s" %a1.func1(3, 2))
# print("5 - 3 = %s" %a1.func1(5, 3))

#需求变更:
# 新的类中有两个方法  方法1：相减  方法2: 两数相加 再 加 100


# class B(A):
#     def func1(self, a, b):
#         return a + b
#     def func2(self, a, b):
#         return self.func1(a, b) + 100
#
# b = B()
# print("3 - 2 = %s" %b.func1(3, 2))
# print("5 - 3 = %s" %b.func1(5, 3))

from abc import ABCMeta, abstractmethod

class ab(metaclass=ABCMeta):
    @abstractmethod
    def func1(self, x, y):
        pass

    @abstractmethod
    def func2(self):
        pass

class A(ab):
    def func1(self, x, y):
        return x - y

class B(ab):
    def func1(self, x, y):
        return x + y
    def func2(self, x, y):
        return self.func1(x, y) + 100