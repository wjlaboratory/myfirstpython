a = 10  # a1 当前模块全局变量
def outer():
    a = 9  # a2 当前outter作用域局部变量
    def inner():
        global a
        a = 8  # a3 既是全局变量a1，又是inner局部变量
        print(a)  # a3 8,在inner的局部作用域中找到了a3
    inner()  # inner()函数结束，a3作为全局变量被保留下来成为a1
    print(a)  # a2 9,在outer局部作用域中找到a2
outer()  # outer()函数结束，a2作为outer局部变量被释放
print(a)  # a1 8, 在当前模块全局作用域中找到了a1
