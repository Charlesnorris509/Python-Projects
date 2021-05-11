#This is the source code for a ping pong game in python
# using turtle library
# @CharlesNorris 6/05/21

import turtle
import os

wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_A = 0
score_B = 0

#Paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.shapesize(stretch_wid= 5, stretch_len= 1)
paddle_A.penup()
paddle_A.goto(-350, 0)

#Paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.shapesize(stretch_wid = 5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


#Writing Functions
def paddle_a_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)
    
def paddle_a_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)
    
def paddle_b_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)
    
def paddle_b_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)

#Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")    
#While running the loop
while True:
    wn.update()
    
    #Move the ball
    ball.setx(ball.ycor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
        
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
        
    #Moving Left and Right
    if ball.xcor() > 350:
        score_A += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx *= -1
        
    elif ball.xcor() < -350:
        score_B += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        
    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1 
        os.system("afplay bounce.wav&")
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")
    
