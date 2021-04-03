# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 13:17:20 2021

@author: Julien
"""

from Cell import Cell
import inspect
import sys
import os
import numpy as np

def unit_test(class_t, expected):
    """
    this function tries different inputs types into the class_t arguments and verifies the output using exeptions
    
    inputs :
        class_t : the class you want to test
        expected : the array of success that should be encountered
    """
    
    #define different entries to test out
    entries = {"int" : 1,
               "negative int":-1,
               "float" : 1.0,
               "negative float" : -1.0,
               "complex" : 1+1j,
               "string" : "string",
               "null" : None}
    
    param = list(inspect.signature(Cell.__init__).parameters.keys())
    param.pop(0)
    
    min_valid = True #a boolean that keeps track of the minimal validation
    success = np.full((len(param),len(param)), False) #the list of the tests passed or not
    
    with open(f'log_for_{os.path.basename(__file__)[:-3]}.txt', 'w') as f : #open a log file
        for i in range(len(expected[0])): #iterate over the arguments
            f.write(5*'-'+f'parameter {param[i]}'+5*'-'+'\n')
            j=0
            for entry_t, entry in entries.items() : #iterate over the entries
                default = [expected[0][i]() for i in range(len(expected[0]))]
                try :
                    default[i] = entry
                    c = class_t(*tuple(default))
                except Exception as e :
                    f.write(f'{entry_t} typed entry has raised the following exeption :\n{type(e).__name__} : '+str(e)+'\n\n')
                    if type(entry)==type(expected[i]) :
                        min_valid = False
                        sys.stdout.write(f'argument "{param[i]}" has failed the minimal requirement\n')
                else :
                    success[i,j] = True
                    f.write(f'{entry_t} typed entry has raised no exeption\n\n')
                finally :
                    j+=1
    
    if min_valid :
        sys.stdout.write('the function has fulfilled the minimal validation needs\n')
    
    for i in range(len(expected[0])):
        if success[i].all() == np.full(len(param), True).all() :
            sys.stdout.write(f'Warning : the parameter "{param[i]}" has not been restrained\n')


if __name__ == '__main__' :
    c1 = Cell(5, 3, 1.0, 1.0, 10.0, 15.0, None)
    print(c1)
    print(c1.getCoords())
    print(c1.getV())
    print(c1.getNb())
    
    expected = [[int, int, float, float, complex, str, Cell],
                [True, False, False, False, False, False, False],
                [True, False, False, False, False, False, False],
                [False, False, True, True, False, False, False],
                [False, False, True, True, False, False, False],
                [False, False, True, False, False, False, False],
                [False, False, True, False, False, False, False],
                [False, False, True, False, False, False, False]]
    
    unit_test(Cell, expected)















