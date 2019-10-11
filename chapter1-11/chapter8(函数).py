# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 15:13:09 2019

@author: 13225
"""
#使用任意数量的关键字实参
def build_profile(first,last,**user_info):
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile
user_profile=build_profile('albert','estiein',location='princeton',field='physics')
print(user_profile)

#用as给函数/模块指定别名
