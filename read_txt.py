#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/15 17:03
# @Author : ZXJ
# @Site : 
# @File : read_txt.py
# @Purpose: PyCharm

import pprint
import re
import pandas as pd
def txt_to_dic(filename, col_name):
    raw_data = {}
    for key in col_name:
        raw_data[key] = []
    for name in filename:
        with open(name, 'r', encoding='utf-8') as ftxt:
            for line in ftxt:
                if 'missing' in line:
                    continue
                new_line = re.sub('( )+', ',', line.strip())
                for i, per in enumerate(new_line.split(',')):
                    # print(per)
                    raw_data[col_name[i]].append(per)
    return raw_data

names = ['press', 'humidity', 'temperature', 'director', 'speed']
file = [r'E:\\风电\\沂山_桃林天融测风塔数据\\沂山天融\\沂山数值预报\\118.7106_36.2031_30_20190101.txt',
       r'E:\\风电\\沂山_桃林天融测风塔数据\\沂山天融\\沂山数值预报\\118.7106_36.2031_30_20190102.txt' ]

# data = txt_to_dic(file, names)
# pprint.pprint(data)
# print(pd.DataFrame(data))







