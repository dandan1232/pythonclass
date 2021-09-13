# -*- coding: utf-8 -*-
# @Time    : 2021/9/13 9:39
# @Author  : Lindand
# @File    : ExtractDomain.py
# @Description :

str = "http://www.niit.edu.cn?userName=admin&pwd=123456"
print("域名：" + str[7:22])
print("用户名：" + str[32:37])
str1 = str.replace("admin", "*****")
str2 = str1.replace("123456", "******")
print(str2)
