# -*- coding: utf-8 -*-
# @Time    : 2021/9/18 11:21
# @Author  : Lindand
# @File    : isPrimeNum.py
# @Description :判断是否为素数

from math import sqrt;

num = int(input("请输入一个整数: "))
result = int(sqrt(num))
is_sushu = True
if num > 1:
    for i in range(2, result + 1):
        if num % i == 0:
            is_sushu = False
            break
if is_sushu and num != 1:
    print("%d是素数" % num)
else:
    print("%d不是素数" % num)
