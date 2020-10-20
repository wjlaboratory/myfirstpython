# 正则表达式
import re

msg = ";ldfk;ald;fkdf2020-09-27dflk;d2021-03-05lkdfa"
url = "http://www.sxu.edu.cn:8080"
result = re.findall('[0-9]{4}-[0-9]{2}-[0-9]{2}', msg)
print(result)

result = re.findall('[a-z]+\\.[a-z]+\\.[a-z]+\\.[a-z]+', url)

print(result)

# 0-100的数
msg1 = '0123'
result = re.match(r"[0-9]?\d?$|100$", msg1)  # "|" 是或的关系
print(result)

# 邮箱匹配 163 126 qq...
msg2 = "456132@qq.com"
result = re.match(r"\w{1,20}@(163|126|qq)\.(com|cn)$", msg2)  # "|" 是或的关系
print(result)

# 分组()
phone = "010-12345678"
result = re.match("(\d{3}|\d{4})-(\d{8})", phone)
print(result.group(1))
print(result.group(2))

msg3 = "<html><h1>abc</h1></html>"

# 　使用分组编号\d
result = re.match(r"<([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>(.+)</\2></\1>$", msg3)
print(result.group(1))
print(result.group(2))
print(result.group(3))

# 　使用分组名称?P
result = re.match(r"<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>", msg3)
print(result.group(1))
print(result.group(2))
print(result.group(3))

# sub正则搜索，并替换
msg4 = "l;kfg10lkdfg100"
result = re.sub(r"\d+", "90", msg4)
print(result)


def fun(temp):
    num = int(temp.group())
    num1 = num + 1
    return str(num1)


result = re.sub(r"\d+", fun, msg4)
print(result)

# split 正则切割

result = re.split(r"[,:]", "java:99,split")
print(result[0])
print(result[1])
print(result[2])

# 贪婪匹配：总是尽可能匹配多的字符（*，+等）；非贪婪匹配：总是尽可能匹配少的字符
# 贪婪转非贪婪：在量词后加"?"字符；如下实例

result = re.match(r"abc\d+","abc123") #贪婪匹配，结果abc123
print(result)
result = re.match(r"abc\d+?","abc123") #非贪婪匹配，结果abc1
print(result)

