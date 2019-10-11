# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 10:27:50 2019

@author: 13225
"""

from name_function import get_formatted_name
print("Enter 'q' to exit")
while True:
         first_number=input('Please input the first number')
         if first_number=='q':
            break
         second_number=input('Please input the second number')
         if second_number=='q':
            break
         formatted_name=get_formatted_name(first_number,second_number)
         print(formatted_name)
#使用类的方法测试
import unittest
class NmaeTestCase(unittest.TestCase):
    def test_f_l_name(self):
        formatted_name=get_formatted_name('hm','sad')
        self.assertEqual(formatted_name,'Hm Sad')
unittest.main()


#测试AnonymousSurvey类
from survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question="Which language?"
        self.my_survey=AnonymousSurvey(question)
        self.responses=['Chinese','English','shanghai']
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])    
        self.assertIn(self.responses[0],self.my_survey.responses)
    def test_store_three_response(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)
unittest.main()
