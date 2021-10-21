# -*- coding: utf-8 -*-
# @Time    : 2021/10/21 14:13
# @Author  : Lindand
# @File    : txtHandle.py
# @Description :
'''要求如下：
1) 打开文件123.txt，使用while True语句读取文件的数据，直到读完为止；
2) 使用try语句检测上述行为；
3) 使用except语句捕获所有的异常，并获取异常描述的具体信息；
4) 使用else语句处理没有异常的情况。
5) 使用finally语句处理释放资源的操作，如关闭文件。
'''


try:
    f = open('D:\\Study\\data.txt')
    while True:
        content = f.readline()
        print(content)
        if not content:
            break
except Exception as err:
    print(err)
else:
    pass
finally:
    print("结束")
    f.close()
