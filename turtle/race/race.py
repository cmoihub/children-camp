import turtle
import random

x = 200
y = 100

cmoi = turtle.Turtle()
cmoi.color("red")
cmoi.shape("turtle")
cmoi.penup()
cmoi.goto(-x, y)

mitch = cmoi.clone()
mitch.shape("square")
mitch.color("red")
mitch.penup()
mitch.goto(-x, -y)

cmoi.goto(300, 60)
cmoi.pendown()
cmoi.circle(40)
cmoi.penup()
cmoi.goto(-x, y)

mitch.goto(300, -140)
mitch.pendown()
mitch.circle(40)
mitch.penup()
mitch.goto(-x, -y)

die = [1, 2, 3, 4, 5, 6]
for i in range(20):
    if cmoi.pos() >= (300, 100):
        print("CMOI wins!")
        break
    elif mitch.pos() >= (300, -100):
        print("Mitch wins!")
        break
    else:
        player_turn = input("Press 'Enter' to roll player's die")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of the steps will be: ")
        print(20 * die_outcome)
        cmoi.fd(20 * die_outcome)

        player_turn = input("Press 'Enter' to roll player's die")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of the steps will be: ")
        print(20 * die_outcome)
        mitch.fd(20 * die_outcome)
