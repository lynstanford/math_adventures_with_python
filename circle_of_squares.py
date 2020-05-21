from turtle import *
import turtle as t

shape('turtle')
speed(15)

# First you need to define a loop function to draw a square
def square():
    for i in range(4):
        t.color('red')
        t.bgcolor('black')
        t.forward(150)
        t.right(90)

# Ask the user for input if they wish to see the Turtle move
question = input("Do you wish to see my animation? y/n: ")
answer = bool(question)
y = True
n = False
if answer == y: 
    answer = True
    
    for i in range(60):
        square()
        t.right(6)
        
else: 
    answer = False
    t.clear()
done()   

  




   
   
    
