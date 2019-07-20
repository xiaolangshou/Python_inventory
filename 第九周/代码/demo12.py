class Foo(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(cls)

    def __new__(cls, *args, **kwargs):
        return object.__new__(Stranger)


class Stranger(object):
    def __init__(self, c):
        self.c = c
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

x = Foo(1, 2)
print(type(x))



#new 方法不能调用自身的new来创建实例,
#会造成死循环
# a = Foo(1, 2)
# print(a, type(a))

#使用object 或者是没有血缘关系的新式类的__new__是可以的
#__new__ 生产经理  它可以决定收到生产资料究竟给谁
## 单例模式 享元模式











