import turtle
import time

#CONSTANTS
delay_game = 0.1

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

while True:
    window.update()
    movSnake()
    
    time.sleep(delay_game)