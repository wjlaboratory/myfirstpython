# 列表推导式
'''
list1 = [1,2,3,4]
result = [x+1 for x in list1 ]
print(result)
result = [x+1 for x in list1 if x%2 == 0 ]
print(result)
result = [x+1 if x%2 == 0 else x for x in list1 ]
print(result)
# 想得到多重嵌套中的数是2的倍数的平方组成的list
example2 = [[1,2,3],[4,5,6],[7,8,9],[10]]
example3 = [j**2 for i in example2 for j in i if j%2 == 0]
print(example3)
print([x*y for x in range(1,5) if x > 2 for y in range(1,4) if y < 3])
d_list = [(x, y) for x in range(5) for y in range(4)]
print(d_list)
'''
# 列表生成器

g = (x * 3 for x in range(10))  # g是一个列表生成器
print(g.__next__())  # 0
print(g.__next__())  # 3
print(g.__next__())  # 6
print(g.__next__())  # 9
# next() builtins内置系统函数
print(next(g))  # 12
print(next(g))  # 15
print(next(g))  # 18
print(next(g))  # 21
print(next(g))  # 24
print(next(g))  # 27


# print(next(g)) # 抛出StopIteration异常

def fib(leng):
    a, b = 0, 1
    n = 0
    while n < leng:
        yield b  # 返回b 并暂停
        a, b = b, a + b
        n += 1
    return 0


h = fib(8)

list1 = []
'''
print(next(h))
print(next(h))
print(next(h))

h.send(表达式)用来向生成器传递参数，但第一次只能传递None值
h.__nexe__()用来产生下一个值
'''
list1.append(next(h))
list1.append(next(h))
list1.append(next(h))
list1.append(next(h))
list1.append(next(h))
list1.append(next(h))
print(list1)
