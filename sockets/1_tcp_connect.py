import socket
_host = "www.google.com"
_port = 80
# create socket object s
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to client
s.connect((_host,_port))
# send data
s.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
# receive data
resp = s.recv(1024)
print(resp)
