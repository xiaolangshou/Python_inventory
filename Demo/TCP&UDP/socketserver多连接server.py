from socketserver import TCPServer, ForkingMixIn, StreamRequestHandler, ThreadingMixIn
import subprocess, struct
class Server(ThreadingMixIn, TCPServer):
#class Server(ForkingMixIn, TCPServer):
    pass

class MyHandler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print("Connect with ", addr)
        while 1:
            cmd = self.request.recv(1024).decode(encoding="utf-8")
            print("server already receive cmd : %s" % cmd)
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout = p.stdout.read()
            stderr = p.stderr.read()
            header = struct.pack('i', len(stdout) + len(stderr))  ##4字节
            self.wfile.write(header)
            self.wfile.write(stdout)
            self.wfile.write(stderr)

if __name__ == '__main__':
    server = Server(("127.0.0.1", 5551), MyHandler)
    server.serve_forever()



