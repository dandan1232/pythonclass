# -*- coding: utf-8 -*-
# @Time    : 2021/10/4 8:25
# @Author  : Lindand
# @File    : Func.py
# @Description :

def 炼丹炉(func):
    def 变身(*args, **kwargs):
        print('有火眼金睛了')
        return func(*args, **kwargs)

    return 变身


def 龙宫走一趟(func):
    def 你好(*args, **kwargs):
        print('有金箍棒了')
        return func(*args, **kwargs)

    return 你好


def 拜师学艺(func):
    def 师傅(*args, **kwargs):
        print('学会飞、72变了')
        return func(*args, **kwargs)

    return 师傅


@拜师学艺
@龙宫走一趟
@炼丹炉
def 孙悟空():
    print('吃桃子')


if __name__ == '__main__':
    孙悟空()

# 输出
# 学会飞、72变了
# 有金箍棒了
# 有火眼金睛了
# 吃桃子
