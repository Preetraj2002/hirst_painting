import colorgram
from turtle import Turtle,Screen
import random

colors=colorgram.extract("image.jpg",30)
colors_rgb=[]
for i in colors :
    color_tuples=(i.rgb[0],i.rgb[1],i.rgb[2])

    colors_rgb.append(color_tuples)
print(colors_rgb)

screen=Screen()
screen.colormode(255)

tim=Turtle()
tim.pensize(1)
#
#

# colors_rgb=[(220, 158, 84), (39, 109, 150), (120, 163, 191), (150, 63, 87), (217, 232, 222), (203, 134, 157), (180, 160, 34), (32, 131, 95), (122, 179, 152), (235, 218, 225), (161, 79, 52), (213, 87, 61), (197, 85, 112), (208, 223, 231), (229, 199, 114), (57, 166, 135), (141, 33, 42), (8, 104, 80), (47, 158, 182), (234, 163, 181), (117, 115, 162), (32, 62, 111), (236, 171, 157), (126, 38, 34), (156, 210, 197), (32, 57, 78), (70, 41, 37), (25, 65, 56), (74, 37, 47)]
tim.penup()
tim.setx(-250)
tim.sety(-250)

for j in range(10):
     for i in range(10):
          tim.color(random.choice(colors_rgb))
          tim.fd(50)
          tim.dot(20)

     tim.backward(50*10)
     tim.left(90)
     tim.forward(50)
     tim.right(90)





screen.exitonclick()