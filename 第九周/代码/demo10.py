
class fireAlert:
    def run(self):
        print("this is firealert")

class waterPush:
    def run(self):
        print("start push water")

class callPhone:
    def run(self):
        print("call 119...")


class fadeMode:
    def __init__(self):
        self.fire = fireAlert()
        self.water = waterPush()
        self.call = callPhone()
    def small_fire(self):
        self.fire.run()
        self.water.run()
    def big_fire(self):
        self.fire.run()
        self.water.run()
        self.call.run()

if __name__ == '__main__':
     f = fadeMode()
     f.small_fire()
     print("##")
     f.big_fire()