import turtle
import random

x = 200
y = 100


def create_turtle(color, shape):
    t = turtle.Turtle()
    t.color(color)
    t.shape(shape)
    return t


def go_home(player, x_pos, y_pos):
    player.penup()
    player.goto(x_pos, y_pos)


def make_target(player, target):
    player.goto(300, target)
    player.pendown()
    player.circle(35)


def go_forward(player, name):
    player_turn = input("Press 'Enter' to roll " + name + "'s die")
    die_outcome = random.choice([1, 2, 3, 4, 5, 6])
    print("The result of the die roll is: ")
    print(die_outcome)
    print("The number of the steps will be: ")
    print(20 * die_outcome)
    player.fd(20 * die_outcome)


# setup cmoi
cmoi = create_turtle("red", "turtle")
go_home(cmoi, -x, y)
make_target(cmoi, 60)
go_home(cmoi, -x, y)

# setup mitch
mitch = create_turtle("red", "square")
go_home(mitch, -x, -y)
make_target(mitch, -140)
go_home(mitch, -x, -y)

for i in range(20):
    if cmoi.pos() >= (300, 100):
        print("CMOI wins!")
        break
    elif mitch.pos() >= (300, -100):
        print("Mitch wins!")
        break
    else:
        go_forward(cmoi, "cmoi")
        go_forward(mitch, "mitch")

