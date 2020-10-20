# 类与对象
# 实例属性、方法
# 类属性、方法 @classmethod修饰，传递类名cls
# 静态方法 @staticmethod修饰，不传递任何参数，但必须通过类名调用
# __init__魔术方法，系统内置方法
# _foo 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import
# __foo 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了
# __new__ 创建对象时调用，自定义__new__方法会覆盖系统提供的__new__方法，如果没有自定义__new__方法，
#    系统将自动提供一个__new__方法，以便供创建新对象时调用，__new__方法是类方法
# __inti__ 对象创建好之后，初始化对象时调用，__init__是实例方法
# __call__：把对象当函数调用时，该函数被调用
# __del__：当对象的应用计数为零时，由垃圾回收器自动被调用(sys.getreference(p))，覆盖默认的垃圾回收函数
# __str__：把对象名当字符串处理时被调用
# @property：装饰器，把私有属性公有化（下面例子中的私有属性__age，转换为公有属性age）


class Person:
    def __init__(self):
        self.name = "zhangsan"
        self.__age = 20  # 私有属性
        print("__init__ has been excuted...")

    def __new__(cls, *args, **kwargs):
        print("__new__ has been excuted...")
        # return object.__new__(cls)
        return super(Person, cls).__new__(cls)

    def __call__(self, *args, **kwargs):
        print('call...%s' % self.name)

    def __del__(self):
        print("对象已被删除...")

    def __str__(self):
        return "ttt"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0 and age < 100:
            self.__age = age
        else:
            print("年龄超出范围...")


"""
p1 = Person()
# p1()                      # 把对象当函数时该函数被调用
print("p1--原来年龄是%s" % p1.age)
p1.age = 40
print("p1--现在年龄是%s" % p1.age)
# p2 = p1
p2 = Person()
p2.age = 80
print("p2--现在年龄是%s" % p2.age)
print("p1--现在年龄是%s" % p1.age)
print("id(p1)=", id(p1))
print("id(p2)=", id(p2))
# p1.age = 80
# print("p2--现在年龄是%s" % p2.age)

"""
a=12345
b=12346
print("id(a)", id(a))
print("id(b)", id(b))
