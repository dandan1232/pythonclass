# -*- coding: utf-8 -*-
# @Time    : 2021/10/15 15:08
# @Author  : Lindand
# @File    : LambStatic.py
# @Description :
'''
1、定义一个“三角形”类，通过传入三条边长来构造三角形，并提供计算周长的方法。
2、在创建三角形对象前需检查传入的三条边长是否能构造出三角形对象
提示：可以先写一个静态方法来验证三条边长是否可以构成三角形
3、如果能够构造出三角形对象，则计算该三角形的周长。'''


class Triangle(object):
    def __init__(self, a, b, c, ):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c


a = float(input("请输入三角形第一条边:"))
b = float(input("请输入三角形第二条边:"))
c = float(input("请输入三角形第三条边:"))

if Triangle.is_valid(a, b, c):
    t = Triangle(a, b, c)
    print("可以构成三角形")
    print("周长为：%.1f" % t.perimeter())
else:
    print("无法构成三角形")
