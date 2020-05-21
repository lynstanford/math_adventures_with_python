from turtle import *

# The sidelength property can be re-called each time it's used
def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)
        
square(50)
square(30)
square()

