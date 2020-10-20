# 线程
# 线程可以共享全局变量
# 耗时(I/O密集型(爬虫))操作使用多线程
# 计算密集型操作使用多进程
# 死锁

import threading

money = 0
lock = threading.Lock()
list1 = [0]*10

# 自定义线程


class MyThread(threading.Thread):
    def run(self):
        global money
        for i in range(1000000):  # 当运算量达到一定值时，系统会自动释放GIL锁
            lock.acquire()  # 获取锁，否则，阻塞
            money += 1
            lock.release()  # 释放锁


def func1():
    global money
    for i in range(1000000):  # 当运算量达到一定值时，系统会自动释放GIL锁
        lock.acquire(timeout=5)  # 获取锁，否则，阻塞
        money += 1
        lock.release()  # 释放锁




def func2():
    global money
    for i in range(1000000):  # 当运算量达到一定值时，系统会自动释放GIL锁
        lock.acquire(timeout=5)  # 获取锁，否则，阻塞
        money += 1
        lock.release()  # 释放锁


if __name__ == "__main__":
    th1 = threading.Thread(target=func1, name='th1')
    th2 = threading.Thread(target=func2, name='th2')
    th3 = MyThread()

    th1.start()
    th2.start()
    th3.start()

    th1.join()
    th2.join()
    th3.join()

    print("money=", money)
    print(list1)