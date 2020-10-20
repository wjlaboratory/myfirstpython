# 进程池
# multiprocessing 模块提供一个方法pool，初始化时可以指定一个最大进程数，当有新的请求被提交到pool时，
# 如果还没满，就创建一个新的进程来执行该请求，否则，该请求就会等待，直到池中有进程结束，才会创建新的进程

import os
import time
from multiprocessing.pool import Pool
from random import random


def task(task_name):
    print("开始我的新任务啦....", task_name, os.getpid())
    starttime = time.time()
    time.sleep(random() * 3)
    endtime = time.time()
    #print("我的任务--{}--完成啦...耗时{},进程{}".format(task_name, endtime-starttime, os.getpid()))
    return "我的任务--{}--完成啦...耗时{},进程{}".format(task_name, endtime - starttime, os.getpid())


def callback_func(n):
    print(n)


if __name__ == "__main__":
    # 进程池
    pool = Pool(5)
    tasks = ["听音乐", "吃饭", "打游戏", "看孩子", "做饭", "跑步", "学习", "打架", "听音乐", "吃饭", "打游戏", "看孩子",
             "做饭", "跑步", "学习", "打架"]
    for t in tasks:
        pool.apply_async(task, args=(t,), callback = callback_func)  # 异步方式，非阻塞
    pool.close()  # 进程池添加结束
    pool.join()  # 使主进程阻塞
