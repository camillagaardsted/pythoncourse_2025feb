# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 13:52:03 2024

@author: admin
"""

# usually you make a file for each class
import shape
class Rectangle(shape.Shape):
    
    
    # you can have class variables out here
    # what you usually call a static variable
    rectangleCounter=0
    
    # constructor
    def __init__(self,height,width,topleftcornerx,topleftcornery, linecolor=1, linewidth=10):
        # super means my parent class here
        super().__init__(linecolor,linewidth)        
        self.topleftcornery= topleftcornerx
        self.topleftcornery=topleftcornery
        self.height=height
        self.width= width
        Rectangle.rectangleCounter+=1
        
      # destructor
      # clean up nicely here - release any ressources you use 
    def __del__(self):
        Rectangle.rectangleCounter-=1
      

    def getArea(self):
        return self.width*self.height
    
    
    def getGradientColorFactor(self):
        return self.linecolor*0.02*self.height
    
    
    # we call +
    #def __add__