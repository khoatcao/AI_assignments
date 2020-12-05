import pandas as pd
import numpy as np
import math
import cv2 as cv
from queue import PriorityQueue

# I am going to create a class to hold out peak of and present distance formula in betwen two points in the space S and G
class peak(object) : # peak for s and g and delare polygon 
    ## declare constructor
    def __init__(self,x,y, th_poly) :
        self.peak = [x,y] # 
        self.th_poly = th_poly 
    # compute distance from A to B in coordinate plane     
    def distance(self,p2) :
        x1,y1 = self.peak[0],self.peak[1]
        x2,y2 = p2.peak[0],p2.peak[1]

        return math.sqrt((x1-x2)**2+(y1-y2)**2)

    def __eq__(self,value) : 
        return self.peak == value.peak 
    
    def __str__(self) : # a clear description about something
        ##  %d for number
        ## %s for string
        x,y,th = self.peak[0], self.peak[1],self.th_poly
        if th_poly == None : 
            return '%d,%d'%(x,y)
        
        return '%d,%d,polygon : %s' %(x,y,str(th_poly))

