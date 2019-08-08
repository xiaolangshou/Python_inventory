import socketserver, socket
from socketserver import BaseRequestHandler
import time, subprocess, sys, getpass, os

class MyHandler(BaseRequestHandler):
    user = getpass.getuser()
    hostname = socket.gethostname().split('.')[0]
    shell_env = os.getcwd()
    abspath = shell_env.split('/')[-1]
    shell_name = "[{user}@{hostname} {abspath}]#".format(user=user, hostname=hostname, abspath=abspath)
    def handle(self):
        addr = self.request.getpeername()
        print('Get connection from', addr)
        self.request.sendall(bytes(self.shell_name, encoding="utf-8"))
        while 1:
            cmds = self.request.recv(1024).decode(encoding="utf-8").strip()
            if not cmds:
                self.request.sendall(bytes(self.shell_name, encoding="utf-8"))
            else:
                for cmd in cmds.split(';'):
                    if not cmd:
                        continue

                    if cmd.lower() == "exit":
                        self.request.close()

                    if cmd.split()[0].lower() == "cd":
                        self.shell_env = cmd.split()[1].lower()
                        self.abspath = self.shell_env.split('/')[-1]
                        self.shell_name = "[{user}@{hostname} {abspath}]#".format(user=self.user, hostname=self.hostname,
                                                                             abspath=self.abspath)
                    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=self.shell_env)
                    while p.poll() is None:
                        line = p.stdout.readline()
                        sys.stdout.write(line.decode(encoding="utf-8"))
                        self.request.sendall(line)
                    if p.returncode == 0:
                        self.request.sendall(p.stdout.read() + bytes("\n" + self.shell_name, encoding="utf-8"))
                    else:
                        self.request.sendall(p.stderr.read() + bytes("\n" + self.shell_name, encoding="utf-8"))

if __name__ == '__main__':
    host = "127.0.0.1"
    port = 5552
    server = socketserver.ThreadingTCPServer((host, port), MyHandler)
    server.serve_forever()