import threading

# 创建同步锁对象
threadLock = threading.Lock()
threads = []


class TestThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)  # 不要忘记调用父类的构造函数
        self._name = name

    def print_thread(self):
        sname = self._name
        print('线程名字是：', sname)

    def run(self):
        # 获取同步锁
        threadLock.acquire()
        sname = self._name
        print('线程名字是：', sname)

        # 释放同步锁
        threadLock.release()


# 创建线程
thread1 = TestThread('thread1')
thread2 = TestThread('thread2')

# 加入到线程列表
threads.append(thread1)
threads.append(thread2)

# 开始执行
thread1.start()
thread2.start()

# thread1.join()


