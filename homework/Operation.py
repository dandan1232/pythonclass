# -*- coding: utf-8 -*-
# @Time    : 2021/9/24 14:55
# @Author  : Lindand
# @File    : Operation.py
# @Description :
'''定义一个用于计算的函数，请按照以下要求完成。
# 1)函数有3个参数，operation默认值为“+”，只能接收“-”、“*”和“/”符号；num1和num2分别用于接收整数。
# 2)使用if-elif语句判断，如果为“+”，返回num1和num2的和；如果为“-”，返回num1和num2的差，以此类推。
# 3)注意，处理num2不为0的情况。
'''


def cal(num1, num2, operation='+'):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return '除数不能为0'
        else:
            return num1 / num2
    else:
        return '该函数不能为此数'

num1 = int(input("请输入第一个整数："))
num2 = int(input("请输入第二份整数："))
print('num1+num2=', cal(num1, num2))
print('num1-num2=', cal(num1, num2, '-'))
print('num1*num2=', cal(num1, num2, '*'))
print('num1/num2=', cal(num1, num2, '/'))
