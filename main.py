import turtle as t
import random

my_screen = t.Screen()
timmy = t.Turtle()
t.colormode(255)
timmy.hideturtle()
my_screen.setworldcoordinates(-1, -1, my_screen.window_width() - 1, my_screen.window_height())

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for i in range(30):
#     rgb = colors[i].rgb
#     red = rgb.r
#     green = rgb.g
#     blue = rgb.b
#     color_tuple = (red, green, blue)
#     rgb_colors.append(color_tuple)

color_list = [(236, 251, 243), (200, 10, 35), (247, 236, 37), (240, 244, 251), (239, 231, 3), (36, 216, 77), (223, 159, 61), (39, 79, 185), (28, 39, 159), (210, 73, 16), (17, 151, 18), (239, 39, 152), (65, 9, 27), (188, 14, 9), (216, 25, 127), (218, 140, 198), (223, 161, 7), (59, 12, 7), (67, 202, 227), (10, 96, 60), (84, 80, 212), (17, 19, 52), (237, 157, 218), (106, 232, 195), (99, 205, 136), (212, 84, 58), (8, 222, 235), (236, 171, 161)]

#requirements
#paint with 10 by 10 rows of spot
#space of 50 paces, size 20
height = 0
for i in range(10):
    height += 50
    for j in range(10):
        timmy.pendown()
        timmy.color(random.choice(color_list))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)

    timmy.goto(0, height)



my_screen.exitonclick()