##不使用工厂模式的使用 有以下代码:

from abc import ABCMeta, abstractmethod
class LeiFeng(metaclass=ABCMeta):
    @abstractmethod
    def do_something(self):
        pass
    @abstractmethod
    def do_work(self):
        pass

class Student(LeiFeng):
    def do_something(self):
        print("学生正在做好事")

    def do_work(self):
        print("学生正在干累活")

class Volunteer(LeiFeng):
    def do_something(self):
        print("志愿者正在做好事")
    def do_work(self):
        print("志愿者正在干累活")

class Staff(LeiFeng):
    def do_something(self):
        print("职工正在做好事")
    def do_work(self):
        print("职工正在干累活")


class Factory:
    @abstractmethod
    def create_new_leifeng(self):
        pass

class student_factory(Factory):
    def create_new_leifeng(self):
        return Student()

class volunteer_factory(Factory):
    def create_new_leifeng(self):
        return Volunteer()

class staff_factory(Factory):
    def create_new_leifeng(self):
        return Staff()

x = student_factory()

s1 = x.create_new_leifeng()  ##学生
s1.do_work()
s1.do_something()

s2 = x.create_new_leifeng()
s2.do_something()
s2.do_work()

y = staff_factory()
s3 = y.create_new_leifeng()
s3.do_work()
s3.do_something()

# s = Student()
# print(s.do_something(), s.do_work())
#
# v = Volunteer()
# print(v.do_something(), v.do_work())

#新增职工做好事的话
#1. 创建一个职工类  Leifeng
#2. 修改 LeiFeng_Factory ## 违背了开闭原则
# 需要对原来的类做修改 不可以的.
#
# class LeiFeng_Factory:
#     def create_new_leifeng(self, leifeng):
#         maps = {
#             "学生": Student(),
#             "志愿者": Volunteer()
#         }
#         if leifeng not in maps:
#             raise TypeError("请输入学生或志愿者")
#         else:
#             return maps[leifeng]

# x = LeiFeng_Factory().create_new_leifeng("学生")
# x.do_something()
# x.do_work()

# x = LeiFeng_Factory().create_new_leifeng("学生")
# x.do_something()
# x.do_work()

# x = LeiFeng_Factory().create_new_leifeng("学生")
# x.do_something()
# x.do_work()


# x = LeiFeng_Factory().create_new_leifeng("职工")
# x.do_something()
# x.do_work()