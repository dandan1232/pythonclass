# -*- coding: utf-8 -*-
# @Time    : 2021/10/18 8:38
# @Author  : Lindand
# @File    : FunChinaEnglish2.py
# @Description :
'''有下面两个函数，分别是中国人、美国人自我介绍。
 def chinese():
    print("我来自中国。")
 def american():
    print("I am from America.")
请设计一个装饰器，在这两个函数执行的时候，分别根据其国籍，来说出一段打招呼的话，如“你好!”“hello.”。
'''


class Contry():
    def __init__(self, contry):
        self.contry = contry

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            if self.contry == "china":
                print("你好")
            elif self.contry == "america":
                print("hello.")
            else:
                return

            # 真正执行函数的地方
            func(*args, **kwargs)

        return wrapper()


@Contry("china")
def chinese():
    print("我来自中国。")


@Contry("america")
def american():
    print("I am from America.")


chinese
print("--------------")
american