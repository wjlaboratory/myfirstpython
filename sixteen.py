#注意：如果在外层没有找到变量a,则会继续在再外层寻找，直到全局作用域的下一层为止（看第3点）
a = 10  # a1 当前模块全局变量
def outer2():
    a = 9 # a2 outer2作用域局部变量
    b = 100
    print(a) # a2 9,还未被a3改变
    def outer1():
        print(a) # a2 9,在outer1中没找到局部变量a，则寻找外层(outer2)变量a2(还未被a3改变)
        def inner():
            nonlocal a
            a = 0  # a3 既是inner局部变量，又是再外层outer2作用域变量
            print(a)  # a3 0, 找到inner局部变量a3
        inner()  # inner()函数结束，a3作为外层变量(outer2局部变量)被保留成为a2
        print(a)  # a2 0,在outer1中没找到局部变量a，则寻找外层(outer2)变量a2(被a3改变)
    outer1()
    print(a) # a2 0, 在outer1中找到outer1局部变量a2(被a3改变)
outer2()
print(a)  # a1 10，在当前模块全局作用域中找到了a1
