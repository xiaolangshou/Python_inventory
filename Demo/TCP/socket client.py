import socket, struct, subprocess


tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect(("127.0.0.1", 5551))

while 1:
    cmd = input("input shell cmd").strip()
    if not cmd:
        continue
    tcp.send(bytes(cmd, encoding="utf-8"))
    header = tcp.recv(4) ##表示要接受多少数据的字节流.
    total_count = struct.unpack('i', header)[0]
    recv_count = 0
    result = b''
    while recv_count < total_count:
        t = tcp.recv(1024)
        recv_count += len(t)
        result += t
    print("cmd result: %s" %result.decode(encoding="utf-8"))

