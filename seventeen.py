#全局变量不是外层变量，不被nonlocal寻找
a = 10  # a1 当前模块全局变量
def outer():
    def inner():
        nonlocal a  # 在当前作用域外层即outer局部作用域中没找到outer局部变量a，outer外层为全局作用域，nonlocal不继续寻找，报错
        a = 8
        print(a)
    inner()
    print(a)
outer()
print(a)  # a1 10，在当前模块全局作用域中找到了a1
