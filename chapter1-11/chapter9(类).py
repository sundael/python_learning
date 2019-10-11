# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 16:37:09 2019

@author: 13225
"""
#创建dog类
class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name.title()+" is now sitting.")
    def roll_over(self):
        print(self.name.title()+" rolled over")
my_dog=Dog('willie',6)
print("My dog's name is "+my_dog.name.title())
my_dog.sit()

#car实例
class Car():
    def __init__(self,make,model,year):
    """初始化汽车属性"""
     self.make=make
     self.model=model
     self.year=year
     self.odometer_reading=0
    def get_descriptive_name(self):
    """返回整洁的描述属性""""
         full_name=str(self.year)+" "+self.make+" "+self.model
         return full_name.title()
    def read_odometer(self):
    """描述汽车里程"""
         print("This car has "+str(self.odometer_reading)+" miles on it.") 
#通过方法修改属性值
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You cannot roll back an odometer")
#通过方法对属性的值进行递增
    def increment_odometer(self,miles):
        self.odometer_reading +=miles
class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kWh battery")
    def get_range(self):
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270
        message="This car can go "+str(range)+" miles on a full charge."
        print(message)
my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(100)
my_new_car.increment_odometer(69)
my_new_car.read_odometer()
#继承
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):  #方法接受创建Car实例所需的信
        super().__init__(make,model,year)   #调用父类方法
        self.battery=Battery()
my_tesla=ElectricCar('telsa','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

        


