# -*- coding: utf-8 -*-
# @Time    : 2021/9/18 16:13
# @Author  : Lindand
# @File    : EmployeesInput.py
# @Description :
'''需要编程录入4位员工的薪资，请按照以下要求完成程序：
1、用字典或列表和字典组合记录员工的姓名和工资
2、结合循环语句和else语句，录入员工的薪资；全部录入后，打印提示“您已经全部录入4名员工的薪资”
3、输入员工的薪资时，若薪资小于1000则重新输入
4、录入过程中，可以输入‘Q’或‘q’提前结束录入，且之前录入的薪资作废
5、4位员工的薪资都正常录入，则打印出录入员工的姓名和薪资明细，以及平均薪资
'''

Sum = 0
Count = 0
salarys = 0
EmpSal_list = []

for i in range(4):
    emp = input("请输入员工姓名:")
    s = input("请输入%s的薪资(按Q或q结束):" % emp)
    if s.upper() == 'Q' or s.upper() == 'q':
        print("录入完成，退出")
        break
    if float(s) < 1000:
        print("不可能那么少啦，请重新输入！！")
        s = input("请重新输入:")
        Sum += float(s)
        EmpSal_dict = {'姓名:': emp, '薪资:': s}
        EmpSal_list.append(EmpSal_dict)
        Count += 1
        continue
    Count += 1
    Sum += float(s)
    EmpSal_dict = {'姓名:': emp, '薪资:': s}
    # print(EmpSal_dict)
    EmpSal_list.append(EmpSal_dict)
else:
    print("您已经全部录入4名员工的薪资:\n" + str(EmpSal_list))

if (Count == 0):
    print("录入员工数为0，已结束")
else:
    print("员工数:{0}".format(Count))
    print("总工资数为：" + str(Sum))
    print("平均薪资:{0}".format(Sum / Count))
