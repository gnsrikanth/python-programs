import socket
_host = "8.8.8.8"
_port = 53
data = "DNS REQUEST"
# Socket object s 
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(data,(_host,_port))
res,addr = s.recvfrom(1024)
print(res)
