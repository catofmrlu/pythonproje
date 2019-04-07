import socket
import clientTest

try:
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.bind(host, port)

    s.listen(5)

    while True:
        c = clientTest
        c.addr = s.accept()
        print('连接地址：', c.addr)
        c.send('欢迎访问！')
        c.close()
except:
    print('有异常出现！')

