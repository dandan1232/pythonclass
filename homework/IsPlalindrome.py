# -*- coding: utf-8 -*-
# @Time    : 2021/10/4 11:32
# @Author  : Lindand
# @File    : IsPlalindrome.py
# @Description : 判断是否为回文

def isPalindrome(s):
    if len(s) < 2:  # 如果字符串只有0个或1个字符，那么该字符串符合回文的定义
        return True
    if s[0] != s[-1]:  # 如果字符串不止一个字符，那么检查字串符的第一项和最后一项是否等同
        return False
    return isPalindrome(s[1:-1])  # 字串符的第一项和最后一项等同，所以去除字符串的第一项和最后一项，继续进行检查


str = input("请输入一个字符串： ")
if isPalindrome(str):
    print(str + "是一个回文字符串")
else:
    print(str + "不是一个回文字符串")
