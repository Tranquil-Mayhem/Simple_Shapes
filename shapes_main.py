import turtle
from IllusionHelper import *


hasDrawn = False # tells the program if the shapes have been drawn

# draw function - draws the shapes
def draw():
    global hasDrawn     # this is a global variable so it can be accessed later

    if not hasDrawn:    # if the shapes haven't been drawn, draw them
        drawLine(turtle, -50, -50, 50, 50)  

        drawCircle(turtle, 150, -50, 50, "blue")

        drawSquare(turtle, -200, -50, 100, "red")

        drawRectangle(turtle, -50, -200, 250, 100, "green")

        drawTriangle(turtle, -200, -200, 100, "orange")

        drawDiamond(turtle, 150, 100, 100, "purple")

        drawEllipse(turtle, -75, 175, 50, 50, "pink")

        hasDrawn = True   # changes the global variable, indicates the shapes have been drawn
        
    else:
        turtle.penup() 
        turtle.goto(0, 0) # places the pen in the center

while True:
    try:  
        draw() # this keeps the application "drawing" until the user exits the program otherwise it will end immediately
    except turtle.Terminator: # catches the exception if the user clicks the X button on the application
        print("Goodbye")
        break # ends the program
   