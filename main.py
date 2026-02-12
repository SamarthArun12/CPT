import turtle as trtl
import random as rand
import time

colors = ["dark red", "dark blue", "dark green", "dark orange", "purple"]

wn = trtl.Screen()
wn.screensize(400,400)

total_time = 0
turtles_clicked = 0

def spawnTurtle():
    new_turtle = trtl.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.shape("circle")
    new_turtle.shapesize(5)
    selected_color = colors[rand.randint(0,len(colors)-1)]
    new_turtle.color(selected_color)
    new_turtle.speed(0)
    xpos = rand.randint(-300, 300)
    ypos = rand.randint(-250,250)
    new_turtle.goto(xpos, ypos)
    new_turtle.showturtle()
    return new_turtle

#need to use a function inside onclick()
def change_clicked():
    clicked = not clicked

while True:
    current_turtle = spawnTurtle()
    clicked = False
    start_time = time.time
    while not clicked:
        current_turtle.onclick(change_clicked())
    end_time = time.time
    elapsed_time = end_time - start_time
    print(elapsed_time)
    total_time += elapsed_time
    turtles_clicked += 1
    average = total_time/turtles_clicked
    print(average)

