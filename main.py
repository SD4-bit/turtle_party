# Turtle  Party Project
# by Sherry Moore
# 04.18.24
import turtle

turtle.color("sea green")

def back(len):
  turtle.pu()           # same as penup()
  turtle.backward(len)
  turtle.pd()           # same as pendown()

#forward helper function
def move(len):
  back(-1 * len)

def polygon(num, size):
   for i in range(num):
     turtle.forward(size)
     turtle.left(360 / num)
     
def spiral(len, angle):
    for i in range(len, 5, -5):
      turtle.forward(i)  # Use the i because it has the value of the 3 parameters
      turtle.left(angle)
      
spiral(75, 45)
move(150)
turtle.color("blue")
spiral(100, 90)
