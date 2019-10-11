# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 20:58:15 2019

@author: 13225
"""

with open('C:/Users/13225/Desktop/py project/pi_digits.txt',encoding='UTF-8') as file_object:
   for line in file_object:
       print(line.rstrip())
      
#创建一个包含文件各行内容的列表
with open('C:/Users/13225/Desktop/py project/pi_digits.txt',encoding='UTF-8') as file_object:
    lines=file_object.readlines()    #读取每一行，将其存储在一个列表中
pi_string=''
for line in lines:
    pi_string+=line.rstrip()
print(pi_string)
print(len(pi_string))
#百万小数点的pi
with open('C:/Users/13225/Downloads/python_peitao/chapter_10/pi_million_digits.txt',encoding='UTF-8') as filename:
    lines_m=filename.readlines()
pi_string_m=''
for line in lines_m:
    pi_string_m+=line.strip()
print(pi_string_m[:52])
print(len(pi_string_m))
#判断生日是否在圆周率中
birthday=input("please input your birthday: ")
if birthday in pi_string_m:
    print("Your birthday in the file")
else:
    print("Your birthday is not in the file")

#写文件
filename='C:/Users/13225/Desktop/py project/programming.txt'
with open(filename,'w') as filename_object:
    filename_object.write("I love python\n")
#附加到文件
with open('C:/Users/13225/Desktop/py project/programming.txt','a') as filename_o:
    filename_o.write('why?\n')
    filename_o.write('funny')
    
"""异常"""
print("give me 2 numbers to divide them\nprint 'q' to exit")
while True:
    first_number=input('Please input the first number')
    if first_number=='q':
        break
    second_number=input('Please input the second number')
    if second_number=='q':
        break
    try:
        answer=int(first_number)/int(second_number)
        print(answer)
    except ZeroDivisionError:
        print('you an not set the second number 0')
        
"""分析文本"""
def word_count(filenamea):    
    try:
        with open(filenamea,'r') as f_obj:
             contents=f_obj.read()
    except FileNotFoundError:
        print("the route is not exisit")
    else:
        words=contents.split()
        num_words=len(words)
        print("文本有"+str(num_words)+"个字符串")
word_count('C:/Users/13225/Downloads/python_peitao/chapter_10/alice.txt')
filenames=['C:/Users/13225/Downloads/python_peitao/chapter_10/alice.txt',
           'C:/Users/13225/Downloads/python_peitao/chapter_10/little_women.txt']
for filename in filenames:
    word_count(filename)

#存储数据
"""写json"""
import json
numbers=[1,2,3,4,5]
file_n='C:/Users/13225/Desktop/py project/numbers.json'
with open(file_n,'w') as file_obj:
    json.dump(numbers,file_obj)
"""读json"""
with open('C:/Users/13225/Desktop/py project/numbers.json','r') as fj:
    nuber=json.load(fj)
print(nuber)

##remember me.py
file_n='C:/Users/13225/Desktop/py project/username.json'
try:
    with open(file_n) as fo:
        username=json.load(fo)
except FileNotFoundError:
    username=input("What is your name? ")
    with open(file_n,'w') as fo:
        json.dump(username,fo)
        print("Welcome, "+username+"\nwe will remember you")
else:
    print("Wlecome")