# -*- coding: utf-8 -*-
# @Time    : 2021/10/4 8:44
# @Author  : Lindand
# @File    : FooFun.py
# @Description :

# import time
#
#
# def time_fun(func):
#     def wrapped_func(a, b):
#         print("时间：" + str(time.ctime()))
#         print(a, b)
#         return func(a, b)
#
#     return wrapped_func
#
#
# @time_fun
# def foo(a, b):
#     print(a + b)
#
#
# foo(3, 5)


def timefun(func):
    def inner(a, b):
        ticks = time.time()
        print("函数调用时间：", ticks)
        return func(a, b)

    return inner


import time


@timefun
def foo(a, b):
    print(a+b)
    return a + b


foo(1, 2)
