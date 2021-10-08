# -*- coding: utf-8 -*-
# @Time    : 2021/9/27 9:39
# @Author  : Lindand
# @File    : Lamb.py
# @Description :判断三边是否能够构成三角形

a = float(input("a:"))
b = float(input("b:"))
num1 = lambda a, b: (a ** 2) + (b ** 2)
print("两条边的平方和:" + str(num1(a, b)))

c = float(input("c:"))
if (a + b > c and a + c > b and b + c > a and abs(a - b) < c and abs(a - c) < b and abs(b - c) < a):
    num = [a, b, c]
    s = sorted(num, key=lambda x: x)
    n1 = s[0]
    n2 = s[1]
    sum = lambda n1, n2: (n1 ** 2) + (n2 ** 2)
    print("两条短边平方为：" + str(sum(n1, n2)))
    if sum(n1, n2) == s[2] ** 2:
        print("为直角三角形")
    else:
        print("不是直角三角形")
else:
    print("不能组成三角形")
