# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 13:53:26 2024

@author: admin
"""

# main program 

# we defined two classes: Circle and Rectangle and they inherit from Shape

import circle
import rectangle

c1=circle.Circle(10, 45, 66)
c2=circle.Circle(15, 45, 66)

print("counter",rectangle.Rectangle.rectangleCounter)

print('area c1',c1.getArea())
print('area c2',c2.getArea())

r1 = rectangle.Rectangle(100,2000,0, 0,10,45)
print("counter",rectangle.Rectangle.rectangleCounter)
r2 = rectangle.Rectangle(10,2000,0, 0,10,45)
print("counter",rectangle.Rectangle.rectangleCounter)
# destroy or delete the variable called r2
del r2

print("counter",rectangle.Rectangle.rectangleCounter)
print(r1.linecolor,r1.linewidth, r1.fillcolor)

print(r1.getGradientColorFactor())