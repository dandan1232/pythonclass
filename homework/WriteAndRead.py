# -*- coding: utf-8 -*-
# @Time    : 2021/10/18 10:28
# @Author  : Lindand
# @File    : WriteAndRead.py
# @Description :
import os

# 1.读文件

f = open('D:\\Study\\data.txt', 'r+')
content = f.readlines()
# 2.找到pthon所在的位置，在前面插入need
index = content[0].find('Python')
print(content)
print(index)
content[0] = content[0][:index] + ' need ' + content[0][index:-2]
print(content)

f.seek(0, 0)
f.write(content[0])
f.close()

# 4.保存文件，把文件重命名为“data-end.txt”
os.rename('D:\\Study\\data.txt', 'D:\\Study\\data-end.txt')

f.close()
