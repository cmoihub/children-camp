import turtle
import random

y = 100

# setup cmoi
cmoi = turtle.Turtle()
cmoi.color("red")
cmoi.shape("turtle")
cmoi.penup()
cmoi.goto(-200, 100)

# setup mitch
mitch = cmoi.clone()
mitch.shape("square")
mitch.color("red")
mitch.penup()
mitch.goto(-200, -100)

# make a circle with cmoi
cmoi.goto(300, 60)
cmoi.pendown()
cmoi.circle(40)

# go back to cmoi's original position
cmoi.penup()
cmoi.goto(-200, 100)

# make a circle with mitch
mitch.goto(300, -140)
mitch.pendown()
mitch.circle(40)

# go back to mitch's original position
mitch.penup()
mitch.goto(-200, -100)

die = [1, 2, 3, 4, 5, 6]
for i in range(20):
    if cmoi.pos() >= (300, 100):
        print("CMOI wins!")
        break
    elif mitch.pos() >= (300, -100):
        print("Mitch wins!")
        break
    else:
        # cmoi goes forward
        player_turn = input("Press 'Enter' to roll player's die")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of the steps will be: ")
        print(20 * die_outcome)
        cmoi.fd(20 * die_outcome)

        # mitch goes forward
        player_turn = input("Press 'Enter' to roll player's die")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of the steps will be: ")
        print(20 * die_outcome)
        mitch.fd(20 * die_outcome)
