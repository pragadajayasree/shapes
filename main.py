from turtle import Turtle,Screen
import random
def drawshape(side,angle):
    for i in range(side):
        timmy.forward(100)
        timmy.right(angle)
timmy = Turtle()
"""timmy.shape("turtle")
timmy.color("lavender")
for i in range(4):
  timmy.forward(100)
  timmy.right(90)
for i in range(5):
   timmy.forward(10)
   timmy.penup()
   timmy.forward(10)
   timmy.pendown()"""
colors=["red","blue","pink","orange","violet","green"]
for i in range(3,11):
    timmy.color(random.choice(colors))
    sides = i
    angle = 360/sides
    drawshape(sides,angle)


screen = Screen()
screen.exitonclick()


