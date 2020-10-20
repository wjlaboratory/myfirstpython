# os file and path的操作
import os

currentpath = r"D:\record\python\39-函数的返回值及其函数调用.wmv"
filename = os.path.split(currentpath) # 拆分文件路径与文件名
extendname = os.path.splitext(currentpath) # 拆分文件名与文件扩展名
print(filename)
print("the path of current file is {}".format(filename[0])) # 文件路径
print("the name of current file is {}".format(filename[1])) # 文件名称
print(extendname)
print("the source name of current file is {}".format(extendname[0])) # 文件名称
print("the extend name of current file is {}".format(extendname[1])) # 文件扩展名
print('the size of \"{}\" is {}'.format(currentpath, os.path.getsize(currentpath)))
print(os.getcwd())
print(os.path.join(os.getcwd(), 'file', 'a', 'www.abc')) # 构成新的文件路径名称
print(os.path.isabs(currentpath))  # 是否是绝对路径
print(os.path.isfile(currentpath))  # 是否是文件
print(os.path.isdir(currentpath))  # 是否是目录
print(os.listdir(os.getcwd()))  # 列出当前目录下的所有文件与文件夹
os.mkdir("aaa")  # 创建文件夹
if os.path.exists("aaa"):
    os.rmdir("aaa")  # 删除文件夹
    print("文件夹删除成功...")

if os.path.exists(currentpath):
    print("'{}' 已经存在...".format(currentpath))
else:
    print("'{}' 不存在...".format(currentpath))
# os.remove(文件名称) 删除指定文件
# os.chdir(文件夹)  切换当前目录

