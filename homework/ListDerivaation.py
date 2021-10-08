# -*- coding: utf-8 -*-
# @Time    : 2021/9/18 9:42
# @Author  : Lindand
# @File    : ListDerivaation.py
# @Description :
'''请用列表推导式，按照要求生成列表：
1、生成列表 [0, 4, 16, 36, 64]
2、生成列表[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
3、从 [‘66’, ‘007’, ‘jsy’, ‘JSY’, ‘main’] 提取出全是字母的元素生成新列表
4、从 [‘66’, ‘007’, ‘jsy’, ‘JSY’, ‘main’] 生成新列表[‘66’, ‘007’, ‘JSY’, ‘jsy’, ‘MAIN’]
提示：列表推导式中使用 startswith()、 upper()、lower() 等字符串函数
'''

# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环.
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print([x * x for x in range(0, 10) if x % 2 == 0])

# 通过利用列表的下标，步长和切片操作解决问题
list5 = [i for i in range(1, 10)]
# print(list5)
list6 = [list5[j:j + 3] for j in range(0, len(list5), 3)]
# print(len(list5))
print(list6)

# 列表推导式左边为输出元素，然后从左至右进行嵌套执行的顺序
# 将list3中全字母的元素取出放在list4中
list3 = ['66', '007', 'jsy', 'JSY', 'main']
list4 = [x for x in list3 if x.isalpha()]
print(list4)

# （可迭代指一个范围，使for可循环遍历）
# list = [结果1 if 条件  else  结果2  for i in 可迭代]  （当条件语句含else时，分情况输出）
# 举例子：#如果是 J 开头的则将单词变为小写，不是 J 开头则全部大写
# 对于列表元素的修改
list1 = ['66', '007', 'jsy', 'JSY', 'main']
list2 = [word.lower() if word.startswith('J') else word.upper() for word in list1]
print(list2)
