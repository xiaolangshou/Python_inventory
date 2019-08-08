import socket
import time
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp.bind(("127.0.0.1", 5001))
tcp.listen()

while 1:
    cli, addr = tcp.accept()
    print(cli, addr)
    while 1:
        data = cli.recv(65535)
        print(data)
        s = 'abcdefghijklmn123456789'
        cli.send(bytes(s, encoding="utf-8"))
        if not data:
            break

