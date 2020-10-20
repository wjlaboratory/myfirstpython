# 排列于组合

import itertools

# 排列
for val in itertools.permutations("abcd"):
    print(val)

print("===================================")

# 组合
for val in itertools.combinations("abcd", 2):
    print(val)

print("===================================")

# 笛卡尔集
for val in itertools.product("abcd", "1234"):
    print(val)

