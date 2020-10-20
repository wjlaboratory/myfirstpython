# 协程（微线程）在python中通过生成器来实现
# yield
# greenlet包
# gevent包 及其 猴子补丁

import time

from greenlet import greenlet


import gevent

from gevent import monkey

monkey.patch_all()      # 猴子补丁，替换time包中的sleep，使其自动具有yield的作用

# 生成器模式
def task0():  # 生成器0
    print("启动任务0...")
    while True:
        res = yield 4        #  其作用相当于return 4，res将永远为None
        print("res ", res)

def task1():  # 生成器1
    for i in range(3):
        print("A " + str(i))
        yield
        time.sleep(0.2)


def task2():  # 生成器2
    for i in range(3):
        print("B " + str(i))
        yield
        time.sleep(0.2)


# greenlet模式

def task3():
    for i in range(3):
        print("greenlet-A " + str(i))
        gb.switch()
        time.sleep(0.2)


def task4():
    for i in range(3):
        print("greenlet-B " + str(i))
        ga.switch()
        time.sleep(0.2)

# gevent模式


def a():
    for i in range(3):
        print("gevent-A " + str(i))
        time.sleep(0.2)


def b():
    for i in range(3):
        print("gevent-B " + str(i))
        time.sleep(0.2)


def c():
    for i in range(3):
        print("gevent-C " + str(i))
        time.sleep(0.2)

if __name__ == "__main__":

    # 生成器模式
    g0 = task0()
    print(next(g0))
    print("*" * 20)
    print(next(g0))
    print(next(g0))
    '''
    g1 = task1()
    g2 = task2()
    while True:
        try:
            next(g1)
            next(g2)
        except:
            break
    '''
    # greenlet模式
    '''
    ga = greenlet(task3)
    gb = greenlet(task4)

    ga.switch()
    # gb.switch()
    '''

    # gevent模式
    '''
    ga = gevent.spawn(a)
    gb = gevent.spawn(b)
    gc = gevent.spawn(c)

    ga.join()
    gb.join()
    gc.join()
    '''
