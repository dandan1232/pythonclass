# -*- coding: utf-8 -*-
# @Time    : 2021/10/15 14:08
# @Author  : Lindand
# @File    : PolymCatDogFrog.py
# @Description :
# 请按照以下要求设计类（10分钟）
# 1)定义Animal类，在该类中声明talk方法；
# 2)定义Cat类，在该类中声明talk方法，用于打印“Meow!”的信息；
# 3)定义Dog类，在该类中声明talk方法，用于打印“Woof! Woof!”的信息；
# 4)定义animal_talk函数，入参为animal对象，调用对象的talk方法；
# 5)分别定义Cat、Dog的对象 c、d
# 6)将对象c、d分别作为animal_talk函数的入参，观察执行结果
# 7)定义frog类，在该类中声明talk方法，用于打印“Croak ! Croak!”的信息;
# 8)定义frog的对象f，作为animal_talk函数的入参，观察执行结果


class Animal(object):
    def talk(self):
        print("说话")

class Cat(Animal):
    def talk(self):
        print("Meow!")

class Dog(Animal):
    def talk(self):
        print("Woof!Woof!")

def animal_talk(animal):
    animal.talk()
animal=Animal()
c = Cat()
d = Dog()
# 调用了Animal下的animal_talk方法，将c传给animal_talk
# 又调用了Dog下的talk（），相当于c.talk（）
animal_talk(animal)
animal_talk(c)
animal_talk(d)
class frog(Animal):
    def talk(self):
        print("Croak! Croak!")
f = frog()
animal_talk(f)
