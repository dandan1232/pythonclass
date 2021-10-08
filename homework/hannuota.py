# -*- coding: utf-8 -*-
# @Time    : 2021/10/8 13:53
# @Author  : Lindand
# @File    : hannuota.py
# @Description :

count = 0


def hanoi(number, A, B, C):
    count = 0
    if number == 1:
        print(A, "--->", C)
        count += 1
    else:
        count += hanoi(number - 1, A, C, B)
        hanoi(1, A, B, C)
        count += 1
        count += hanoi(number - 1, B, A, C)
    return count


def positive(number):
    if number <= 0:
        flag = 0
    else:
        flag = 1
    return flag


string = input('请输入汉诺塔的层数：')
number = int(string)
if positive(number):
    print("移动顺序为：")
    count = hanoi(number, 'A', 'B', 'C')
    print("移动次数为：%d" % count)
else:
    print("输入错误，程序结束！")
