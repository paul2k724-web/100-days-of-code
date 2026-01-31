import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [
    (202, 164, 110), (240, 245, 241), (149, 75, 50),
    (222, 201, 136), (52, 93, 124), (170, 154, 41),
    (138, 31, 20), (134, 163, 184), (197, 92, 73),
    (47, 121, 86), (73, 43, 35)
]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

t.Screen().exitonclick()
