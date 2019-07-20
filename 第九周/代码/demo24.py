from abc import ABCMeta, abstractmethod

class Ticket(metaclass=ABCMeta):
    @abstractmethod
    def login(self, username, password):
        pass
    def set_code(self, value):
        self.code  = value

    @abstractmethod
    def show(self):
        pass

class xiecheng_ticket(Ticket):
    def login(self, username, password):
        if username == "xiecheng" and password == "abc123":
            print("login xiecheng successs")
        else:
            raise ValueError("账号密码错误!")
    def show(self):
        print("携程上查询到了机票%s"%self.code)

class feizhu_ticket(Ticket):
    def login(self, username, password):
        if username == "feizhu" and password == "abc123":
            print("login feizhu success")
        else:
            raise ValueError("登录飞猪失败")

    def show(self):
        print("飞猪上查询到了机票%s"%self.code)


class ticket_agent:
    def __init__(self, support, username, password, code):
        self.support = self.__get_support(support)
        self.username = username
        self.password = password
        self.code = code

    def __get_support(self, support):
        if support == "xiecheng":
            return  xiecheng_ticket()
        elif support == "feizhu":
            return feizhu_ticket()
        else:
            raise ValueError("供应商输入失败")

    def operate_show(self):
        self.support.login(self.username, self.password)
        self.support.set_code(self.code)
        self.support.show()





if __name__ == '__main__':

    x = ticket_agent("feizhu", "feizhu", 'abc123', "HU7334")
    x.operate_show()

    # xiecheng = xiecheng_ticket()
    # xiecheng.login("xiecheng", "abc123")
    # xiecheng.set_code("HU7334")
    # xiecheng.show()
    #
    # print("##" * 20)
    #
    # feizhu = feizhu_ticket()
    # feizhu.login("feizhu", 'abc123')
    # feizhu.set_code("HU7334")
    # feizhu.show()