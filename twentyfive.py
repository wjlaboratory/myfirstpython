# 异常处理
def func():
    try:
        a = int(input("请输入第一个操作数:"))
        b = int(input("请输入第二个操作数:"))
        oper = input("请输入操作符(+ - * /):")
        if oper == '+':
            print("%s + %s = %s" % (a, b, a + b))
        elif oper == '-':
            print("%s - %s = %s" % (a, b, a - b))
        elif oper == '*':
            print("%s * %s = %s" % (a, b, a * b))
        elif oper == '/':
            print("%s / %s = %s" % (a, b, a / b))
        else:
            print("操作符输入错误...")
        # return 1
        # list1 = []
        # list1.pop()
        # with open("xxx.xxx", "r") as stream:
        #    content = stream.read()
        #    print(content)
    except ZeroDivisionError:
        print("除数不能为零...")
    except ValueError:
        print("操作数必须是数字...")
    except Exception as err:
        print("Exception 异常", err)
    except:
        print("发生了未知的异常...")
    else:
        print("没有发生任何异常...")  # 没有发生任何异常时执行
    finally:
        print("操作完成...")  # 无论是否发生了异常，均会被执行
        # return 3


def register():
    username = input("请输入用户名：")
    if len(username) < 6:
        raise Exception("用户名长度不能小于6位...")
    return username


# func()

username = ""
try:
    username = register()
except Exception as err:
    print(err)
    print("注册失败...")
else:
    print("{} 成功注册...".format(username))
