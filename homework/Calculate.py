# -*- coding: utf-8 -*-
# @Time    : 2021/9/18 8:36
# @Author  : Lindand
# @File    : Calculate.py
# @Description :计算两个数的和差积

num1 = float(input("输入num1:"))
num2 = float(input("输入num2:"))
calculate = input("输入计算符号为（+，-，*，/）：")
if (calculate == "+"):
    print("计算两者的和为：%.1f" % (num1 + num2))
elif (calculate == "-"):
    print("计算两者的差为：%.1f" % (num1 - num2))
elif (calculate == "*"):
    print("计算两者的积为：%.1f" % (num1 * num2))
elif (calculate == "/"):
    if (num2 != 0):
        print("计算两者的积为：%.1f" % (num1 / num2))
    else:
        print("当前算式不成立！")
