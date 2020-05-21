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

if answer:
    turtle.bgcolor('black')
    turtle.color('red')

    for repetition in range(60):  # unused variable
        square()
        turtle.right(6)

turtle.hideturtle()
turtle.done()
