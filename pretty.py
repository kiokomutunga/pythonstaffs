import turtle
import time
import random

screen = turtle.Screen()
screen.bgcolor("black")


writer = turtle.Turtle()
writer.speed(0)
writer.pensize(3)


colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "pink"]

def draw_text():
    writer.penup()
    writer.goto(-150, 0)
    writer.pendown()
    writer.color(random.choice(colors))

    style = ("Arial", 40, "bold")
    writer.write("Pretty Joy", font=style, align="left")
    
    time.sleep(0.3)
    writer.clear()


for _ in range(20):
    draw_text()


turtle.done()
