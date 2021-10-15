# -*- coding: utf-8 -*-
# @Time    : 2021/10/15 15:35
# @Author  : Lindand
# @File    : LegNumAnimal.py
# @Description :
'''
1.定义Animal类，在该类中有一个带有参数的构造方法，用于给legNum属性赋值；
2.定义继承自Animal类的子类Bird类，重写父类的构造方法，在构造方法中添加plume属性，并赋值为“白色”；
3.创建Bird类的对象，输出“有一只白色的鸟儿在树上唱歌。”
'''
# 如果子类想要调用父类中被重写的方法，需要使用super方法访问父类中的成员。
# super() 函数用于调用下一个父类(超类)并返回该父类实例的方法。

# 定义父类Animal
class Animal(object):
    def __init__(self, legNum):
        # 腿的数量
        self.legnum = legNum


# 定义Bird类继承自Animal
class Bird(Animal):
    # 重写了父类的init方法
    def __init__(self, legnum):
        # 增加特有的属性
        self.plume = '白色'
        # 调用父类的init方法
        super().__init__(legnum)


bird = Bird(2)
print('有一只%s条腿%s的鸟儿在树上唱歌。' % (bird.legnum, bird.plume))
