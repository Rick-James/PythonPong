#Pong
import time
import turtle

window = turtle.Screen()
window.title("Pong - by Ricky Bennett")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#Paddele A
paddle_a = turtle.Turtle()
paddle_a.speed(5)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(1)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=2, stretch_len=2)
ball.penup()
ball.goto(0, 0)


def paddle_a_up() -> None:
    #returns y coordinate
    y = paddle_a.ycor()
    #adds 20 px to y
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    #returns y coordinate
    y = paddle_a.ycor()
    #adds 20 px to y
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    #returns y coordinate
    y = paddle_b.ycor()
    #adds 20 px to y
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    #returns y coordinate
    y = paddle_b.ycor()
    #adds 20 px to y
    y -= 20
    paddle_b.sety(y)


#keyboard binding
window.listen()
window.onkeypress(paddle_a_up(), "w")
window.onkeypress(paddle_a_down(), "s")
window.onkeypress(paddle_b_up(), "Up")
window.onkeypress(paddle_b_down(), "Down")


# Main game loop
while True:
    window.update()



