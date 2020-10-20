# 模块的引入　　import 模块　或　from 模块　import 变量名[函数名][类名]［*］
# 使用前者导入模块中的标识符前，必须带上模块名(模块名.标识符)；而后者则可以省略模块名
# 在模块中，可以使用__all__系统列表变量来限定星号（*）能导入的标识符。__all__ = [number, caculator]
# 在模块中定义的执行语句，在模块被导入加载时，将被自动执行，除非使用__name__==“__main__”进行了限定
# Python有很多模块，而这些模块是可以独立运行的！这点不像C++和C的头文件。
# import的时候是要执行所导入的模块的。
# __name__就是标识模块的名字的一个系统变量。这里分两种情况：假如当前模块是主模块（也就是调用其他模块的模块），
#       那么此模块名字就是"__main__"，通过if判断这样就可以执行“__mian__:”后面的主函数内容；假如此模块是被import的，
#       则此模块名字为文件名字（不加后面的.py），通过if判断这样就会跳过“__mian__:”后面的内容。


# 包的组成：__init__.py及其其它模块（*.py）
# 当导入包时，默认调用__init__.py文件，__init__.py文件的作用是：
# 1、本包中常用的类、变量与函数的定义放入__init__.py中
# 2、对于定义在__init__.py中的元素的访问，通过(包名.元素名称)的方式
# 3、使用from 包名 import * 导入包中所有模块时，定义在 __init__.py 中的系统列表变量 __all__ = []起作用

# 循环导入（1、避免；2、导入import放置在模块的中间或末尾）

# sys.path 返回导入包的默认搜索路径
import datetime
import random
import sys
import time
import hashlib

print(sys.path)
print(sys.version)
print(sys.argv)      # 运行程序时，传递给解释器的命令行参数
# print(time.time())   # 返回秒数
# time.sleep(3)
# print(time.time())   # 返回秒数

print(time.ctime(time.time()))   # 返回字符串格式
print(time.localtime(time.time()))   # 返回元组
print(time.mktime(time.localtime(time.time())))   # 元组转时间戳

print(time.strftime("%Y-%m-%d"))
print(time.strptime("2020/03/04","%Y/%m/%d"))
'''
datatime模块：
    time 时间
    date 日期
    datetime 日期时间
    timedelta 时间差
'''

print(datetime.date.today())

print(random.randrange(1,10))   # [1..10)
print(random.randint(1,10))   # [1..10]
list1 = ["张三", "里斯", "王五", "找刘", "狗狗"]
print(random.choice(list1))
random.shuffle(list1)    # 洗牌
print(list1)
print(chr(97)) # unicode码字符
print(ord('A')) # unicode码
print(ord("我")) # unicode码

# MD5加密是不可逆的，但base64加密是可逆的
md5 = hashlib.md5("共产党".encode("utf-8"))
print(md5.hexdigest())
sh1 = hashlib.sha1("共产党".encode("utf-8"))
print(sh1.hexdigest())
sh256 = hashlib.sha256("共产党".encode("utf-8"))
print(sh256.hexdigest())
