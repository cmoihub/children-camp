#!/bin/python3

from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

# setup the race
for step in range(15):
    # label positions
    write(step, align="center")
    right(90)
    # draw lines
    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)


def create_turtle(color):
    turtle = Turtle()
    turtle.color(color)
    turtle.shape("turtle")
    return turtle


def position_turtle(turtle, y):
    turtle.penup()
    turtle.goto(-160, y)
    turtle.pendown()


def rotate_turtle(turtle, turns, right):
    for turn in range(turns):
        turtle.right(right)


# setup asael
asael = create_turtle("red")
position_turtle(asael, 100)
rotate_turtle(asael, 10, 36)

# setup anslem
anslem = create_turtle("blue")
position_turtle(anslem, 70)
rotate_turtle(anslem, 72, 5)

# create ore
ore = create_turtle("green")
position_turtle(ore, 40)
rotate_turtle(ore, 60, 6)

# create nissi
nissi = create_turtle("orange")
position_turtle(nissi, 10)
rotate_turtle(nissi, 30, 12)

turtles = [asael, anslem, ore, nissi]

# run the race
for turn in range(100):
    for turtle in turtles:
        turtle.forward(randint(1, 5))

