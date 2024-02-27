# -*- coding: utf-8 -*-
"""
Day one - python course! """


### DAY 1 One python course

# we can install python from python.org
# or we can install it via Anaconda 
# we get the spyder editor automatically from Anaconda installation

# we saw the python launcher on Windows
# py -0 # shows all versions on the machine

# py helloworld.py

#####################################################
# Module 2  - Variables
#####################################################

# what is a variable?

# A variable is a container that can hold a value/data
# A variable has a name
# A varible has a data type

# we don't specify the type - it becomes an integer (whole number)
shoesize = 42

firstname= "Lionel"
lastname='Messi'
# python does not have Char - we just have strings
# there is NO difference beteween " and '
singleLetter = 'A'

text = 'That is very "cool"'

print(text)
shoesize = 'Thirtyfour'

# decimal values 

# when we type a decimal inside the code - then you use .
priceOneLiterOfMilk = 14.25

#  bool
tookAShowerThisMorning = False

print(shoesize)
print(firstname,lastname)
print(priceOneLiterOfMilk)

firstname + lastname

firstname + ' ' +lastname

print()

print(firstname,lastname,sep='_')

# grabing a string from the console with input function
firstname = input('Please write your firstname:')

# number of characters in the string
len(firstname)

# does not exist
# length()

# None  - null - that means no value 
# None has it's own type called None type

sqlconnection = None # reserved word

# hex number systems 

# 16 digits - 0,1,2, .. 9, a,b,c,d,e,f = f is 15 

# 15 *1 + 15*16
hexValue = 0xff
15 *1 + 15*16

# 517
# 7*1 + 1*10 +  5*10**2

# binary numbers 

# 1111
binaryValue = int('1111',base = 2)

# we want to get the shoenumber from the user as input

# input function always gives a string
shoesize = input('Type your shoe number, please:')

shoesize = int(input('Type your shoe number, please:'))

#shoesize = input(int('Type your shoe number, please:'))

# python is nice to us here
# shoesize = input(int('678'))

print(firstname,lastname)

# formatting text in python
# f stands for format - modern way to do it
f"{lastname}, {firstname} has shoe number {shoesize})"

# the old way - with position numbers in the curly braces

"{0}, {1} and finally {2} ".format(lastname,firstname,shoesize) 

# Break until 10.51

###############################################################


# best practise - use variables with good names
# that will make the code much easier to read

shoesizeAsString = input('Type your shoe number, please:')
shoesize= int(shoesizeAsString)

shoesize = input('Type your shoe number, please:')
shoesize= int(shoesize)

# PEP - python enhancment propals 

# formatting 

price = 12.5678

f"The price is: {price}" 
# 2 decimals
f"The price is: {price:.2f}" 

f"The price is: {round(price,2)}" 

# Time for exercises

# Go for 1.1 and 1.2
# 2.1
# 2.2
# 2.3 Calculating age  - simple version or more advanced
# 2.4
# Extra if you are fast
# calculate the correct age in 2.3

delivery = 32.5
total = 56 
total = total + delivery

#######################################################
# Computations and comparisons
#######################################################

result = 7+5*2          # 17
result = (7+5)*2        #  24

# increment by one
i = 1
i = i + 1

value = 6
value +=4

# math is a module - it's built in to python
import math # we import the math module

math.sqrt(144)
math.sin(math.pi/2)

# the absolute value 
abs(-17)

# comparisons 

5 >= 3 

# we compare strings

scriptlanguage = 'python'
programminglanguage= 'Python'

# equality comparision ==
scriptlanguage == programminglanguage
scriptlanguage.lower() == programminglanguage.lower()

scriptlanguage.upper()

# not equal to 

number1 = 45
number2= 34

number1 != number2

tookAShowerThisMorning
wentToWorkByCar =True

twoRequirements = tookAShowerThisMorning  and wentToWorkByCar

twoRequirementsAtLeastOneIstrue = tookAShowerThisMorning  or wentToWorkByCar

##################################################
# The four collection types in python
##################################################
# 1) list 
# 2) tuple
# 3) set
# 4) dictionary 

#######################################################
# list 
#######################################################
# it's the one with square brackets 

numberlist = [2018,2021,2024]
numberlistMixedContent = ['2018 2021',2024]

namelist = ['Aage','Hans','Jens','Joe','Donald']

# we can change the value on a list
namelist[4]='Christian'

namelist[0]

# Lunch until 12.40

##################################################
# more about lists  
##################################################

namelist = ['Aage','Birger','Carl','Dan','Eric','Frederik']

namelist[2]

namelist[2]='Charlotte'

print(namelist)

print(namelist[2])

for item in namelist:
    print(item)


for name in namelist:
    # indentation block of code - 4 spaces is best practise
    print(name)
    print(name.lower())
    

for name in namelist:
    print(name)
print(name.lower())

# this will work - but it's easier to see 
for name in namelist:
 print(name)
 
namelist.append('Georgina')
 
# 7 elements
len(namelist)

namelist.append(['Hans','Ina'])
# by value we remove
namelist.remove(['Hans','Ina'])

namelist.extend(['Hans','Ina'])

# we add them again
namelist.extend(['Hans','Ina'])

namelist.remove('Hans')

namelist.count('Ina')
namelist.count('Eric')
namelist.count('Camilla')

namelist[0]

namelist[1]

namelist[9]
# last element is always just called -1
namelist[-1]
namelist[-2]

# we remove the last Ina - to have unique elements
del namelist[-1]

# slicing 
# it always gives a list - so it's a subset of a list

# we get a list with names from position 0 and up to 2
namelist[0:3]

namelist[4:7]

namelist=namelist[0:3] + ['Gollum'] + namelist[3:]
# index error
namelist[10]='Ben'
# slicing does not check the value whether it's too big
namelist[6:10011]

scriptlanguage='python'

for letter in scriptlanguage:
    print(letter)

scriptlanguage[0:3]
# 'str' object does not support item assignment
scriptlanguage[1]= 'Y'

namelist.append(scriptlanguage)

valuesAsText = input('Please type 5 numbers - seperate them with space')

numberlistText = valuesAsText.split(' ')

for number in numberlistText:
    number=int(number)

numberlist=[]

for number in numberlistText:
    value=int(number)
    numberlist.append(value)
    
# 2) tuple
# recognize it by the parenthesis

# read only
# a tuple is immutable
customertuple = ('Lionel','Messi',43,38,123.56)

# a list is mutable - it means we can change it 
customerList=['Lionel','Messi',43,38,123.56]
    
customertuple[1]    
# 'tuple' object does not support item assignment  
customertuple[1]='Ronaldo'

id(customerList)
customerList.append('Miami')

id(customertuple)
customertuple = ('Lionel','Messi',43,38,123.56,'Miami')
id(customertuple)

number1, number2 = 67,89

number1, number2 = (67,89)

(number1, number2) = (67,89)
# _ skip the value - but it is there
(number1,_,number2) = (67,22,89)

(number1,*rest,number2) = (67,22,45,8,9,11,89)

# 3) set -- 
# a set is written with Tuborg/curly braces
numbersetA = {2,4,6,8,10}
numbersetB = {4,8,12}

# intersection - what do the two sets have in common?

numbersetA & numbersetB

# what is A or in B? The union
numbersetA | numbersetB

# in A but NOT in B

numbersetA - numbersetB

numbersetB - numbersetA
# elements in a set are unique
numbersetA = {2,4,6,8,10,2,2,2,2,2,2,2,2}

numbersetA.add(0)
len(numbersetA)

namelist

namelist = ['Aage','Birger','Carl','Dan','Eric','Dan']

nameSet = set(namelist)

areNamesUniqueOnTheList = len(namelist)== len(nameSet)

# the dictionary 


# customertuple[2]
# this could be nice
# customer['shoesize']

# the dictionary 
# has always key and value as data

customerDictionary = {'firstname' :'Lionel', 
                      'lastname':'Messi',
                      'shoesize' : 43,
                      'age' : 38,
                      'price' : 123.567}


customerDictionary['shoesize']

customerDictionary['shoesize']=44
# adding an element to the dictionary - or overwritting it- if it exists
customerDictionary['Country']='Argentina'

print(customerDictionary)

for item in customerDictionary:
    print(item)


for item in customerDictionary:
    print(item,customerDictionary[item])


for key in customerDictionary.keys():
    print(key,customerDictionary[key])

for value in customerDictionary.values():
    print(value)

# k,v is a tuple here 
for k,v in customerDictionary.items():
    print(k,v)

for (k,v) in customerDictionary.items():
    print(k,v)

exerciseName = 'exercise 2.4'
# exercise together

numberlist = [3,7,8]
sum(numberlist)

# this removes the sum variable again
# and python now has the built in sum function again
del sum

# exercise 2.5 in the pdf document

'22'*5
'22'+'22'+'22'+'22'+'22'

goods = [ 'Apples', 'Pears', 'Bananas', 'Cherries']
prices = [ 5, 4, 6, 20 ]
#count = [0,0,0,0] 
count=[]
totalsum = 0  # sum is not a good name for a variable - because we overwrite the built in function 
#for i in range(0,4):
for i in range(0,4):
    print(f'{goods[i]} is {prices[i]} kr.')
    print(f'How many {goods[i]} do you want : ')
    count.append(int(input()))
    price = prices[i] * count[i]
    print(f'Cost: {price} kr.')
    totalsum = totalsum + price
price = 32.5;
print(f'Delivery charge is {price} kr.')
totalsum = totalsum + price
print(f'Total : {totalsum} kr.')


goods = [ 'Apples', 'Pears', 'Bananas', 'Cherries']
prices = [ 5, 4, 6, 20 ]
#count = [0,0,0,0] 
count = 4*[0] 
#count=[]
totalsum = 0  # sum is not a good name for a variable - because we overwrite the built in function 
#for i in range(0,4):
for i in range(0,4):
    print(f'{goods[i]} is {prices[i]} kr.')
    print(f'How many {goods[i]} do you want : ')
    count[i]=(int(input()))
    price = prices[i] * count[i]
    print(f'Cost: {price} kr.')
    totalsum = totalsum + price
price = 32.5;
print(f'Delivery charge is {price} kr.')
totalsum = totalsum + price
print(f'Total : {totalsum} kr.')

# f stands for format - it merges the variable values into the {}
f"here is some text {price}"

"here is some text {price}"

f"here is some text {2+6}"

numberlist.extend([3,9])
numberlist.extend({'python'})

# Exercises : 2.8, 2.9, 2.10, 2.11 and 2.12

# lists
numberlist=[1,2,5]
numberlist.append(3)
2 in numberlist
numberlist[1]
numberlist[1]=222
# count the number of items with the len function
numberOfItems=len(numberlist)
# tip sorted, sum, max and min bare built in functions
max(numberlist)
# Coffee break until 14.50

# sets 
setA={'red','blue','green'}

# exec - executes the dynamic code built from a string
# not best practise - but might sometimes be necessary
exec('number2=45')
for k in range(7):
    exec("print(f'P{k+1}')")
for k in range(7):
    f'P{k+1} = np.array(Sheet2[:,k+2])'
f"some text"

# loop for a dictionary to provide key and value

for k,v in customerDictionary.items():
    print(k,v)
    
#######################################################
# 
#######################################################

# F5 vs F9
# see mytinyscript.py file

# datetime and date in python

import datetime

# we get a variable with the type date
currentdate=datetime.date.today()

currentdate.year
currentdate.month
currentdate.day

# how to print dates in a nice format
# yyyy_mm_dd_hh_mm_ss

logfilename=f"datalog_{currentdate}.log"

logfilename=f"datalog_{currentdate:%Y_%m_%d}.log"

# datetime is the type for a timestamp

currentTimestamp=datetime.datetime.now()
print(currentTimestamp)
logfilename=f"datalog_{currentTimestamp:%Y_%m_%d_%H_%M_%S}.log"

logfilename=f"datalog_{currentTimestamp:%Y_%m_%d_%H_%M}.log"

# how can we create a date - where we specify the year, month and so on?

birthDate = datetime.date(2005,11,10)

# the difference when we subtract the currentdate and the birthdate

timeDifference = currentdate - birthDate

timeDifference.days/365.25

timestampagain = datetime.datetime.now()

result =timestampagain - currentTimestamp

# many people prefer to just import the date
# so you don't have to write the prefix with the module name


from datetime import date
thisday=date.today()










