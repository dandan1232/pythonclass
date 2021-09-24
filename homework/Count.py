# -*- coding: utf-8 -*-
# @Time    : 2021/9/24 14:56
# @Author  : Lindand
# @File    : Count.py
# @Description :

count = 10


def test():
    count = 100
    print("函数内使用全局变量count:", count)


def test2():
    global count
    print("函数内使用全局变量count:", count)


if __name__ == '__main__':
    test()
    print("函数外使用全局变量count：", count)
    test2()
    print("函数外使用全局变量conut：",count)
