import turtle
import random
import functions

# s = turtle.getscreen()
x = 200
y = 100


def go_home(player, x_pos, y_pos):
    player.penup()
    player.goto(x_pos, y_pos)


def draw_circle(player, x_return, y_return):
    player.pendown()
    player.circle(40)
    go_home(player, x_return, y_return)


def go_forward(player):
    player_turn = input("Press 'Enter' to roll player's die")
    die_outcome = random.choice(die)
    print("The result of the die roll is: ")
    print(die_outcome)
    print("The number of the steps will be: ")
    print(20 * die_outcome)
    player.fd(20 * die_outcome)


cmoi = turtle.Turtle()
cmoi.color("red")
cmoi.shape("turtle")
go_home(cmoi, -x, y)

mitch = cmoi.clone()
mitch.shape("square")
mitch.color("red")
go_home(mitch, -x, -y)

cmoi.goto(300, 60)
draw_circle(cmoi, -x, y)

mitch.goto(300, -140)
draw_circle(mitch, -x, -y)

die = [1, 2, 3, 4, 5, 6]
for i in range(20):
    if cmoi.pos() >= (300, 100):
        print("CMOI wins!")
        break
    elif mitch.pos() >= (300, -100):
        print("Mitch wins!")
        break
    else:
        go_forward(cmoi)
        go_forward(mitch)


# def funcname(parameter_list):
#     pass
