# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:43:15 2020

@author: lynst
"""

from turtle import *
from random import *

t1, t2, t3, t4, t5 = Turtle(), Turtle(), Turtle(), Turtle(), Turtle()       # create turtle objects

x = -200
turtles = [t1,t2,t3,t4,t5]
for t in turtles:
    t.speed(100)
    t.left(90)
    t.color('brown')
    t.pu()
    x += randint(80,160)
    t.goto(x, randint(-100,100))
    t.pd()

speed(100)
left(90)

def branch(turt, branch_len):
    angle = randint(22,30)
    sf = uniform(0.6,0.8)                                                   # Shrink Factor
    size = int(branch_len / 10)
    turt.pensize(size)
    if branch_len > 10:
      turt.forward(branch_len)
      turt.left(angle)
      branch(turt, branch_len*sf)                                           # sf replaces 0.7
      turt.right(angle*2)
      branch(turt, branch_len*sf)                                           # sf replaces 0.7
      turt.left(angle)
      turt.backward(branch_len)

for t in turtles:
    branch(t,100)

branch(100)
t.done()
