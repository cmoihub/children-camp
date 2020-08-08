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

# create ada
ada = Turtle()
ada.color("red")
ada.shape("turtle")

# send ada to where she should be
ada.penup()
ada.goto(-160, 100)
ada.pendown()

# rotate ada
for turn in range(10):
    ada.right(36)

# create bob
bob = Turtle()
bob.color("blue")
bob.shape("turtle")

# send bob to where he should be
bob.penup()
bob.goto(-160, 70)
bob.pendown()

# rotate bob
for turn in range(72):
    bob.left(5)

# create ivy
ivy = Turtle()
ivy.shape("turtle")
ivy.color("green")

# send ivy to where she should be
ivy.penup()
ivy.goto(-160, 40)
ivy.pendown()

# rotate ivy
for turn in range(60):
    ivy.right(6)

# create jim
jim = Turtle()
jim.shape("turtle")
jim.color("orange")

# send jim to where he should be
jim.penup()
jim.goto(-160, 10)
jim.pendown()

# rotate jim
for turn in range(30):
    jim.left(12)

# run the race
for turn in range(100):
    ada.forward(randint(1, 5))
    bob.forward(randint(1, 5))
    ivy.forward(randint(1, 5))
    jim.forward(randint(1, 5))

