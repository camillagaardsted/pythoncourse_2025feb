# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 13:49:58 2024

@author: admin
"""
import math 
import shape
class Circle(shape.Shape):
    
    def __init__(self,radius,x,y, linecolor=1, linewidth=10):
        # super means my parent class here
        super().__init__(linecolor,linewidth)
        self.x=x
        self.y=y
        self.radius=radius
        
        
    def getArea(self):
        return self.radius**2 *math.pi
    