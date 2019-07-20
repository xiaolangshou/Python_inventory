from abc import ABCMeta, abstractmethod

class staff:
    def successor(self, person):
        self.person = person
    @abstractmethod
    def handler(self, *args, **kwargs):
        pass

class group_leader(staff):
    def __init__(self, successor):
        self.successor = successor
    def handler(self, day):
        if day >= 1  and day <= 3:
            print("组长批准了你的假期 请假%s天"%day)
        else:
            print("组长同意了 但是需要下一个流程审批")
            self.successor.handler(day)
class team_leader(staff):
    def __init__(self, successor):
        self.successor = successor
    def handler(self, day):
        if day > 3 and day <= 7:
            print("经理同意了你的请假申请 请假%s天"%day)
        else:
            print("经理同意了 但是还需要下一个流程审批")
            self.successor.handler(day)

class company_vp(staff):
    def handler(self, day):
        if day > 7:
            print("VP同意了你的请假申请!")




if __name__ == '__main__':
    lilei = company_vp()
    tom =  team_leader(lilei)
    zhanglong = group_leader(tom)

    zhanglong.handler(10)

