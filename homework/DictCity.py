# -*- coding: utf-8 -*-
# @Time    : 2021/9/17 14:58
# @Author  : Lindand
# @File    : DictCity.py
# @Description :字典城市、国家和人口数

cities = {
    'SuZhou': {
        'country': 'China',
        'population': '25 million',
    },
    'Tokyo': {
        'country': 'America',
        'population': '31 million',
    },
    'ShangHai': {
        'country': 'China',
        'population': '40.1 million',
    },
}

for name, info1 in cities.items():
    print(name + ':')
    for key, info2 in info1.items():
        print('\t' + key + ':  ' + info2)
