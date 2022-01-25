from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()

turtle.shape('arrow')
turtle.speed('fastest')
turtle.shapesize(1)
turtle.pensize(15)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def random_walk(n_points):

    steps = 0

    while steps < n_points:
        turtle.color(random.choice(colours))
        steps += 1
        print("steps:", steps)
        i = random.randint(0,3)
        print("i:", i)
        if i == 0:
            turtle.left(0)
        elif i == 1:
            turtle.left(90)
        elif i == 1:
            turtle.left(180)
        else:
            turtle.left(270)
        turtle.forward(30)

n_points = int(input("How many steps?"      ))
random_walk(n_points)

screen.exitonclick()
