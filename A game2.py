import turtle
import time
import random

delay = 0.1

#Score
score = 0#0 means that that is what u start with in the begining. 
high_score = 0


wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # turns off the screen updates

#Snake Head
head = turtle.Turtle()
head.speed(100) #animation speed of the turtle module
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

segments = []

#Pen
pen =  turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0   High Score: 0", align="center", font=("Courier", 24, "italic"))

#Functions
def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
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

    #Check for collisons with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"


        #Hide the segmens when u lose
        for segment in segments:
            segment.goto(1000, 1000 )

        #Clear the segments list which clears all segments after u lose
        segments.clear()

        #Reset the score when u die
        score = 0
        delay = 0.1

        pen.clear()
        pen.write("Score:{}" "  High Score: {}".format(score, high_score),align="center", font=("Courier", 24, "italic")) 
            
    #Check for collisions with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
    #Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    #Shorten the delay
        delay -= 0.001

    #Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score:{}" "  High Score: {}".format(score, high_score),align="center", font=("Courier", 24, "italic")) 
            
    #Move the end segemnts first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    #Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        
    move()

    #Check for body collisions
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"


            for segment in segments:
                segment.goto(1000, 1000)




         #Clear the segments list which clears all segments after u lose
            segments.clear()

            #Reset the score when u die
            score = 0

            delay = 0.1
            


        #Hide the segments when u lose
            for segment in segments:
                segment.goto(1000, 1000 )

        #Clear the segments list which clears all segments after u lose
            segments.clear()

        
    time.sleep(delay)

wn.mainloop()
