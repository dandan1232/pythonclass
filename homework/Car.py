# -*- coding: utf-8 -*-
# @Time    : 2021/10/8 15:05
# @Author  : Lindand
# @File    : Car.py
# @Description :
'''
请按照以下要求设计一个Car类：
1)Car类中声明两个属性price和speed，分别表示汽车的价格和最高时速；
2)Car类中声明一个方法run，表示汽车行驶的行为，在方法中要求访问speed和price。
3)创建一个Car类对象，调用run方法输出。
'''


class Car:
    def __init__(self, price, speed):
        self.price = price
        self.speed = speed

    def run(self):
        print("汽车行驶")
        print(self.speed)
        print(self.price)


c = Car(5000, 120)
c.run()
