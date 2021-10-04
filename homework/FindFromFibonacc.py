# -*- coding: utf-8 -*-
# @Time    : 2021/10/4 11:01
# @Author  : Lindand
# @File    : FindFromFibonacc.py
# @Description :

fibon = [0, 1]
string = input("请输入一个大于1的整数：")
number = int(string)
while 1:
    if fibon[-1] <= number:
        fibon.append(fibon[-2] + fibon[-1])
    else:
        print("斐波那契数列中比输入数据大的最小的数是：")
        print(fibon[-1])
        break
