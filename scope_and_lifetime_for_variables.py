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

# break until 14.42

##################################################
# 
##################################################

# break and continue

# errorhandling
# reading and writing to a file
# exercises 

# break and continue usefull inside loops!
    # Can we make a function to collect a dynamic number of ints?

numberlist = []
while True:
    number = int(input('Please type an integer between 1 and 50. Type 0 to finish:'))
    if number == 0:
        break # jumps out of the while loop
    numberlist.append(number)

print('Now the loop has finished!')

def getNumbers():
    numberlist = []
    while True:
        number = int(input('Please type an integer between 1 and 50. Type 0 to finish:'))
        if number == 0:
            break # jumps out of the while loop
        numberlist.append(number)
    return numberlist

# continue is a bit more nice - it only skips and jumps to the top and checks the condition again

gender = ''
numberOfBeers=0
while numberOfBeers==0:
    gender = input('Please type gender M for male and F for female:')
    if not gender.upper() in ['M','F']:
        continue # will jump to the top, but execute again if the condition is still true
    numberOfBeers = int(input('number of beers:'))

for i in range(10):    
    if i == 5:
        continue # we skip number 5
    print(i)
    
# errorhandling
# best practise is to be proactive in your scripts
# 


number1=34
# if they type af float or a string this can go wrong:
number2 = int(input('Please enter an integer:'))
# division by zero will raise an error here
result = number1/number2


# we use a try-except to catch any erros 
try:
    number1=34
    number2 = int(input('Please enter an integer as number2:'))
    result = number1/number2
    print(result)
    
except ValueError:
    print('number2 should be an integer!')
except ZeroDivisionError as e:
    errorInfo= e
    print('number2 cannot be 0',e)
except:
    print('Something wrong happened')    
finally:
    print('is always executed at the end no matter whether the try block failed or not')
    
###############################################################
# We want to read and write data
###############################################################

# we want to write some text lines to a file
filename=r'C:\PythonCourse225\ourfirstfile.txt'
myfile = open(filename,'w',encoding='utf-8')
myfile.write('This is the first line in our file\n')
myfile.write('This is the second line\n')
myfile.write('and finally the last one! Æ,Ø and Å often give problems')
myfile.close()

myfile.closed

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

filename=r'C:\PythonCourse225\poem.txt'
# with makes sure the file is close after this block
with open(filename,'w',encoding='utf-8') as myfile:
    myfile.write(pythonpoem)

myfile.closed

# how do we READ data from a file?
filename=r'C:\PythonCourse225\poem.txt'
with open(filename,'r',encoding='utf-8') as myfile:
    content=myfile.read()

filename=r'C:\PythonCourse225\poem.txt'
with open(filename,'r',encoding='utf-8') as myfile:
    content=myfile.readline()

print(content)

filename=r'C:\PythonCourse225\poem.txt'
with open(filename,'r',encoding='utf-8') as myfile:
    content=myfile.readlines()
# WRITING
filename=r'C:\PythonCourse225\poem.txt'
# with makes sure the file is close after this block
with open(filename,'w',encoding='utf-8') as myfile:
    myfile.write(pythonpoem)

# Try exercises with files


