# -*- coding: utf-8 -*-
# @Time    : 2021/9/10 13:54
# @Author  : Lindand
# @File    : printout.py
# @Description :
# 日常课堂作业

# name = "小明"
# age = 28
# weight = 61.5
# print("姓名为：%s,年龄为：%d,体重为：%.1f" % (name, age, weight))

# a = "abcdef"
# print(a[0:2])
# print(a[2:5])
# print(a[2:-1])
# print(a[3:])
# print(a[::2])
# print(a[::-2])


# print(a[0:3])
# print(a[3:5])
# print(a[1:-1])
# print(a[2:])
# print(a[::-2])

# b="南京工业职业技术大学欢迎您"
# print(b[0:2])
# print(b[2:])
# print(b[2:-1])
# print(b[::-3])

# string="Python is good"
# print(string[1:11])
# # print(string[20])
# print(string[3:-4])
# print(string[-10:-3])
# print(string.lower())
# print(string.replace("o","0"))
# print(string.startswith('python'))
# print(string.split())
# print(len(string))
# print(      string[30])
# print(string.replace(' ',''))
# print()

# string="000itcast and itheima000"
# # print(string.find('it'))
# # print(string.count('it'))
# # print(string.replace('000',' '))
# # print(string.upper())
# # print(string.strip())

# a = "itcast"
# print('heima' not in a)
# a += ' heima'
# print(a)
# print((a).title())
# print(a.split(' '))
#
# a = 'sandwiches'
# b = 'apples'
# c = 'sups'
# d = 'cookies'
# e = '4'
# f = "12"
# g = "8000"
# print('PICNIC ITEMS'.center(17, '-'))
# print(a.ljust(12, '·') + e.rjust(5))
# print(b.ljust(12, '·') + f.rjust(5))
# print(c.ljust(12, '·') + e.rjust(5))
# print(d.ljust(12, '·') + g.rjust(5))
#
# print('PICNIC ITEMS'.center(28, '-'))
# print(a.ljust(20, '·') + e.rjust(5))
# print(b.ljust(20, '·') + f.rjust(5))
# print(c.ljust(20, '·') + e.rjust(5))
# print(d.ljust(20, '·') + g.rjust(5))

# tlist = [5, 11, 98, 19, 71, 100]
# # print(tlist[0:2])
# print(tlist[2:5])
# print(tlist[2:-1])
# print(tlist[3:])
# print(tlist[::2])
# print(tlist[::-2])

# lst = [2, 5, 6, 7, 8, 9, 2, 9, 9]
# print(lst[2:4])
# print(lst[1:-3])
# print(lst[-5])
# print(lst[:-4])
# print(lst[-4:])

# lst = [1, 4, 5, [1, 3, 5, 6, [8, 9, 10, 12]]]
# print(len(lst))
# print(type(lst[1]))
# print(type(lst[3]))
# print(lst[3][4])
# print(lst[3][4][1])
# print(lst[3][4].append([5,6]))
#
# print(lst[-1][-1][-2])
# print(lst[-2])
# print(len(lst[-1]))
# print(len(lst[-1][-1]))
# print(lst[-1][1:3])
# print(lst[-1][-1][1:2])

# list = ['小明', '小红', '小兰', '小白']
# len = len(list)
# print("列表长度为：", len)
# i = 0
# print("while循环遍历：")
# while i < len:
#     print(list[i])
#     i += 1
# print("for循环遍历:")
# for name in list:
#     print(name)

'''按照以下要求完成程序：
1、定义一个空列表，往列表中添加5个任意整数；
2、在列表索引为1的位置，插入一个元素99；
3、找出下标为偶数的元素，并从列表中删除它们；
4、让列表由大到小排序，然后输出。
'''

# 法一
# list = []
# list.append(1)
# list.append(2)
# list.append(3)
# list.append(4)
# list.append(5)
# print("往列表中添加5个任意整数:" + str(list))
# list.insert(1, 99)
# print("在列表索引为1的位置，插入一个元素99:" + str(list))
# for i in range(len(list)):
#     if i % 2 == 0:
#         print("下标为" + str(i) + "的元素有：" + str(list[i]))
# del list[::2]
#
# print("删除下标为偶数的元素后为：" + str(list))
# list.sort(reverse=True)
# print("表由大到小排序:" + str(list))

# 法二
# list = []
# list.append(1)
# list.append(2)
# list.append(3)
# list.append(4)
# list.append(5)
# print("往列表中添加5个任意整数:" + str(list))
# list.insert(1, 99)
# print("在列表索引为1的位置，插入一个元素99:" + str(list))
# for i in range(len(list)):
#     if i % 2 == 0:
#         del list[0]
#     else:
#         list.append(list[0])
#         del list[0]
# print("删除下标为偶数的元素后为：" + str(list))
# list.sort(reverse=True)
# print("表由大到小排序:" + str(list))

# # 使用while循环遍历列表和元组
# a_tuple = ('fkit', 'crazyit', 'Charli')
# i = 0
# # 只有i小于len(a_list)，继续执行循环体
# while i < len(a_tuple):
#     print(a_tuple[i],end=" ")  # 根据i来访问元组的元素
#     i += 1

# # 元组
# tup = (1, 4, 5, (1, 3, 5, 6, (8, 9, 10, 12)))
# print(len(tup))
# print(type(tup[1]))
# print(type(tup[3]))
# print(tup[3][4])
# print(tup[3][4][1])
# # a = tup[3][4].append([5, 6])
# # print(a)
# print(tup[-1][-1][-2])
# print(tup[-2])
# print(len(tup[-1]))
# print(len(tup[-1][-1]))
# print(tup[-1][1:3])
# print(tup[-1][-1][1:2])
#
# def cal(num1, num2, operation='+'):
#     if operation == '+':
#         return num1 + num2
#     elif operation == '-':
#         return num1 - num2
#     elif operation == '*':
#         return num1 * num2
#     elif operation == '/':
#         if num2 == 0:
#             return '除数不能为0'
#         else:
#             return num1 / num2
#     else:
#         return '该函数不能为此数'
#
# num1 = int(input("请输入第一个整数："))
# num2 = int(input("请输入第二份整数："))
# print('num1+num2=', cal(num1, num2))
# print('num1-num2=', cal(num1, num2, '-'))
# print('num1*num2=', cal(num1, num2, '*'))
# print('num1/num2=', cal(num1, num2, '/'))

func = lambda x: x % 3
list_test = list(range(1, 101))
result = filter(func, list_test)
print(list(result))

list1 = list(map(lambda x, y: [x, y], [1, 2, 3], [2, 2, 3]))
print(list1)

from functools import reduce

func2 = lambda x, y: x * y
result = reduce(func2, [1, 2, 3, 4, 5])
print(result)
