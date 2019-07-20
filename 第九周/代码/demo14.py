#模型 视图  控制器模式
#SOC 关注点分离  将一个应用分割成若干的部分 每个部分解决一个
#单独的关注点

#M 模型  模型是核心的部分 代表着应用的信息本源 包含数据 状态
#V 视图  是模型的可视化表现
#C 控制器
# django  spring-mvc ##   Modle ORM DB类    mybatis
# V   views
# C   模板文件
from random import randint
class Model:
    text = ["helloworld", "live a lone", "feel lonely", "very hapy"]
    def get_msg(self, index):
        try:
            x = self.text[index]
        except:
            raise IndexError("out of index")
        else:
            return x

class View:
    def show(self, msg):
        print("the message is %s" %msg)
    def error(self, msg):
        print("found error %s" %msg)
    def select(self):
        x = randint(0, 5)
        return x
import time
class Control:
    def __init__(self):
        self.m = Model()
        self.v = View()
    def run(self):
        n = 10
        while n > 0:
            time.sleep(0.2)
            try:
                index = self.v.select()
                msg = self.m.get_msg(index)
            except Exception as e:
                self.v.error(str(e))
            else:
                self.v.show(msg)
            n = n - 1

c1 = Control()
c1.run()




