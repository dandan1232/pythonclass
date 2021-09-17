# -*- coding: utf-8 -*-
# @Time    : 2021/9/13 13:53
# @Author  : Lindand
# @File    : Sort.py
# @Description :
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

# 法三
list = []
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
print("往列表中添加5个任意整数:" + str(list))
list.insert(1, 99)
print("在列表索引为1的位置，插入一个元素99:" + str(list))
for i in range(len(list) - 1, -1, -1):  # list是一个列表
    if i % 2 == 0:
        list.remove(list[i])
print("删除下标为偶数的元素后为：" + str(list))
list.sort(reverse=True)
print("表由大到小排序:" + str(list))
