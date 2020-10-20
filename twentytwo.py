# 　装饰器
# 1、首先是一个闭包
# 2、外层函数的形式参数是函数的应用
# 3、带参数的装饰器
def outer(x):
    def decorate(func):
        a = 100
        print("正在装饰...")

        def wrapper(*args, **kwargs):
            nonlocal a
            # a += 1
            print("x=%s" % x)
            print("正在运行装饰器...")
            func(args[0])
            print("装饰器运行结束...")

        print("结束装饰...")
        return wrapper

    return decorate


# @decorate　# 单层装饰器
@outer(10)  # 带参数的装饰器
def login(a):
    print("{}用户登录函数...".format(a))


name = "王江"
login(name)
