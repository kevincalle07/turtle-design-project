#my design
import turtle

turtle.colormode(255)#brings in the colormode function
turtle.bgcolor(230,220,230)

bob = turtle.Turtle()
bob.speed(11)
distance = 100

#using loop variable to change the value of color,distance.
for times in range(10):
    bob.begin_fill()
    bob.color(255,120,100-times)
    bob.forward(50)
    bob.left(45)
    bob.forward(50)
    bob.left(45)
    bob.forward(50)
    bob.left(45)
    bob.forward(50)
    bob.goto(50,45)
    bob.end_fill()
    

#using loop variable to change the value of color,distance.

for times in range(10):
    bob.begin_fill()
    bob.color(0,150,150-times)
    bob.forward(50)
    bob.left(45)
    bob.forward(50)
    bob.left(45)
    bob.forward(50)
    bob.left(45)
    bob.forward(50)
    bob.goto(50,45)
    bob.end_fill()
    
from turtle import *
color('red', 'black')
begin_fill()
while True:
    forward(120)
    left(200)
    if abs(pos()) < 1:
        break
end_fill()
done()


