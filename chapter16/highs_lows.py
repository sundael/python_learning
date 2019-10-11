# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 20:45:52 2019

@author: 13225
"""

import csv
from matplotlib import pyplot as plt
from datetime import datetime
filename='sitka_weather_2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    next_row=next(reader)
    #打印文件头及其位置
    for index,colunm_header in enumerate(next_row):   #enumerate获取每个元素的索引及值
        print(index,colunm_header)
    highs=[]
    dates=[]
    lows=[]
    for row in reader:
        date=datetime.strptime(row[0],"%Y-%m-%d")  #把原始数据转换为datetime对象
        dates.append(date)
        lows.append(int(row[3]))
        highs.append(int(row[1]))
    print(highs)

#绘制图形
fig=plt.figure(dpi=128,figsize=(5,3))
plt.plot(dates,highs,c='blue',alpha=0.5)
plt.plot(dates,lows,c='red',alpha=0.5)

#设置格式
plt.title("high temp a day",fontsize=5)
plt.xlabel('',fontsize=5)
fig.autofmt_xdate()   #绘制斜日期标签
plt.ylabel('(F)',fontsize=5)
plt.tick_params(axis='both',which='major',labelsize=5)
plt.fill_between(dates,highs,lows,facecolor='yellow',alpha=0.3)
plt.show()