# 生产者与消费者
# python的queue模块提供了同步的线程安全的队列类，Queue、LifoQueue与PriorityQueue。它们均提供了锁源语

import queue
import random
import threading
import time


def produce(q):
    i = 0
    while i<10:
        num = random.randint(1, 100)
        q.put("生产者生产数据：%d" % num)
        print("生产者生产数据：%d" % num)
        time.sleep(1)
        i += 1
    q.put(None)
    q.task_done()


def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print("消费者消费数据：%s" % item)
        time.sleep(4)
    q.task_done()


if __name__=='__main__':
    q = queue.Queue(10)
    th1 = threading.Thread(target=produce, args=(q, ))
    th2 = threading.Thread(target=consumer, args=(q, ))

    th1.start()
    th2.start()

    th1.join()
    th2.join()


