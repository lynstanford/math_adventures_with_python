#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lynst
#
# Created:     21-04-2020
# Copyright:   (c) lynst 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from turtle import *
from random import *

# Declare five new variables

t1, t2, t3, t4, t5 = Turtle(), Turtle(), Turtle(), Turtle(), Turtle()

# Create a new array containing the five variables

turtles = [t1, t2, t3, t4, t5]
x = -200
for t in turtles:
    x += randint(60,160)
    y = randint(-50,50)
    t.speed(100)
    t.left(90)
    t.color('brown')
    t.pu()
    t.goto(x,y)
    t.pd()

def branch(turt, branch_len, angle):
    angle = randint(3,2)
    sf = uniform(0.6,0.8)
    size = branch_len/10
    turt.pensize(size)
    if branch_len < 20:
        turt.color('green')
        turt.stamp()
        turt.color('brown')
    if branch_len > 10:
        turt.forward(branch_len)
        turt.left(angle)
        branch(turt,sf*branch_len,angle)
        turt.left(angle)
        turt.backward(branch_len)

for t in turtles:
    branch(t,100,22)
t.done()
