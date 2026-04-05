# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:21:49 2019

@author: Yvonne
"""

def some_function(x):
    return["hello", x* 2]        
result = some_function(5) 


li = []
def some_function(x):
    li.appen(1)
result = some_function(li)


counter =[0]
def some_function(x):
    counter[0] = counter[0] + 1
    return "hello"


counter = [0]
class SomeCalss(object):
    def _init_(self):
        self.counter = 0
    def some_funcfion (self, x):
        self.counter += 1
        return "hello"
    
#if x: is the same as if x == [] or 