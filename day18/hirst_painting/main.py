"""import colorgram

rgb_colors=[]
colors=colorgram.extract("100DaysOfPython\day18\hirst_painting\HirstSpotPaintings.jpg",30)
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)"""

from turtle import *
from random import choice 

colormode(255)
tim=Turtle()
tim.penup()
tim.hideturtle()

list_colors=[(246, 243, 238), (247, 243, 245), (207, 162, 102), (241, 246, 242), (237, 240, 244), (151, 76, 43), (222, 200, 137), (50, 92, 126), (173, 148, 39), (140, 38, 20), (131, 161, 186), (199, 94, 71), (50, 120, 94), (66, 49, 41), (12, 94, 69), (144, 174, 145), (159, 145, 159), (29, 65, 78), (17, 82, 90), (231, 177, 162), (102, 78, 79), (53, 47, 50), (181, 202, 173), (45, 65, 84), (97, 142, 130), (11, 75, 57), (111, 127, 148), (70, 63, 55), (178, 192, 209), (109, 136, 142)]

def startPoint():
    tim.left(90)
    tim.forward(255)
    tim.left(90)
    tim.forward(255)
    tim.left(180)

def newLine():
    
    tim.right(90)
    tim.forward(50)
    tim.right(90)
    tim.forward(500)
    tim.right(180)



startPoint()

tim.dot(25,choice(list_colors))

for _ in range(10):
    for _ in range(10):
        tim.dot(25,choice(list_colors))
        
        tim.forward(50)
       
    newLine()


screen=Screen()
screen.exitonclick()
