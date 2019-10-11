# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 11:14:49 2019

@author: 13225
"""

promot="If you tell us who you are,we can personlize the message you see."
promot +="\nWhat is your first name"
name=input(promot)
print("\nHello,"+name+"!")
#使用标志
active=True
while active:
    message=input(promot)
    if message=='quit':
       active=False
    else:
        print(message)

print("hello web")

#break语句
promot1="\nPlease enter the name of a city you have visited:"
promot1 +="\n(Enter 'quit' when you are finished)"
while True:
    city=input(promot1)
    if city=='quit':
        break
    else:
        print("I would love to go to"+city.title()+"!")

#continue语句
current_number=0
while current_number<10:
    current_number+=1
    if current_number%2==0:
        continue
    print(current_number)



#无限循环
unconfirmed_users=['alice','brian','candace']
confirmed_users=[]
while unconfirmed_users:   #列表为空时停止运行
    current_user=unconfirmed_users.pop()
    print("Verifying user:"+current_user)
    confirmed_users.append(current_user)
print("\nthe following have been confirmed")
for confirmed_user in confirmed_users:
    print(confirmed_user)

#使用用户输入来填充字典
responses={}
flag=True
while flag:
    name=input("\nWhat is your name?")
    response=input('Which country would you like to travel?')
    responses[name]=response
    repeat=input('Would you like to continue?(yes or no)')
    if repeat=='no':
        flag=False
print("\n--results--")
for name,response in responses.items():
    print(name+" want to go to"+response)
