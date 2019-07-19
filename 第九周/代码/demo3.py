from abc import ABCMeta, abstractmethod
class better_student(metaclass=ABCMeta):
    @abstractmethod
    def de(self):
        pass
    @abstractmethod
    def mei(self):
        pass
    @abstractmethod
    def lao(self):
        pass

class better_ti_student(metaclass=ABCMeta):
    @abstractmethod
    def ti(self):
        pass

class better_zhi_student(metaclass=ABCMeta):
    @abstractmethod
    def zhi(self):
        pass

class top_ti_student(better_ti_student):
    def ti(self):
        print("体育好")

class top_zhi_student(metaclass=ABCMeta):
    def zhi(self):
        print("有智慧")

class top_student(better_student):
    def de(self):
        print("品德好")
    def mei(self):
        print("会画画")
    def lao(self):
        print("爱劳动")






class top_ten_student(top_student, top_ti_student, top_zhi_student):
    pass

class Judge:
    def __init__(self, student):
        self.student = student
    def show(self):
        self.student.de()
        self.student.zhi()
        self.student.ti()
        self.student.mei()
        self.student.lao()

lilei = top_ten_student()
Judge(lilei).show()

print("##")
tom = top_ti_student()
tom.ti()
print("##")
hanmei = top_zhi_student()
hanmei.zhi()
##需求 我想要单独的评比出体育好的

