

class control_text:
    def __init__(self, context):
        self.context  = context

    def interpret(self):
        if len(self.context) == 0:
            return
        else:
            msg = self.context.split()
            for j in msg:
                pos = 0
                for k in j:
                    if not k.isdigit():
                        pos += 1
                        continue
                hexian = j[0:pos]
                jiezou = j[pos:]
                # print(hexian, jiezou)
                self.execute(hexian, jiezou)
    def execute(self, a, b):
        s = "和弦是:%s 节奏是:%s"%(a, b)
        print(s)




if __name__ == '__main__':
    x = 'C53231323 Am53231323 F43231323 G63231323'
    y = control_text(x)
    y.interpret()