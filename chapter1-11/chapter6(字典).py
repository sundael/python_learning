# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 10:01:55 2019

@author: 13225
"""

#添加键值对
alien_0={'color':'green','points':5,'speed':'medium'}
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)
if alien_0['speed']=='slow':
     x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3
alien_0['x_position']=alien_0['x_position']+x_increment
print("New x_position:"+str(alien_0['x_position']))

#删除键值对
del alien_0['points']
print(alien_0)

#遍历字典
user_0={'username':'efermi',
        'first':'enrico',
        'last':'fermi',
        }
for key,value in user_0.items():
    print("\nKey:"+key)
    print("Value:"+value)

#遍历字典中所有键
favorite_languages={
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python',
        }
 
friends=['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:          #检查名字是否在列表中
        print("Hi"+name.title()+",I see your favorite language is"+favorite_languages[name].title())
#sorted排序
for name in sorted(favorite_languages.keys()): 
    print(name.title())
#在列表中存储字典
aliens=[]
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['points']=10
        alien['speed']='fast'
for alien in aliens[:6]:
    print(alien)
#在字典中存储列表
#在字典中存储字典
users={
       'aeinstein':{
               'first':'albert',
               'last':'einstein',
               'location':'princeton',},
       'mcurie':{
               'first':'marie',
               'last':'curie',
               'location':'paris',}
       }
for username,user_info in users.items():  #先遍历字典条目
    print("\nUsername is "+str(username))
    fullname=user_info['first']+" "+user_info['last']   #信息是字典类型
    location=user_info['location']
    print("\tFullname is "+str(fullname))
    print("\tLocation is "+str(location))
