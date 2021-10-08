# -*- coding: utf-8 -*-
# @Time    : 2021/10/4 11:27
# @Author  : Lindand
# @File    : FunChinaEnglish.py
# @Description :
'''有下面两个函数，分别是中国人、美国人自我介绍。
 def chinese(): print("我来自中国。")
 def american(): print("I am from America.")
请利用装饰器，在这两个函数执行的时候，分别根据其国籍，来说出一段打招呼的话，如“你好!”“hello.”。
'''

def say_hello(country):
    def wrapper(func):
        def deco(*args, **kwargs):
            if country == "china":

                print("你好!")
            elif country == "america":

                print('hello!')
            else:
                return
            # 真正执行函数的地方
            func(*args, **kwargs)

        return deco

    return wrapper


@say_hello("china")
def chinese():
    print("我来自中国。")


@say_hello("america")
def american():
    print("I am from America.")


chinese()
print("——————————————————————————")
american()
