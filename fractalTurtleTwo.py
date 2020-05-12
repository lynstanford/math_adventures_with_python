# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 13:31:39 2020

@author: lynst
"""

from turtle import *

speed(100)
left(90)

def branch(branch_len):
    if branch_len > 10:
      angle = 30
      forward(branch_len)
      left(angle)
      branch(branch_len*0.7)
      right(angle*2)
      branch(branch_len*0.7)
      left(angle)
      backward(branch_len)
    
branch(100)
done()
