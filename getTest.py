import urllib.request
import time
import threading

def getBlong1():
    i = 1
    while i <= 10000:
        time.sleep(3)
        urllib.request.urlopen('https://blog.csdn.net/lxxlxx888/article/details/85332919')
        urllib.request.urlopen('https://blog.csdn.net/lxxlxx888/article/details/71242825')
        urllib.request.urlopen('https://blog.csdn.net/lxxlxx888/article/details/58333838')
        urllib.request.urlopen('https://blog.csdn.net/lxxlxx888/article/details/53969276')
        print('线程1访问第%d次\n'%i)
        i =i + 1


def getBlong2():
    i = 1
    while i <= 10000:
        time.sleep(5)
        urllib.request.urlopen('https://blog.csdn.net/lxxlxx888/article/details/89791746')
        urllib.request.urlopen('https://blog.csdn.net/lxxlxx888/article/details/90168858')
        urllib.request.urlopen('https://blog.csdn.net/lxxlxx888/article/details/75040974')
        urllib.request.urlopen('https://blog.csdn.net/lxxlxx888/article/details/55520778')
        urllib.request.urlopen('https://blog.csdn.net/lxxlxx888/article/details/54095483')
        urllib.request.urlopen('https://blog.csdn.net/lxxlxx888/article/details/53767988')
        print('线程2访问第%d次\n'%i)
        i =i + 1


t1 = threading.Thread(target = getBlong1)
t1.start()

t2 = threading.Thread(target = getBlong2)
t2.start()

