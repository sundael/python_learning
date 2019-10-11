# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 09:02:01 2019

@author: 13225
"""

cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())
        
#检查特定值是否在列表中
requested_toppings=['mushrooms','onionns','pineapple']
'mushrooms' in requested_toppings

car='subaru'
print("Is car=='subaru'?I predict True.")
print(car=='subaru')

#if-elif-else
age=14
if age < 4:
    print("Your admission cost is $0.")
elif age<18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

if age <4:
    price=0
elif age<18:
    price=5
else:
    price=10
print("your admission cost is $"+str(price))

#确定列表不是空的
requested_tops=[]
if requested_tops:                          #检查列表元素是否为空
    for requested_top in requested_tops:
        print("Adding"+requested_top+".")
    print("\nFinshed making your pizza!")
else:
    print("Are you want a plain pizza?")