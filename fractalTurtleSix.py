#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     Supposed to be Japanese Cherry Trees
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

x = -100
y = -100

turtles = [t1,t2,t3]
for t in turtles:
    t.speed('fastest')
    t.left(90)
    t.screen.bgcolor('black')
    t.color('brown')
    t.pu()
    x += randint(10,1000)
    y += randint(5,70)
    t.goto(x, randint(-100,100))
    t.goto(y, randint(-100,0))
    t.pd()

def branch(turt, branch_len):
    angle = randint(20,35)
    sf = uniform(0.6,0.8)                               # Shrink Factor
    size = int(branch_len /10)
    turt.pensize(size)
    if branch_len < 30: 
        turt.color('white')
        turt.stamp()
        turt.color('brown')
    if branch_len < 20:
        turt.color('lightpink')
        turt.stamp()
        turt.color('brown')
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
    