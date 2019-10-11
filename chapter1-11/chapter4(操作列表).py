# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 17:32:00 2019

@author: 13225
"""

magicians=['alice','david','carolina']
for magician in magicians:
    print(magician)


#创建数字列表
numbers=list(range(1,6))
print(numbers)

squares=[]
for square in range(1,11):
    square=square**2
    squares.append(square)
print(squares)

#列表解析
squs=[value**2 for value in range(1,11)]
print(squs)


#切片
players=['charles','martina','michael','florence','eli']
print(players[0:3])
#遍历切片
for player in players:
    print(player.title())
#复制列表
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(friend_foods)
#元组(修改整个元组来修改元组变量)
dimensions=(200,50)
print('the origial dimension is:')
for dimension in dimensions:
    print(dimension)
dimensions=(400,100)
print('the modified dimension is:')
for dimension in dimensions:
    print(dimension)
    
    

