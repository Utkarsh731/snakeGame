import turtle
import time
import random

def move():
    if snake_head.direction=="up":
        y=snake_head.ycor()
        snake_head.sety(y+20)
    if snake_head.direction=="down":
        y=snake_head.ycor()
        snake_head.sety(y-20)
    if snake_head.direction=="right":
        x=snake_head.xcor()
        snake_head.setx(x+20)
    if snake_head.direction=="left":
        x=snake_head.xcor()
        snake_head.setx(x-20)

window=turtle.Screen()
segments=[]
score=0
high_score=0
delay=0.1
pen=turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color("white")
pen.shape("square")
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score: 0",align="center",font=("Courier",24,"normal"))

def go_up():
    if snake_head.direction!="down":
        snake_head.direction="up"
def go_down():
    if snake_head.direction != "up":
        snake_head.direction="down"
def go_left():
    if snake_head.direction != "right":
        snake_head.direction="left"
def go_right():
    if snake_head.direction != "left":
        snake_head.direction="right"
window.listen()
window.onkeypress(go_up,"w")
window.onkeypress(go_down,"s")
window.onkeypress(go_left,"a")
window.onkeypress(go_right,"d")

window.title("Snake it")
window.bgcolor("green")
window.setup(600,600)
window.tracer(0)

snake_head=turtle.Turtle()
snake_head.speed(0)
snake_head.shape("circle")
snake_head.color("maroon")
snake_head.penup()
snake_head.goto(0,0)
snake_head.direction="stop"

snake_food=turtle.Turtle()
snake_food.speed(0)
snake_food.shape("circle")
snake_food.color("blue")
snake_food.penup()
snake_food.goto(0,100)


while True:
    window.update()
    if snake_head.xcor()>290 or snake_head.xcor()<-290 or snake_head.ycor()<-290 or snake_head.ycor()>290:
        time.sleep(1)
        snake_head.goto(0,0)
        snake_head.direction="Stop"
        for i in segments:
            i.goto(1000,1000)
        segments.clear()
        score=0
        delay=0.1
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    if snake_head.distance(snake_food)<20:
        x = random.randint(-290,290)
        y = random.randint(-290, 290)
        snake_food.goto(x,y)
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)
        score+=10
        delay-=.01
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))
    for i in range(len(segments)-1,0,-1):
        x=segments[i-1].xcor()
        y=segments[i-1].ycor()
        segments[i].goto(x,y)
    if len(segments)>0:
        x=snake_head.xcor()
        y=snake_head.ycor()
        segments[0].goto(x,y)
    move()
    for segment in segments:
        if segment.distance(snake_head)<20:
            time.sleep(1)
            snake_head.goto(0,0)
            snake_head.direction="stop"
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay=0.1
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",font=("Courier", 24, "normal"))

    time.sleep(delay)
window.mainloop()
