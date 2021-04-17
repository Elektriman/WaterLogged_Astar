# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 12:11:20 2021
Edited on Mon Apr 5 14:39:45 2021 by Julien
Edited on Mon Apr 12 10:12:25 2021 by Julien

@author: Julien
"""

def type_verif(var, *types):
    for t in types :
        if type(var)==t :
            return True
    return False

class Cell :
    """
    this class is a cell from an Astar algorithm
    one particularity is that it contains a vector because the algorithm will be done in a non-isotropic environment
    """
    
    def __init__(self, x_coord, y_coord, x_comp, y_comp, d_to_first, d_to_end, parent=None):
        """
        The cell class can store coordinates and vector components for a 2-d space
        It also stores the heuristic parameters and the parent cell in order to perform the Astar algorithm

        Parameters
        ----------
        x_coord : int or float
            The x coordinate of the cell.
        y_coord : int or float
            The y coordinate of the cell.
        x_comp : int or float
            The x component of the fluid vector.
        y_comp : int or float
            The y component of the fluid vector.
        d_to_first : int or float
            The distance to the first cell. Must be positive. 
        d_to_end : int or float
            The distance to the last cell. Must be positive..
        parent : Cell or None, optional
            The parent cell. Default value is None but only the first cell should have None parent.

        Raises
        ------
        TypeError
            If types of parameters are not matched.
        ValueError
            If heuristic parameters are set to negative values.
        """
        
        #checking the type of the data given in the cells
        
        try :
            # coordinates must be ints or floats
            if type_verif(x_coord, int, float) and type_verif(y_coord, int, float):
                
                #define the coordinates of the cell
                self.x = x_coord
                self.y = y_coord
            
            else :
                raise TypeError('x and y coordinates must be integers or floats')
        
        except Exception as e :
            raise e
        
        try :
            # vectors must be ints or floats
            if type_verif(x_comp, int, float) and type_verif(y_comp, int, float):
                #define the fluid flow vector using its 2d-componants
                self.vx = x_comp
                self.vy = y_comp
            else :
                raise TypeError('Fluid Vector components must be integers or floats')
        
        except Exception as e :
            raise e
        
        try :
            #heuristic params must be ints or floats
            if type_verif(d_to_first, int, float) and type_verif(d_to_end, int, float) :
                
                #heuristic params must be positive as they are distances
                #we do this check after to avoid comparing a string or a complex to 0
                if d_to_first >= 0 and d_to_end >= 0 :
                    #define its heuristic parameters
                    self.dtf = d_to_first #distance to the starting cell
                    self.dte = d_to_end #distance to the finish cell
                    self.h = d_to_first + d_to_end #heuristic weight
                else :
                    raise ValueError('heuristic parameters must be positive')
            else :
                raise TypeError('heuristic parameters must be integers or floats')
            
        except Exception as e :
            raise e
        
        try :
            #the parent cell must be a cell but the starting has no parent so we allow the None value
            if type_verif(parent, Cell, type(None)) :
                self.parent=parent
            else :
                raise TypeError('parent must be a Cell (or None if it is the starting cell)')
        except Exception as e :
            raise e
    
    #GETTERS for different parameters of the cell
    def getCoords(self):
        """
        getter for the the coordinates

        Returns
        -------
        tuple (x,y)
        """
        return((self.x,self.y))

    def getV(self):
        """
        getter for the vector

        Returns
        -------
        tuple (vx,vy)
        """
        return((self.vx,self.vy))
    
    #heursitic values are often named with f,g and h respectively for the distances to origin, to end, and the sum of the two.
    def getF(self):
        """
        getter for the distance to the first cell

        Returns
        -------
        int or float
            distance to the first cell
        """
        return self.dtf
    
    def getG(self):
        """
        getter for the distance to the end cell

        Returns
        -------
        int or float
            distance to the end cell
        """
        return self.dte
    
    def getH(self):
        """
        getter for the sum of the distances to the first and to the last cell

        Returns
        -------
        int or float
            distance to the first cell + distance to the last cell
        """
        return self.h
    
    def getParent(self):
        """
        getter for the parent cell

        Returns
        -------
        Cell or None
            parent cell. None returned only in the case of this method performed onto the first cell
        """
        return self.parent

    #no SETTERS as a Cell should not be altered after creation
