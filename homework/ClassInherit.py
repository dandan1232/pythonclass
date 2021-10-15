# -*- coding: utf-8 -*-
# @Time    : 2021/10/11 20:18
# @Author  : Lindand
# @File    : ClassInherit.py
# @Description :
'''
1、定义Bird类，在该类中声明fly方法，用于打印“鸟儿飞翔”的信息；
2、定义Fish类，在该类中声明swim方法，用于打印“鱼儿游泳”的信息；
3、定义Volador类继承自Bird和Fish类，在Volador类中没有任何属性和方法；
4、创建一个Volador类的对象，依次调用fly和swim方法。
5、在Bird和Fish类中增加breathe方法，分别用于打印“鸟儿呼吸”和“鱼儿呼吸”的信息；
6、让刚刚创建的对象，调用breathe方法。
'''
class Bird(object):

    def fly(self):
        print("鸟儿飞翔")

    def Breath(self):
        print("鸟儿呼吸")


class Fish(object):
    def swim(self):
        print("鱼儿游泳")

    def Breath(self):
        print("鱼儿呼吸")


class Volador(Bird, Fish):
    pass

# 创建Volador对象
volador = Volador()
# 调用fly方法
volador.fly()
# 调用swim方法
volador.swim()
# 刚刚创建的对象，调用Breathe方法。
volador.Breath()
#调用 Fish 类中的 Breathe 方法
Fish.Breath(volador)
#调用 Bird 类中的 Breathe 方法
Bird.Breath(volador)
