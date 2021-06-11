from turtle import Turtle, Screen
import random

tim = Turtle()
colours = ["CornflowerBlue","DarkOrchid", "IndianRed"]
def draw_shape(num_sides):
    angle = 360/ num_sides
    for  i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for sh in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(sh)

screen = Screen
screen.exitonclick()
