# 单例模式
# 类属性、对象属性
class Singleton:
    # 私有化
    aaa = 100
    __bbb = 200
    __instance = None
    # 重写__new__

    def __new__(cls):
        print("new")
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def get_bbb(self):
        return self.__bbb

    def set_bbb(self, b):
        self.__bbb = b

    @classmethod
    def get_class_bbb(cls):
        return cls.__bbb

s1 = Singleton()
print(s1)
s2 = Singleton()
print(s2)
print(Singleton.__dict__)
print(s1.__dict__)
s1.aaa += 1
# Singleton.aaa += 2
print(id(Singleton.aaa))
print(id(s1.aaa))
print(s2.aaa)
print(s1.__dict__)
s1.set_bbb(1000)
print(s1.__dict__)
print("Singleton bbb:" + str(Singleton.get_class_bbb()))
print("s1 bbb:" + str(s1.get_bbb()))

