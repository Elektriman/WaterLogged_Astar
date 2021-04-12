# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 13:17:20 2021
Edited on Mon Apr 5 14:45:12 2021 by Julien

@author: Julien
"""

from Cell import Cell
import unittest

def tuple_for_testing(model, val, replace_i):
    """this function creates a tuple by changing only one parameter from a list
    
    Positionnal arguments :
        model -- a list of valid arguments to pass to the object to test
        val -- the value you want to put in the list
        replace_i -- the index of the value to be replaced
    
    Returns :
        tuple
    """
    m_copy = model.copy()
    m_copy[replace_i]=val
    return tuple(m_copy)

#testing class
class test_Cell_c(unittest.TestCase):
    
    #this is a default input that should not raise Errors
    #We will test every argument of the Cell by modifying this list of arguments before feeding it to the asserRaises method
    default = [1, 1, 1.0, 1.0, 10.0, 15.0, None]
    
    """the process could be iterated over but i prefer not to do so because in general it shouldn't be"""
    
    #♠testing the types of the arguments
    def test_type_xcoord(self):
        arg_n = 0
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, "string", arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, [], arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, (1,), arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, 1+2j, arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, True, arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, None, arg_n))
    
    def test_type_ycoord(self):
        arg_n = 1
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, "string", arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, [], arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, (1,), arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, 1+2j, arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, True, arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, None, arg_n))
    
    def test_type_xcomp(self):
        arg_n = 2
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, "string", arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, [], arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, (1,), arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, 1+2j, arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, True, arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, None, arg_n))
        
    def test_type_ycomp(self):
        arg_n = 3
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, "string", arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, [], arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, (1,), arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, 1+2j, arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, True, arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, None, arg_n))
    
    def test_type_dtofirst(self):
        arg_n = 4
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, "string", arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, [], arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, (1,), arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, 1+2j, arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, True, arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, None, arg_n))
    
    def test_type_dtoend(self):
        arg_n = 5
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, "string", arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, [], arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, (1,), arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, 1+2j, arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, True, arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, None, arg_n))
    
    def test_type_parent(self):
        arg_n = 6
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, 1, arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, 1.0, arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, "string", arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, [], arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, (1,), arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, 1+2j, arg_n))
        self.assertRaises(TypeError, Cell, *tuple_for_testing(self.default, True, arg_n))
    
    #testing the values for the heuristic parameters
    def test_value_dtofirst(self):
        arg_n = 4
        self.assertRaises(ValueError, Cell, *tuple_for_testing(self.default, -1, arg_n))
        self.assertRaises(ValueError, Cell, *tuple_for_testing(self.default, -1.0, arg_n))
    
    def test_value_dtoend(self):
        arg_n = 5
        self.assertRaises(ValueError, Cell, *tuple_for_testing(self.default, -1, arg_n))
        self.assertRaises(ValueError, Cell, *tuple_for_testing(self.default, -1.0, arg_n))

if __name__ == '__main__' :
    c1 = Cell(5, 3, 1.0, 1.0, 10.0, 15.0, None)
    print(c1)
    print(c1.getCoords())
    print(c1.getV())
    print(c1.getF())
    print(c1.getG())
    print(c1.getH())
    print(c1.getParent())
    
    c2 = Cell(3, 5, 1.0, 1.0, 10.0, 12.0, c1)
    print(c2.getParent().getCoords())
