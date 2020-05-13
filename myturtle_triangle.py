from turtle import *
import turtle as t

def triangle(sidelength=100):
    for i in range(3):  
        t.forward(sidelength)
        t.right(120)
        
triangle()
