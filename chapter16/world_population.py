# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 21:42:14 2019

@author: 13225
"""
import json
import pygal_maps_world
from countries import get_country_code
from pygal.style import RotateStyle
##加亮颜色主题
from pygal.style import LightColorizedStyle
##文件
filename='population_data.json'
with open(filename) as f:
    pop_data=json.load(f)
    
cc_population={}
for pop_dict in pop_data:
    if pop_dict['Year']=='2010':
        country_name=pop_dict['Country Name']
        code=get_country_code(country_name)
        population=int(float(pop_dict['Value']))
        if code:
            cc_population[code]=population
cc_pop_1={}
cc_pop_2={}
cc_pop_3={}
for cc,pop in cc_population.items():
    if pop<10000000:
        cc_pop_1[cc]=pop
    elif pop>1000000000:
        cc_pop_3[cc]=pop
    else:
        cc_pop_2[cc]=pop
print(len(cc_pop_1),len(cc_pop_2),len(cc_pop_3))
##颜色主题
wm_style=RotateStyle('#BB6699',base_style=LightColorizedStyle)
wm=pygal_maps_world.maps.World(style=wm_style)
wm.title='World population in 2010'
wm.add('0-10m',cc_pop_1)
wm.add('10m-1bm',cc_pop_2)
wm.add('>1bm',cc_pop_3)

wm.render_to_file('world_population.svg')
       