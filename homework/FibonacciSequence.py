# -*- coding: utf-8 -*-
# @Time    : 2021/9/27 8:30
# @Author  : Lindand
# @File    : FibonacciSequence.py
# @Description :斐波那契数列指的是这样一个数列：1、1、2、3、5、8、13、21、34、……
# 在数学上，斐波纳契数列以如下被以递归的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)(n>=2，n∈N*)

# 方法一
# 递归的写法
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def main():
    n = int(input("请输入求解第几项： "))
    num = fib(n)
    print("结果为%d" % num)


if __name__ == '__main__':
    main()

# 方法二
# 通过迭代的方式
# a = [1, 1]
# fib = int(input("请输入求解前几项："))
# for i in range(2, fib):
#     a.append(a[i - 1] + a[i - 2])
# print(a)

n = int(input("请输入求解第几项： "))


def fibon(n):
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a + b
    return b


print(fibon(n))
