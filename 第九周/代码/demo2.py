#聚合关系

class  student:
    def __init__(self, name):
        self.name = name
    def say(self):
        return "my name is %s" %self.name

class school:
    def __init__(self, student):
        self.student=student
    def __str__(self):
        return self.student.say()


class Room:
    def createRoom(self):
        print("创建了一个房间")

class House:
    def __init__(self):
        self.room = Room()
    def createHouse(self):
        self.room.createRoom()

#is-a  继承
#has-a  拥有关系.. 合成和聚合
#继承不能乱用 继承只适合is-a 不适合has-a的场景
## 例子 : 错误的用继承 在has-a 的情况下用继承
#对导致代码的扩展性非常差

# man  father  staff  student
# 人 和 角色之间    is-a
from abc import ABCMeta, abstractmethod
class Person(metaclass=ABCMeta):
    @abstractmethod
    def show(self):
        pass

class Father(Person):
    def show(self):
        print("在家做父亲")

class Staff(Person):
    def show(self):
        print("在公司当员工")
class Student(Person):
    def show(self):
        print("在学校是学生")

lilei = Student()
lilei.show()
print(id(lilei))
lilei = Staff()
lilei.show()
print(id(lilei))

#人 是 拥有角色
#人 has a role
#staff is a role
#student is a role
#father is a role

class Role(metaclass=ABCMeta):
    @abstractmethod
    def show(self):
        pass

class Father(Role):
    def show(self):
        print("在家做父亲")

class Staff(Role):
    def show(self):
        print("在公司当员工")
class Student(Role):
    def show(self):
        print("在学校是学生")

class Person:
    def set_role(self, role):
        self.role = role
    def get_role(self):
        self.role.show(self)

lilei = Person()
print(id(lilei))
lilei.set_role(Student)
lilei.get_role()
lilei.set_role(Staff)
print(id(lilei))
lilei.get_role()

#继承在is-a的情况下用
#has-a 表示 拥有关系 --》聚合
                        #合成关系 