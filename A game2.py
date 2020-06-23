import turtle
import time
import random

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
head.direction = "stop"


#Snake Food
food = turtle.Turtle()
food.speed(0) #animation speed of the turtle module
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


#Functions
def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
#Keyboard Bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

#Main game loop
while True:
    wn.update()

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
    move()

    time.sleep(delay)

wn.mainloop()
