# -*- coding: utf-8 -*-
# @Time    : 2021/10/8 14:28
# @Author  : Lindand
# @File    : CountNumber.py
# @Description :统计字符串个数
# python 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

s = input("请输入字符串：")
alphaNum = 0
spaceNum = 0
numbers = 0
otherNum = 0
for str in s:
    if str.isalpha():
        alphaNum += 1
    elif str.isnumeric():
        numbers += 1
    elif str.isspace():
        spaceNum += 1
    else:
        otherNum += 1
print("字母char=%d" % alphaNum)
print("空格space=%d" % spaceNum)
print("数字digit=%d" % numbers)
print("其他others=%d" % otherNum)
