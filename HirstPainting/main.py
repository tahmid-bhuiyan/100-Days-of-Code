import turtle
from random import choice

color_list = [(131, 165, 205), (224, 150, 101), (32, 41, 59), (199, 134, 147), (234, 212, 88), (167, 56, 46), (39, 104, 153), (141, 184, 162), (150, 59, 66), (169, 29, 33), (215, 81, 71), (157, 32, 30), (236, 165, 157), (15, 96, 70), (58, 50, 47), (50, 111, 90), (49, 42, 47), (34, 61, 56), (227, 165, 169), (170, 188, 221), (184, 103, 112), (32, 59, 108), (105, 127, 160), (175, 200, 188), (33, 150, 210), (65, 66, 56)]

t = turtle.Turtle()
turtle.colormode(255)
t.penup()
t.setpos(-300,-250)
starting_posit = t.pos()
t.hideturtle()

def color():
    ran_color = choice(color_list)
    return ran_color
dots = 0
while dots < 10:
    t.dot(size=20)
    t.color(color())
    t.forward(50)
    dots += 1
    if dots == 10:
        dots = 0
        posit = list(starting_posit)
        posit[1] += 50
        t.setpos(posit[0],posit[1])
        starting_posit = t.pos()
turtle.Screen().exitonclick()