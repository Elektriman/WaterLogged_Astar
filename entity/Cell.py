# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 12:11:20 2021

@author: Julien
"""

import numpy as np

class Cell :
    """
    this class is used in a 2d-array which contains fluid velocity vectors
    An A* algorithm will be done on this array
    """
    def __init__(self, x_coord, y_coord, x_comp, y_comp, d_to_first, d_to_end, parent):
        
         #checking the type of the data given in the cells
        
        try :
            if (type(x_coord),type(y_coord)) == (int,int) :
                
                if x_coord >= 0and y_coord >= 0 :
                    #define the coordinates of the cell
                    self.x = x_coord
                    self.y = y_coord
                else :
                    raise ValueError('x and y coordinates must be positive')
            
            else :
                raise TypeError('x and y coordinates must be integers')
        
        except Exception as e :
            raise
        
        try :
            if (type(x_comp),type(y_comp),type(d_to_first),type(d_to_end)) == (float,float,float,float) :
                #define the fluid flow vector using its 2d-componants
                self.vx = x_comp
                self.vy = y_comp
                
                if d_to_first >= 0 and d_to_end >= 0 :
                    #define its heuristic parameters
                    self.dtf = d_to_first #distance to the starting cell
                    self.dte = d_to_end #distance to the finish cell
                    self.h = d_to_first + d_to_end #heuristic weight
                else :
                    raise ValueError('heuristic parameters must be positive')
                
            elif (type(x_comp),type(y_comp))!=(float,float) :
                raise TypeError('fluid vector components must be floats')
            
            else :
                raise TypeError('heuristic parameters must be floats')
        
        except Exception as e :
            raise
    
    #gives a tuple of the coordinates
    def getCoords(self):
        return((self.x,self.y))
    
    #gives a tuple of the flow vector
    def getV(self):
        return((self.vx,self.vy))
    
    #gives the coordinates of the neighbouring cells
    def getNb(self):
        N = np.empty((3,3), dtype=tuple)
        for i in range(-1,2):
            for j in range(-1,2):
                if not (i==0 and j==0) : #avoid adding the cell itself
                    N[i+1,j+1] = (self.x+i, self.y+j)
        return(N.ravel()[N.ravel()!=None])