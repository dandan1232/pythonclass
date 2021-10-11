# -*- coding: utf-8 -*-
# @Time    : 2021/10/11 9:15
# @Author  : Lindand
# @File    : Demo.py
# @Description :定义一个Demo类，声明一个data1属性赋值为100；
# 定义set方法，该方法接收一个num值，它会赋值给data2属性
# 重载__str__方法返回自定义的字符串，即打印data1和data2的值
# 创建一个Demo类实例demo，调用set方法给data2赋值为200
# 分别使用print（），str（），repr（）函数输出demo的信息。

class Demo:
    __data1 = 100

    def set(self, num):
        self.__data2 = num

    def __str__(self):
        return ("data1 =%d,data2=%d" % (self.__data1, self.__data2))

    def __repr__(self):
        return ("repr data1 =%d,data2=%d" % (self.__data1, self.__data2))


demo = Demo()
demo.set(200)
print(str(demo))
print(repr(demo))
