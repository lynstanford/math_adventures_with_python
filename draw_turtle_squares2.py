
from turtle import *
import turtle

# First you need to define a loop function to draw a square


def square():
    for side in range(4):  # unused variable
        turtle.forward(150)
        turtle.right(90)


# Ask the user for input if they wish to see the Turtle move
question = input("Do you wish to see my animation? y/n: ")
answer = question.lower() in ('y', 'yes')

turtle.shape('turtle')
turtle.speed('fastest')


# Using if statement to execute statements based on a condition
if answer:
    
# And next the 'for' loops
    for repetition in range(60):  # unused variable
        turtle.bgcolor('black')
        turtle.color('red')
        square()
        turtle.right(6)
        
    for repitition in range(60): 
        turtle.right(8)
        turtle.color('orange')
        turtle.forward(250)
        square()
        turtle.right(90)
        turtle.right(6)
                
    for repitition in range(60): 
        turtle.right(1)
        turtle.color('lime')
        turtle.forward(350)
        square()
        turtle.forward(30)
        turtle.right(90)
        turtle.right(6)
        
    
         

turtle.hideturtle()
turtle.done()
