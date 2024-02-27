# -*- coding: utf-8 -*-
"""
DAY 2 Python Course - SU-225"""
# Agenda today

    # repetition
    # control flow - if and while
    # (list) comprehensions - 
    # functions - 
    # working with files
    

# variable
    # scalar variable - can contain one single value
    # string (str), integer (int), float, bool, None
    # a variable has a name
    # a variable has a datatype
    # it's a container
     

# sequences - collections
    # list  []
    # tuple  () - read only - you cannot change number of elements
    # dictionary {}
    # set  {}
    
    
mydictionary={}     # empty dictionary
    
numberlist = [6,8,3]    

# I want to create 100 random numbers betweeen 1 and 20
# and save them in a list

import random
random.randint(1, 20)

# 0.0 <= X < 1.0    
randomfloat = random.random()    

# range function 

interval = range(1,11)

for i in interval:
    print(i)
    
anotherIntervalFromZero = range(10)    
for i in anotherIntervalFromZero:
    print(i)
    
# so i with the range is the standard for loop syntax in python    
for i in range(20):
    print(i)    
    
for item  in numberlist:    
    print(item)
    
for i in range(len(numberlist)):
    print(numberlist[i])
    
numberlist=[]  
  # I want to create 100 random numbers betweeen 1 and 20
  # and save them in a list

for i in range(100):
    randomInt = random.randint(1, 20)  
    numberlist.append(randomInt)
    
# we want to do simple statistics
# we want to know how many times each number appears on the list
# so we want a datastructure like this, where we count occurences as second element:
# [ [1,9],[2,5],.. [20, 6]       ]    

uniqueValueSet=set(numberlist)
#uniqueNumberList = list(uniqueValueSet)

# counts the number of occurences for 19 on the list
numberlist.count(19)

frequencylist = []
for number in uniqueValueSet:
    numberOfOccurrences = numberlist.count(number)
    frequencylist.append([number,numberOfOccurrences])

 # we had a max function yesterday 
# now we want to identify the max occurence

occurencelist =[]

for item in frequencylist:
    occurencelist.append(item[-1])
    
maxfrequency=max(occurencelist)

# we will get back to this example again later
# using more elegant techniques

##################################################
# control flow of a program
##################################################

# conditional code  - if statement

# we can test a condition and execute code when the condition is True

statusCode = 42

if statusCode > 40:
    # this code which is indented belongs to the if statement
    # and is executed when it is true
    print('The code is above 40')


statusCode = 39

if statusCode > 40:
    # this code which is indented belongs to the if statement
    # and is executed when it is true
    print('The code is above 40')
print('This is the final statement')


if statusCode > 40:
    # this code which is indented belongs to the if statement
    # and is executed when it is true
    print('The code is above 40')
else:
    print('That number is below 40 or equal to 40')
print('This is the final statement')

statusCode= 21

if statusCode > 40:
    # this code which is indented belongs to the if statement
    # and is executed when it is true
    print('The code is above 40')
elif statusCode > 20: 
    print('higher than 20')
else:
    print('That number is below 20 or equal to 20')


# classic example with leap years
# every 4th year is a leap year
# 2024 is a leap year

# year%4 gives the remainder by division by 4

# 2003 = 4*500 + 3
2003%4
2003/4  # in python 3 we get a float here (in python 2 we got an integer)
2003//4 # // is integer division

for year in range(2000,2025):
    print(year, year%4)

# so a leap year har a remainder on 0 for %4 
# 1900 was a leap year - 
# centuries should be divisible by 400 to be a leap year 

year = 2003
year = 2024

for year in range(1880,2025):
    if (year%4 == 0 and year%100!=0) or year%400==0 :
        print(year,"It's a leap year!")
    
    else:
        print(year,'Not a leap year')


if year%400==0 :
    print(year,"It's a leap year!")
elif year%4 == 0 and year%100!=0:
    print(year,"It's a leap year!")
else:
    print(year,'Not a leap year')


# creating a folder which does not exist

# \n means newline in a string in python (and in C and C#)
# \\ means a backslash
# \ the escape character to write special characters
# \t

foldername='C:\PythonCourse225\news'

# one way to handle and write backslash is using r for raw
# r means raw - that means python does not interpret the string
foldername=r'C:\PythonCourse225\news'
print(foldername)

price = 12.5687
textWithPriceIn = f"The price is {price}"

# ra
r"The price is {price}"

print(foldername)

# python supports windows folders with slash instead of backslash
foldername='C:/PythonCourse225/news'
print(foldername)

import os 

os.getcwd()

foldername='C:/PythonCourse225'
os.path.exists(foldername)
foldername='C:/PythonCourse225/news'
os.path.exists(foldername)

folderExists = os.path.exists(foldername)
if folderExists:
    print(foldername,'is already there')
else:
    os.mkdir(foldername)
    if os.path.exists(foldername):
        print(foldername,'Now the folder has been created')
    else:
        print('Something went wrong')


#########################################
# looping -when we don't know the number of times to execute a code block
# while loop - 
#########################################

# while loop executes as long as something is true

import time

while True:
    # do something
    print('still running')
    time.sleep(1)



counter= 0
while counter < 10:
    print(counter)
    counter+=1


# we loan 1 million 

capital = 1_000_000 # _ thousand seperator for typing integers
interestrate=0.04
payPrHalfYear=50000 
NoOfPayment = 1
leftToPay = capital*(1+interestrate)-50000

while leftToPay>0:
    print(NoOfPayment,leftToPay)
    leftToPay = leftToPay*(1+interestrate)-50000
    NoOfPayment+=1


# You should create python code where you create a little script
# start with a variable with a random number between 1 and 100
# let the user guess the number
# and you provide tips to the user - is the guess two high or 
# too low

statuscode=1
import random
random.randint(1,10)

if statuscode != 10:
    print('statusCode is 10')
elif statuscode >20:
    print('Code is above 20')
else:
    print('something else')

while counter < 10:
    print(counter)
    counter+=1
    
# Break for 15 minutes
    

# Code review - we look at Frank's code:
    
import random

rightNumber = random.randint(1, 100)

result = 0

while result < 1:

    GuessNumber = int(input(print('Guess a number between 1 and 100:')))

    if GuessNumber > rightNumber:
        print('The number is bigger\n')
    elif GuessNumber < rightNumber:
        print('The number is smaller\n')
    else:
        print('The number is right\n') 
        result = 1


import random
rightNumber = random.randint(1, 100)
guessNumber=0
while guessNumber != rightNumber:
    guessNumber = int(input('Guess a number between 1 and 100:'))
    if guessNumber > rightNumber:
        print('The number is bigger\n')
    elif guessNumber < rightNumber:
        print('The number is smaller\n')
    else:
        print('The number is right\n') 
        
        
result = print('Guess a number between 1 and 100:')

print('Guess a number between 1 and 100:')
guess = int(input())

guess = int(input('Guess a number between 1 and 100:'))



result = False

while not result:

    GuessNumber = int(input(print('Guess a number between 1 and 100:')))

    if GuessNumber > rightNumber:
        print('The number is bigger\n')
    elif GuessNumber < rightNumber:
        print('The number is smaller\n')
    else:
        print('The number is right\n') 
        result = True


################################################################
# Comprehensions - we can use them for list,dictionary, sets and tuple
################################################################
# 
# a better way to generate data in a faster way than adding one element at a time


#list with numbers from 1 to 1_000_000
%%timeit # magic command to measure performance in python interactive console
numberlist=[]
for i in range(1_000_000):
    numberlist.append(i)

# list comprehensions can do this faster and better

numberlistcomp= [i for i in range(10)]

limit=1_000_000
%%timeit
numberlistcomp= [i for i in range(limit)]

# the example with 100 random numbers between 1 and 20

import random
randomNumberList = [random.randint(1,20) for i in range(100)]

# we count the number of occurences 
# we do it with a list comprehension now:
    
frequencylist = [ [i,randomNumberList.count(i)] for i in range(1,21)       ]    
    
# second item:
occurenceList = [item[1]   for item in frequencylist]
# last item
occurenceList = [item[-1]   for item in frequencylist]
maxValue=max(occurenceList)

# comprehension expression can also handle conditions with an if statement

# generate all numbers - not divisble by 3 between 1 and 100

listwithnot3division = [i for i in range(1,101) if i%3!=0]

# think of it as a selection here -those where the condition is true are selected
maxOccurenceElements = [item for item in frequencylist if item[-1]==maxValue]

# let's make a list with all olympic years between 1970 and now

startYear = 1970
endYear = 2024
summerOlympicYears = [2*year for year in range(startYear,endYear+1)            ]

numberlist= [i for i in range(0,10)]
[i*i for i in range(0,10)]


numberlist= [2 for i in range(0,10)]

for i in range(10):
    numberlist.append(2)

startYear = 1972
endYear = 2024
summerOlympicYears = [year for year in range(startYear,endYear+1,4)]
# 2020 was not an olympic year because of covid19

summerOlympicYears = [year for year in range(startYear,endYear+1) if (year%4==0 and year!=2020) or year==2021 ]

# Sometimes we need longer comments or multi line text in python 

# 
import this # gives the poem below

"""
startYear = 1972
endYear = 2024
summerOlympicYears = [year for year in range(startYear,endYear+1,4)]
# 2020 was not an olympic year because of covid19
"""

pythonpoem="""The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# we need to count the word frequency in this poem
# which words occurs most?
# lower case and upper case is regarded equal

wordlist = (pythonpoem.lower()
            .replace('\n',' ')
            .replace(',','')
            .replace('.','')
            .replace('**','')
            .replace('--','')
            .replace('!','')
            .split(' '))        

# we want a dictionary now with all words and numberOfOccurences
# we use a comprehension

uniqueWords = set(wordlist)
wordDictionary = {word: wordlist.count(word)  for word in  uniqueWords    }

wordDictionary['be']

wordlist.count('is')
wordlist.count('be')

###########################################################
# Introduction to functions
###########################################################

# we have built in functions 

# What is a function?
# A thing that does something

# In mathematics a function often computes something for us
# f(x) = 2*x + 3
# e.g x = 5  then f(5) = 2*5 + 3 = 13
# so we have input value 5 and output value 13 here

# What is a function?
    # A thing that does something
    # a piece of code that does something and always return an output - might be None
    # A function has a name
    # It's a piece of code that we give a name
    # so we can reuse it and call it every time we want to execute it
    

    # def means now we define a function
    # a boring function with no input parameters
def printMainmenu():
    print(20*'-')
    print('Main Menu')
    print(20*'-')
    print('1) Play guess a number')
    print('2) Leap year computation')
    print('3) Summerolympic years')


printMainmenu()

result = printMainmenu()

result = print('nothing is returned here - result will be none')

# let's create a simple function - which sums two numbers

def computesum(number1,number2):
    return number1+number2


result = computesum(67,5)

computesum()

# the sequence matters - the computesum2 is not defined yet
computesum2()

def computesum2(number1,number2):
    return number1+number2

computesum('Donald','Duck')

# """ here and now documentation or '''
# or for string variables with multiline text
def computesum(number1 : int,number2 : int) -> int:
    """
    Parameters
    ----------
    number1 : int
        DESCRIPTION.
    number2 : int
        DESCRIPTION.

    Returns
    -------
    int
        DESCRIPTION.

    """
    return number1+number2

computesum('Donald','Duck')

computesum()

# lunch 12.50

#############################################################
# programming a function in Python:
    # A function has a name
    # A function can have 0,1,2.. or more input parameters
    # A function always has a return  type (might be None/void)
    # a function is a block of code which we can reuse
    # recognize it has parenthesis at the end
    # A function is callable
#############################################################

# named parameters  vs positional parameters
# dynamic number of input parameters 

# 5 input parameters
def printAddress(streetname,streetNo, city, zipcode,country):
    print(streetname,streetNo)
    print(zipcode,city)
    print(country)


# positional parameters -- the order is crucial here
printAddress('Poul Due Jensens vej',7,'Bjerringbro',8850,'Denmark')
# named parameters - the order does not matter
printAddress(country='Denmark',city='Bjerringbro',streetname='Poul Due Jensens vej',streetNo=7,zipcode=8850)

def printAddress(streetname,streetNo, city, zipcode,country='Denmark'):
    if country=='Denmark':
        print(streetname,streetNo)
        print(zipcode,city)
        print(country)
    elif country=='us':
        print(streetNo,streetname)
        print(city,zipcode)
        print(country)
    else:
        print('country not supported')

printAddress(country='Denmark',city='Bjerringbro',streetname='Poul Due Jensens vej',streetNo=7,zipcode=8850)
printAddress('Poul Due Jensens vej',7,'Bjerringbro',8850)

printAddress('Hollywood Boulevard',12357,'Beverly Hills',90210,'us')

# a dynamic number of input parameters

def sumfunction(number1,number2):
    return number1+number2

# 2 input parameters
sumfunction(45,2)
# 5 input parameters
sumfunction(45,2,78,1,56)

print('Here is one string param')

print('Here is one string param',2)

print('Here is one string param',2, True)
# 0 input parameters
print()

print()

print('Here is one string param',2, True,sep='_')

print('Firstline')
print('Nextline')
print('the end')


print('Firstline',end='Q')
print('Nextline')
print('the end')
print()

shoenumber=34
type(shoenumber)

def sumfunction(*inputparameters):
    print(type(inputparameters))
    
    
sumfunction(4,5)  
    

def sumfunction(*inputparameters):
    #print(type(inputparameters))
    for parameter in inputparameters:
        print(parameter)


sumfunction(4,5)  

# will often be called *args - args just means arguments
# *inputparameters
# inputparameters can have a dynamic number of input values - the star puts all of them into a tuple
def sumfunction(*inputparameters):
    return sum(inputparameters)

sumfunction(4,5)   
sumfunction(4,5,3,2,1)  

sumfunction('Donald','Duck')

sumfunction(4)  

sumfunction([1,3,5])  

sum()

a,b,c = 4,7,8

a,*b,c = 4,7,7,6,5,8

# one more nice thing about functions in python

price = 100

def computePriceWithTaxIncluded(price):
    return 0.25*price+price


computePriceWithTaxIncluded(price)


def computePriceWithTaxIncludedAndTax(price):
    return (0.25*price+price,0.25*price)

result = computePriceWithTaxIncludedAndTax(1000)

priceWithTax,tax=computePriceWithTaxIncludedAndTax(1000)

# we return to the topic about dynamic paramters
# but now we want a name for each dynamic parameter
# **mydictionary means all named input parameters are put into a dictionary callled mydictionary

# **kwargs is often used as name here instead of mydictionary
# kwargs stands for keyword arguments
def myfunctionWithDictionaryInput(**mydictionary):
    print(type(mydictionary))
    for k,v in mydictionary.items():
        print(k,v)
    

myfunctionWithDictionaryInput()

myfunctionWithDictionaryInput(startValue=1,endvalue=45,hasACar=True,canSing=False,price=123.56)

def setConfiguration(startValue,endvalue,**optionalConfigurationProperties):
    for i in range(startValue,endvalue):
        print(i)
    print(optionalConfigurationProperties)

setConfiguration(1,5,logLevel='verbose')

print()

setConfiguration(1,3)
setConfiguration

# Labs:
# Exercise: 3.2 Temperatures
# Exercise  3.1 Create a function that grabs 10 numbers...
# 3.3
# 3.4
# 3.6

def sumfunction(number1,number2):
    return number1 + number2

############################################################
# 
############################################################

def isLeapYear(year : int) -> bool:
    if (year%4 == 0 and year%100!=0) or year%400==0 :
        return True    
    else:
        return False


isLeapYear(2025)

########################################################
# we will discuss scope now
########################################################
















 
    