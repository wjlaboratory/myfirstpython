# 闭包：
# 1、在一个外函数中定义了一个内函数
# 2、内函数里运用了外函数的临时变量
# 3、并且外函数的返回值是内函数的引用
def decorate():
    a = 100

    def wrapper():
        nonlocal a
        a += 1
        print("a=%s" % a)

    return wrapper


func = decorate()
func()
