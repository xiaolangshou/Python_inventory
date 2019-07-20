class Logging:

    def __init__(self):
        pass

    def collectLog(self):
        print("collect log...")


class Anaylise:

    def __init__(self):
        pass

    def analayse(self):
        print("analayse log...")


class Client:

    def __init__(self):
        pass

    def act(self):
        log = Logging()
        log.collectLog()

        anali = Anaylise()
        anali.analayse()


if __name__ == '__main__':
    c = Client()
    c.act()
