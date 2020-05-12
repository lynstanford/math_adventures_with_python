#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lynst
#
# Created:     12-05-2020
# Copyright:   (c) lynst 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from turtle import *
from random import *

t1 = Turtle()                                           # create turtle objects
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()

x = -400
y = -400
turtles = [t1,t2,t3,t4,t5]
for t in turtles:
    t.speed(100)
    t.left(90)
    t.color('turquoise')
    t.bg('orange')
    t.pu()
    x += randint(80,160)
    y += randint(45,170)
    t.goto(x, randint(-100,100))
    t.goto(y, randint(-100,20))
    t.pd()


def branch(turt, branch_len):
    angle = randint(20,35)
    sf = uniform(0.6,0.8)                               # Shrink Factor
    size = int(branch_len /10)
    turt.pensize(size)
    if branch_len < 20:
        turt.color('darkturquoise')
        turt.stamp()
        turt.color('aqua')
    if branch_len > 10:
        turt.forward(branch_len)
        turt.left(angle)
        branch(turt, branch_len*sf)                     # sf replaces 0.7
        turt.right(angle*2)
        branch(turt, branch_len*sf)                     # sf replaces 0.7
        turt.left(angle)
        turt.backward(branch_len)

for t in turtles:
    branch(t,80)