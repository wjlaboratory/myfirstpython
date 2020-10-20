# 类的继承及其多继承
# 广度优先搜索
# super().__init__(name, age, gender)使得所有的父类的初始化方法只执行一次

class A(object):
    def __init__(self):
        print("A __init__")

    #   def say(self):
    #        print("say something...")   # 被下面的同名函数覆盖

    def say(self, a):
        print("say a " + a)


class B(A):
    def __init__(self, name):
        print("B __init__" + name)
        super(B, self).__init__()

class C(A):
    def __init__(self, name):
        print("C __init__" + name)
        super(C, self).__init__()


class D(A):
    def __init__(self, name):
        print("D __init__" + name)
        super(D, self).__init__()


class E(C, B):
    def __init__(self):
        print("E __init__")
        super(E, self).__init__()


class F(C):
    def __init__(self, name):
        print("F __init__")
        super(F, self).__init__(name)


class G(D, B):
    def __init__(self):
        print("G __init__")
        super(G, self).__init__()


if __name__ == '__main__':
    # print(F.__mro__)
    f = F('zhangsan')
    print("-------")
    # d = D()
    # print("-------")
    # g = G()
    # print("-------")
    a = A()
    a.say("me")


class GrandFather():
    money = 10000000


class Father(GrandFather):
    money = 1000
    face = "帅气的一张脸"


class Me(Father):
    pass


# 实例化
myself = Me()
print(myself.money)
print(myself.face)
