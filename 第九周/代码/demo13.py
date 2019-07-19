

class Role:
    def __init__(self, role_type, wuqi, kuijia, tedian):
        self.role_type = role_type
        self.wuqi = wuqi
        self.kuijia = kuijia
        self.tedian = tedian

    def __str__(self):
        s = "士兵类型: %s 武器: %s 着装:%s 特点:%s"%(self.role_type
                                           , self.wuqi, self.kuijia,
                                           self.tedian)
        return s

r1 = Role("步兵", '刀', '盔甲', '灵活')
print(r1)
#使用享元模式 来提取公共的数据 来节约资源

class Person:
    pool = {}
    def __new__(cls, *args, **kwargs):
        role_type = kwargs.get("role_type") ##步兵,,
        t = cls.pool.get(role_type, None)
        if not t:
            t = object.__new__(cls)
            cls.pool[role_type] = t
            t.role_type = role_type
        else:
            pass
        return t

    def render(self, wuqi, zhuozhuang, tedian):
        s = "士兵类型: %s 武器: %s 着装:%s 特点:%s"%(self.role_type
                                           , wuqi, zhuozhuang,
                                           tedian)
        return s



r1 = Person(role_type="步兵")
r2 = Person(role_type="步兵")
print(id(r1))
print(id(r2))
print(r1.render("刀", "盔甲", "灵活"))
print(r2.render("弓箭", "盔甲", "灵活"))


r3 = Person(role_type="藤甲兵")
r4 = Person(role_type="藤甲兵")
print(r3.render("长矛", "藤甲", "刀枪不入"))
print(r4.render("长矛", "藤甲", "刀枪不入"))

print(len(Person.pool))


r1.xueye = 100
print(r1.xueye)
print(r2.xueye)

r1.xueye = 90
print(r1.xueye)
print(r2.xueye)





