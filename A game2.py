import turtle

screen = turtle.Screen() #create a new screen
screen.setup(700, 700)   # 500 x 500 window
screen.tracer(0)         #tell screen to not show automatically

thebox = turtle.Turtle() #create a turtle
thebox.speed(0)          #make it move faster
thebox.width(3)
thebox.hideturtle()      # hide thebox, we only want the drawing

def draw_square() :      #function that draws one square
    for side in range(4) :
        thebox.forward(50)
        thebox.left(90)

thebox.penup()           #go off the screen on the left
thebox.goto(-550, 0)
thebox.pendown()

while True:              #now do this repeatedly, to animate : 
    thebox.clear()       # - clear all the turtle's previous drawings
    draw_square()        # - draw a square
    screen.update()      #only now show the screen, as one of the frames
    thebox.forward(0.2)  # - move forward a bit
    thebox.color("orange")

#Tip of fireball

tip = turtle.Turtle()
tip.speed(0)          
tip.width(3)
tip.hideturtle()    

def draw_square() :    
    for side in range(4) :
        thebox.forward(50)
        thebox.left(90)

thebox.penup()         
thebox.goto(-550, 0)
thebox.pendown()

while True:             
    thebox.clear()       
    draw_square()       
    screen.update()      
    thebox.forward(0.2)  
    thebox.color("orange")
