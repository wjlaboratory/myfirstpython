# 匿名函数
from functools import reduce

x = lambda a, b: a + b
y = lambda x, y: x * y

print(x(1, 2))
print(y(2, 2))

list1 = [1, 2, 3, 5, 6]
print("the amx of list1 is %s" % max(list1))

list2 = [{"a": 10, "b": 20}, {"a": 100, "b": 101}, {"a": 1000, "b": 1001}]
print("the amx of list2 is %s" % max(list2, key=lambda x1: x1["a"]))

print(list(map(lambda l: l + 2, list1)))
print(list(map(lambda l: l if l % 2 == 0 else l + 2, list1)))

for index, i in enumerate(list1):
    print(list1[index], end=" ")

print()

tuple1 = (1, 2, 3)
print(reduce(lambda m, n: m + n, tuple1))

tuple2 = (1, )
print(reduce(lambda m, n: m + n, tuple2, 10))

tuple1 = (1, 2, 3)
print(list(filter(lambda m: m > 1, tuple1)))

ll = [4,100,2,3,1]
print(sorted(ll))
print(ll)