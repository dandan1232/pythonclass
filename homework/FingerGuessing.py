# -*- coding: utf-8 -*-
# @Time    : 2021/9/18 8:14
# @Author  : Lindand
# @File    : FingerGuessing.py
# @Description :和机器的石头剪刀布

import random
human = int(input("随机输入一个0-2的数:"))
machine = random.randint(0, 2)
if (human != 0 and human != 1 and human != 2):
    print("输入错误，请重新输入")
else:
    # print("用户出的是: " + str(human) + ",机器出的是: " + str(machine))
    print("用户出的是：%d,机器出的是：%s" % (human, machine))
if (human == 0):
    print("用户出的剪刀")
elif (human == 1):
    print("用户出的石头")
else:
    print("用户出的布")

if (machine == 0):
    print("机器出的剪刀")
elif (machine == 1):
    print("机器出的石头")
else:
    print("机器出的布")

if (human == 0 and machine == 2) or (human == 1 and machine == 0) or (human == 2 and machine == 1):
    print("你赢了!")
elif human == machine:
    print("平局")
else:
    print("你输了")
