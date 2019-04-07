import socket

s = socket.socket
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口号

s.connect(host, port)
print(s.recv(1024))
s.close()