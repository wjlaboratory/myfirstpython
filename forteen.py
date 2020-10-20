a = 10  # a1 当前模块全局变量
def outer():
    a = 9 # a2 outer局部变量
    def inner():
        nonlocal a  #声明此变量与外层同名变量为相同变量;
        #2、注意：如果在外层没有找到变量a, 则会继续在再外层寻找，直到全局作用域的下一层为止（看第3点）
        a = 8  # a3  既是inner局部变量，又是外层outer局部变量
        print(a)  # a3 8，在inner的局部作用域中找到了a3
    inner()  # inner()函数结束，a3作为外层变量(outer局部变量)被保留成为a2
    print(a)  # a2 8,在outer局部作用域中找到a2（在inner中被改变）
outer()  # outer()函数结束，a2作为outer局部变量被释放
print(a)  # a1 10，在当前模块全局作用域中找到了a1
