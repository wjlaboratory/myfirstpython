# 进程间通讯
# put(self, obj, block=True, timeout=None)函数：如果队列有空位，则在队尾添加新元素，否则，进程在timeout内处于阻塞状态
# get(self, block=True, timeout=None)函数：如果队列不空，则在队头获取新元素，否则，进程在timeout内处于阻塞状态

from multiprocessing import Queue, Process

from time import sleep


def download1(qq):
    list1 = ["gril.jpg", "boy.jpg", "man.jpg"]
    for l in list1:
        print("正在下载{}...".format(l))
        sleep(1)
        qq.put(l)


def save1(qq):
    while True:
        try:
            file = qq.get(timeout = 3)
            print("保存{}成功...".format(file))
        except:
            break


if __name__ == "__main__":
    q = Queue(5)
    q.put('A')
    q.put('B')
    q.put('C')
    q.put('D')
    q.put('E')
    print(q.qsize())
    if not q.full():
        q.put('F', timeout = 1)  # 如果在一秒钟之内操作不成功，则抛出异常
    else:
        print("队列已满...")

    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    if not q.empty():
        q.get(timeout = 1)  # 如果队列已空，当前进程阻塞一秒，之后则抛出异常
    else:
        print("队列已空...")

    p1 = Process(target=download1, args=(q,))
    p2 = Process(target=save1, args=(q,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
