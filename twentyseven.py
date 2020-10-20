# 可迭代、迭代器
# 生成器是可迭代的、元组、列表、集合、字典与字符串是可迭代的
# 迭代器：能出现在next中的产生下一个元素的就是迭代器，只能向后不能向前
# 生成器是迭代器，但元组、列表、集合、字典与字符串不是迭代器
# 通过iter内置函数，把可迭代的转化为迭代器
#  from collections import Iterable 已被废弃


from typing import Iterable

list1 = []
result = isinstance(list1, Iterable)
print(result)
g = (x for x in range(10))
list1.append(next(g))
list1.append(next(g))
list1.append(next(g))
list1.append(next(g))
list1.append(next(g))
print(list1)
print(isinstance(g, Iterable))
print(isinstance('123', Iterable))
list1 = iter(list1)  # 把list1转换为迭代器
print(next(list1), end=" ")
print(next(list1), end=" ")
print(next(list1), end=" ")
print(next(list1), end=" ")
