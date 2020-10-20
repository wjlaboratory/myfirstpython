# 多进程

# linux系统中，通过fork函数为当前进程创建子进程 通过os模块导入；
# windows系统中，引入multiprocessing模块，　通过Process类创建子进程
# run()只是执行，但没有启动进程
# start()启动进程并执行
# terminate：终止进程的执行
# 对于全局变量 m 而言，每个子进程均会创建一个拷贝，对其进行的任何修改，不会影响到主进程中的全局变量
# 自定义进程
# 进程池

import os
from multiprocessing import Process, Pool
from random import random

from time import sleep, time

m = 0  # 不可变类型
list1 = []  # 可变类型


def task1(sec, name):
    global m
    while True:
        sleep(sec)
        m += 1
        list1.append(str(m) + "task1")
        print("task1...", os.getpid(), os.getppid(), name, "m=", m, list1)
        if m >= 10:
            break


def task2(sec, name):
    global m
    while True:
        sleep(sec)
        m += 1
        list1.append(str(m) + "task1")
        print("task2...", os.getpid(), os.getppid(), name, "m=", m, list1)
        if m >= 10:
            break


# 自定义进程

class MyProcess(Process):

    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    # 重写run方法
    def run(self):
        print("I'm ", self.name)

if __name__ == "__main__":
    # 创建两个子进程p1, p2
    p1 = Process(target=task1, name="任务1", args=(1, 'aa'))
    p1.start()
    p2 = Process(target=task2, name="任务2", args=(1, 'bb'))
    p2.start()
    print(p1.name)
    print(p2.name)
    while True:
        sleep(1)
        m += 1
        if m>10:
            break;
    print("m=", m)
    # 自定义进程
    p = MyProcess("wangjiang")
    p.start()
