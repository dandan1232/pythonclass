# -*- coding: utf-8 -*-
# @Time    : 2021/9/27 10:27
# @Author  : Lindand
# @File    : RandomNum.py
# @Description :

import random

for i in range(10):
    print("第" + str(i+1) + "次")
    print("生成0~1的随机浮点数：", random.uniform(0, 1))
    print("生成1~100的随机浮点数：", random.uniform(1, 100))
    print("生成1~100的随机整数：", random.randint(1, 100))
    print("生成1~10的偶数：", random.randrange(0, 10, 2))
    print("------------------------------------------")
