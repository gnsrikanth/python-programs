import socket
import threading
bind_ip = "0.0.0.0"
bind_port = 80
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((bind_ip,bind_port))
s.listen(10)

data = "Hello"
def srv(sock):
  req = sock.recv(1024)
  print(req)
  sock.send(data)
  sock.close()

while True:
  client,addr = s.accept()
  client_handler = threading.Thread(target=srv,args=(s,))
  client_handler.start()
