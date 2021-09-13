# -*- coding: utf-8 -*-
# @Time    : 2021/9/13 9:39
# @Author  : Lindand
# @File    : ConstituteName.py
# @Description :

data = input("请输入一个日期，格式为:年/月/日:")
name = "林丹丹"
print(name)
student_id = 1902343231
print(student_id)
data1 = data.replace("/", "年", 1)
data2 = data1.replace("/", "月", 1)
data2 += "日"
a = "我叫%s，我的学号是%d，今天是%s" % (name, student_id,data2) + "，我在学习有趣又有用的python程序设计"
print(str(a))
