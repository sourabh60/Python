from turtle import Turtle, Screen
import random
import turtle
race_is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")

colours = ['red','yellow','green','blue','purple']
y_positions = [0,70,140,-140,-70]
all_turtles = []

for i in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[i])
    all_turtles.append(new_turtle)
 
if user_bet:
    race_is_on = True

while race_is_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")


        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)




screen.exitonclick()

