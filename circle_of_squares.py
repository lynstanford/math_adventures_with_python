from turtle import *
import turtle as t
shape('turtle')
speed(9)
def square():
    for i in range(4):
        t.color('white')
        t.bgcolor('turquoise')
        t.forward(150)
        t.right(90)
square()

for i in range(60):
    square()
    t.right(6)

done()

   
   
    