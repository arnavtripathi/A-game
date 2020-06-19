import turtle
import time

delay = 0.1

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # turns off the screen updates

#Snake Head
head = turtle.Turtle()
head.speed(0) #animation speed of the turtle module
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "up"

#Functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)




#Main game loop
while True:
    wn.update()

    move()

    time.sleep(delay)

wn.mainloop()
