# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 08:36:08 2024

@author: admin
"""

# Agenda for Wednesday

# repetition
# os and files 
# lambda functions - usefull - example with sorting
# Modules and packages
# Python Virtual environments
# Object Oriented Programming in Python
# Git - Source control  - version1, version2, finalversion_3


# repetition

# reading and writing to a file from python

# built in function called open
# with makes sure the file is closed afterwards
# 
import os # operating system
os.chdir(r'C:\PythonCourse225')

filename='data.txt' 
with open(filename,'w',encoding='utf-8') as myfile:
    myfile.write('First line in our file!\n')


print('Now the file is closed')

myfile.closed

os.getcwd()

os.chdir(r'C:\PythonCourse225')

filelist=os.listdir()

filename=r'C:\PythonCourse225\data.txt'

fileinfoTuple=os.path.split(filename)

foldername,filename = os.path.split(filename)

foldername=r'C:\PythonCourse225'

# join function - it can put a foldername and a filename together

fullpath=os.path.join(foldername, filename)

print(fullpath)

# current working directory
os.getcwd()

os.chdir(r'C:\PythonCourse225')

# a full list of all files and folders 
filelist=os.listdir()

filename = 'day1.py'

filename.endswith('.py')

'day' in  filename

# list comprehensions

# we want to have a list with all py files from the filelist

[filename for filename in filelist if filename.endswith('.py')]


numberlist = [4,7,8,3,9,0,1]

# pick numbers above 5 from the list

[number for number in numberlist if number>5]

##################################################################
# functions
##################################################################

# a piece of code in python with a name
# and it has return type (maybe None)
# can have 0,1,2, ... inputparameters
# recognize something is a function by the parenthesis after the name

# we create a function which always returns the last element of a list

def getLastItemFromList(thelist : list):
    return thelist[-1]


getLastItemFromList([4,87,1,3,9,5])

getLastItemFromList((4,87,1,3,9,5))

# let's create a function to parse a date from a string or from a number



danishDate = '28-02-2024'

# we need a function to convert a Danish date into a date data type in Python

import datetime

today=datetime.date(2024,2,26)

datetime.datetime.strptime(danishDate, '%d-%m-%Y')

def getDateFromDanishString(danishDate : str):
    return datetime.datetime.strptime(danishDate, '%d-%m-%Y')


dateList = ['28-03-2021','28-02-2024','18-02-2022']


dateList=  [ getDateFromDanishString(date) for date in dateList   ]


dateAsInt= 20240228

datetime.datetime.strptime(str(dateAsInt), '%Y%m%d')


dateAsInt // 10000
dateAsInt % 100

datetime.date(dateAsInt // 10000,2,26)

uglydate='aælkfjdsaælfjsadælf 31/01/22 23:59:59.999999 afælkjadælfkjsafd'

uglydate[0:5]

idx=uglydate.index('/')-2

uglydate[idx:idx+17]

#####################################################
# discussing lambda functions

students = [
    {'name':'john', 'grade':'A', 'age':15},
    {'name':'jane', 'grade':'B', 'age':12},
    {'name':'dave', 'grade':'B', 'age':10}
]

# challenge - we want to sort the list with youngest studen first

students = [
    ['john', 'A', 15],
    ['jane', 'B', 17],
    ['dave', 'B', 10]
]


# seems that the sorting just takes the first element and sorts by that
sorted(students)

sorted(students,key=getLastItemFromList)
# lambda means an anonymous function
sorted(students,key=lambda student : student[-1])

sorted(students,key=lambda student : student[1],reverse=True)

students = [
    {'name':'john', 'grade':'A', 'age':15},
    {'name':'jane', 'grade':'B', 'age':12},
    {'name':'dave', 'grade':'B', 'age':10}
]

sorted(students, key=lambda student : student['age'])

sorted(students, key=lambda student : student['grade']+student['name'])

sorted(students, key=lambda student : student['grade'])


# we have an exercise with a csv file with some temperatures from Mars
filename='data.txt' 
with open(filename,'w',encoding='utf-8') as myfile:
    myfile.write('First line in our file!\n')


filename=r'C:\PythonCourse225\MPF_subset_data.csv'
with open(filename,'r') as myfile:
    rowline=myfile.readline()    
    while rowline:
        print(rowline,end='')
        rowline=myfile.readline()
        
# compute the average temperature for the last three columns
# just using the open function and classic python functions

data='2,11:30:07,2.466424,-28.2,-24.2,-21.0'
data.split(',')

# break for 15 minutes 

###################################################################

# 
T1=[]
T2=[]
T3=[]

filename=r'C:\PythonCourse225\MPF_subset_data.csv'
with open(filename,'r') as myfile:
    rowline=myfile.readline()    
    while rowline:
        print(rowline,end='')
        if not '"' in rowline:
            # then it's a datarow
            T1.append(float(rowline.split(',')[-3]))
            T2.append(float(rowline.split(',')[-2]))
            T3.append(float(rowline.split(',')[-1]))
        rowline=myfile.readline()

sum(T1)/len(T1)


filelist.index('news')


# Modules and packages - module 7

import os

os.environ

# the path in windows here
os.environ['PATH']

# How do we install modules for python

# if we just have a basic python installation from python.org
# then most people just use pip.exe (windows) for installing modules

"""
import sys
print(sys.executable)
"""
# C:\Users\admin\AppData\Local\Programs\Python\Python312\python.exe"""

# pip install pandas

# but it's much better to define a virtual environment for our project
# where we only install the required modules for that python project


# plan for the afternoon:

    # virtual environments and spyder

    # Object Oriented Programming in Python

    # Git - Source control  - version1, version2, finalversion_3

################################################################
# Object Oriented Programming in Python
################################################################

# Class definition will then contain:
# student:
    # Properties/ attributes
        # firstname
        # studentNo
        # grade
        # lastname
        # cpr
        # dateofbirth
    # Functions:    
        # computeHisAge()
        # savetodb()
        # exporttocsv()
        # promotetonextschoolyear()


# Car
    # Properties:
        # price
        # Brand
        # Model
        # kmNo
        # hasFlootMats
        # isStationWagon
        # TypeOfVehicle
        # FuelType
        # KmPrLiter
        # previuosOwnerWasASmoker
    # functions:
        # MarkAsSold()
        # EstimatePriceBasedOnDataForThisCar()
        
        
# we make a class now for a student:

from datetime import date
    
class Student:        
    # we need a special function to define a student    
    def __init__(self,firstname,lastname,dateofbirth):
        self.firstName = firstname
        self.lastName = lastname
        self.dob = dateofbirth
        if self.firstName=='Harry':
            self.houseName = 'Gryffindor'
        else:
            self.houseName='Slytherin'
        
    def __str__(self):
        return f'{self.lastName}, {self.firstName}'
    
    
    def getage(self):
        # lazy implementation
        timediff = date.today() - self.dob
        return timediff.days //365
    
# here we construct a Student
# this means we call the __init__ function by providing the class Name Student
# student1 is a Student object
student1 = Student('Harry','Potter',date(1980,7,31))
student1.getage()
student1.houseName    
student1.getage()
print(student1)

# student2 is also an object 
student2 = Student('Ron','Weasley',date(1980,4,22))
student2.houseName
# in python all our types are classes 

# in C++ int and float are not classes  - it's just simple types
# and in C++ you can have classes without a constructor 
# that means you can have classes with a lot of helper functions



potterTuple=('Harry','Potter',date(1980,7,31))

potterTuple[0]

student1.firstName

student1.firstName
# break until 14.35



from dataclasses import dataclass

# a more modern way today to construct a class
# but you may often want to implement the __init__ and so on your self
@dataclass # a decorator
class Circle:
    # properties
    radius : int
    centerX : int
    centerY : int

c1 = Circle(10,0,0)

print(c1)











