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

# create a class of n polygons
class polygon(object) :
    
    def __init__(self, num_peaks, list_peaks) : 
        self.num_polygons = num_polygons
        self.list_peaks = list_peaks

## drawing polygon with Opencv  
def draw_poly(image,name,list_peaks):
     # parameters needed
     # in order to draw polygon I need coordinates of vertices
     # make those points into an array of shape rows*1*1 where rows are number of vertices and it should be type int32.
     # lets draw polygon from
     # link to document https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html
     pts = np.array(list_peaks,np.int32)
     pts = pts.reshape((-1*1*2)) # reshape array if it has one single vector
     image = cv.polylines(image,[pts],True,(0,255,255)
     # create p point under my consider
     p = (list_speaks[-1][0],listpeaks[-1][2])
     # draw string on image
     org = (50,50)
     font = cv2.FONT_HERSHEY_SIMPLEX
     fontscale = 1
     #blue color 
     color = (255,0,0)
     # tine thickness of 2 px
     thickness = 2
     cv2.puttext(image,"name",org,color,fornt,fontscale,p,thickness)
     
     return image
     
    