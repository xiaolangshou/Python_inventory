import socket, subprocess, struct

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind(("127.0.0.1", 5555))
tcp.listen()

while 1:
    cli, addr = tcp.accept()
    print(cli, addr)
    while 1:
        cmd = cli.recv(1024)
        print("server already receive cmd : %s" %cmd)
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout = p.stdout.read()
        stderr = p.stderr.read()
        header = struct.pack('i', len(stdout) + len(stderr))  ##4字节
        cli.send(header)
        cli.send(stdout)
        cli.send(stderr)
