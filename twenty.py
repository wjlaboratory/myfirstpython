#inner是一个闭包
def out():
    counter = 0
    def inner():
        nonlocal counter
        counter += 1
        print("这是你的第{}次访问".format(counter))
    return inner


x = out()
x()
x()
x()

