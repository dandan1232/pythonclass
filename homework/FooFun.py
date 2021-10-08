# -*- coding: utf-8 -*-
# @Time    : 2021/10/4 8:44
# @Author  : Lindand
# @File    : FooFun.py
# @Description :装饰器：
# 函数名称foo，调用时间Fri Oct  8 14:53:06 2021，参数的值xz
# python难不难啊我的小笨脑袋瓜学不会

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

#
# def timefun(func):
#     def inner(a, b):
#         ticks = time.time()
#         print("函数调用时间：", ticks)
#         return func(a, b)
#
#     return inner
#
#
# import time
#
#
# @timefun
# def foo(a, b):
#     print(a+b)
#     return a + b
#
#
# foo(1, 2)


import time


def timefun_arg(pre="ldd"):
    def timefun(func):
        def wrappedfunc():
            print("函数名称%s，调用时间%s，参数的值%s" % (func.__name__, time.ctime(), pre))

            return func()

        return wrappedfunc

    return timefun


@timefun_arg(pre="xz")
def foo():
    print("python难不难啊我的小笨脑袋瓜学不会")


foo()

