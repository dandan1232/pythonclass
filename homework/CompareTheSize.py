# -*- coding: utf-8 -*-
# @Time    : 2021/9/6 19:58
# @Author  : Lindand
# @File    : CompareTheSize.py
# @Description : 要求如下： 1) 接收用户输入的两个数字； 2) 比较它们的大小

# 设置输入的第一个数,使用float存取第一个数
a = float(input("请输入第一个数字："))
# 设置输入的第二个数，使用float存取第二个数
b = float(input("请输入第二个数字："))
# 进行判断，如果两数相同
if (a == b):
    print("相比较，两个数相同")


# 如果a比b大，输出a
elif (a > b):
    print("相比较，第一个参数比较大，为" + str(a))
# 如果b比a大，输出b
else:
    print("相比较，第二个参数比较大，为" + str(b))
