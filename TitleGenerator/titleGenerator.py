#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author: "sailorsinbad14"
# copyright: "Copyright 2020 by sailorsinbad14"
#license: "GPL"
# version: "3.0"
# email: "sailorsinbad14@gmail.com"


# 调试用: 测试当前python编码, 一般默认为UTF-8
# import sys
# print(sys.getdefaultencoding())

# 导入 rawData.csv 中各列, 每列标题请严格按照下方范例命名和排序制表, 否则无法识别. 具体请参照 export.csv 范本
import pandas as pd
df = pd.read_csv('rawData.csv')
brand = df['Brand']
logo = df['Logo']
color = df['Color']
coreWords = df['Core Words']
usage = df['Usage']

# 合成的标题将首先储存与此
result=[]

# 标题合成
for b in brand:
    if not (str(b).lower() =='nan'):
        for l in logo:
            if not (str(l).lower() =='nan'):
                for cl in color:
                    if not (str(cl).lower() == 'nan'):
                        for c in coreWords:
                            if not (str(c).lower() =='nan'):
                                for u in usage:
                                    if not (str(u).lower() =='nan'):
                                        title = str(b).title() + ' ' + str(l).title() + ' ' + str(cl).title() + ' ' + str(c).title()+ ' ' + str(u).title()
                                        result.append(title)
                                        title = ''

# 导出合成的标题到 export.csv ,如果当前文件夹没有则新建, 已有则覆盖
ex = pd.DataFrame(result)
ex.to_csv('export.csv')
