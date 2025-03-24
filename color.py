from turtle import *
from colorsys import*
speed(0)

bgcolor("black")
h=0

for i in range(75):
    color(hsv_to_rgb(h,1,1))
    h += 0.014
    left(1)

    forward(1)

    for j in range(2):
        left(2)
        circle(140)
    hideturtle()
done()