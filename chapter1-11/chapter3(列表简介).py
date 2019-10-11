# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 16:45:16 2019

@author: 13225
"""
bicycles=["trek","cannondale","redline","specialized"]
print(bicycles[-1].title())
#列表末尾添加元素
bicycles.append('ducati')
print(bicycles)
#插入元素
bicycles.insert(0,'yeb')
print(bicycles)

#使用pop删除末尾元素
poped_bicycles=bicycles.pop()
print(poped_bicycles)
print(bicycles)

#remove根据值删除元素，只能删除第一个
bicycles.remove('trek')
print(bicycles)

#使用sort永久排序,sorted临时排序
cars=['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)
cars.reverse()
print(cars)
