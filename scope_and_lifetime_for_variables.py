# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 14:18:16 2024

@author: admin
"""

# we have a scope for variables
# in the main file
# and another one inside a function

numberOfPeople = 11

print('Main program',numberOfPeople)

def myfunction1():
    # this is just the one from outside
    print('Inside myfunction1',numberOfPeople)
    
myfunction1()    

def myfunction2():
    
    # this variable is local to the function myfunction2
    numberOfPeople = 12
    print('Inside myfunction2',numberOfPeople)

# NOT BEST PRACTISE
def myfunction3():
    global numberOfPeople # regard it as the one from outside
    # this variable is local to the function myfunction2
    numberOfPeople = 666
    print('Inside myfunction3',numberOfPeople)

def myfunction4():    
    
    numberOfPeople = 666
    print('Inside myfunction4',numberOfPeople)
    return numberOfPeople
    

myfunction2()     
    
print('Main program',numberOfPeople)

#myfunction3()     
    
# print('Main program',numberOfPeople)

numberOfPeople=myfunction4()

print('Main program',numberOfPeople)

