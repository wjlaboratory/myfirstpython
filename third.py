# -*- coding: UTF-8 -*-
def printme(str):
    "打印给定的字符串"
    print(str)
    return
def printinfo(name, age=35):
    "调用关键字参数时，与参数顺序无关, 参数可以带有默认值"
    print(name, age)
    return
def printvariable( arg1, *vartuple ):
   "打印任何传入的参数"
   print("输出: ")
   print(arg1)
   print("输出可变参数")
   for var in vartuple:
      print(var)
   return

sum = lambda arg1, arg2: arg1 + arg2

printme("这是我的第一个函数调用")
printme("这是我的第二个函数调用")
printinfo(age=18,name="王江")
printinfo(name="王江")
printvariable(10,20,30,40)
print("调用匿名函数", sum(10, 20))