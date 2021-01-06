import turtle
import random

scr = turtle.Screen()
scr.setup(width=500,height=400)
turtle_color = scr.textinput(title='Make a bet', prompt='Choose the color of the turtle you think will win!')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
first_point = [-230.0, -100.0]
turtlez = []
for i in range(len(colors)):
    t = turtle.Turtle()
    t.penup()
    t.shape('turtle')
    t.color(colors[i])
    t.setpos(first_point[0], first_point[1])
    first_point[1] += 50
    turtlez.append(t)
game = True
while game:
    for player in turtlez:
        player.forward((random.randint(1,10)))
        if player.pos()[0] >= 210:
            win_turtle = player.color()[0]
            if turtle_color.lower() == win_turtle:
                print(f"You won! The {win_turtle} turtle wins!")
            else:
                print(f"You lost! The {win_turtle} turtle wins!")
            game = False
            break


scr.mainloop()