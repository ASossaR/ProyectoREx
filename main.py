import turtle
import time
import random

#CONSTANTS
delay_game = 0.15
tails = []

#Window config
window = turtle.Screen()
window.title("Snake")
window.bgcolor("black")
window.setup(width = 600, height = 600)
window.tracer(0)

#Objects
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)

apple = turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(0,100)

#Variables's Snake
head.direction = "stop"
head_speed = 20


#Functions
def Up(): 
    head.direction = "Up"
def Down(): 
    head.direction = "Down"
def Left(): 
    head.direction = "Left"
def Right(): 
    head.direction = "Right"
def Exit_game(): 
    turtle.bye()


def eat():
    if head.distance(apple) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        apple.goto(x,y)
        tail()
        
def tail():
    snaketail = turtle.Turtle()
    snaketail.speed(0)
    snaketail.shape("square")
    snaketail.color("grey")
    snaketail.penup()
    tails.append(snaketail)
    
def movtail():    
    totaltails = len(tails)
    for index in range(totaltails -1, 0, -1):
        x = tails[index - 1].xcor()
        y = tails[index - 1].ycor()
        tails[index].goto(x,y)
    
    if totaltails > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x,y) 


def movSnake():
    if head.direction == "Up": 
        y = head.ycor()
        head.sety(y + head_speed)
    if head.direction == "Down": 
        y = head.ycor()
        head.sety(y - head_speed)
    if head.direction == "Left": 
        x = head.xcor()
        head.setx(x - head_speed)
    if head.direction == "Right": 
        x = head.xcor()
        head.setx(x + head_speed)

#Listen keyboard
window.listen()
window.onkeypress(Up, "Up")
window.onkeypress(Down, "Down")
window.onkeypress(Left, "Left")
window.onkeypress(Right, "Right")
window.onkeypress(Right, "Right")
window.onkeypress(Exit_game, "Escape")

while True:
    movSnake()
    eat()
    movtail()
    window.update()
  
    
    time.sleep(delay_game)

turtle. mainloop()