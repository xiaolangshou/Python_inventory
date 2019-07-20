from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    @abstractmethod
    def add_person(self):
        pass

    @abstractmethod
    def work(self):
        pass

class Master(Person):
    def __init__(self, name):
        self.name = name
        self.controlPerson = []

    def add_person(self, staff):
        self.controlPerson.append(staff)

    def work(self):
        print("I am a school headmaster name is %s" %self.name)
        for j in self.controlPerson:
            j.work()

class Manager(Person):

    def __init__(self, name):
        self.name = name
        self.controlPerson = []

    def add_person(self, staff):
        self.controlPerson.append(staff)

    def work(self):
        print("i am a school manager name is %s" %self.name)
        for j in self.controlPerson:
            j.work()

class Teacher(Person):
    def __init__(self, name):
        self.name = name

    def add_person(self):
        print("我只能管学生!")
    def work(self):
        print("我是%s每天都要进行枯燥的教学工作!"%self.name)


if __name__ == '__main__':
    lily = Teacher("lily")
    lucy = Teacher("lucy")
    hanmei = Teacher("hanmei")

    lilei = Manager("lilei")
    tom = Master("tom")

    #
    lilei.add_person(lily)
    lilei.add_person(lucy)
    lilei.work()

    print("##"*20)
    wangtao = Manager("wangtao")
    wangtao.add_person(hanmei)
    wangtao.work()

    print("##" * 20)

    tom.add_person(lilei)
    tom.add_person(wangtao)
    tom.work()


