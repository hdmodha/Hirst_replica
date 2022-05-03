import turtle
import random
color_list = [(249, 212, 93), (150, 69, 97), (53, 99, 155), (232, 137, 62), (107, 174, 211),
              (114, 83, 59), (200, 77, 109), (145, 134, 72), (141, 192, 140), (72, 103, 90),
              (68, 162, 92), (5, 165, 179), (227, 161, 183), (115, 126, 142)]
timmy = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)
timmy.speed("fastest")
timmy.setheading(225)
timmy.penup()
timmy.hideturtle()
timmy.forward(250)
timmy.setheading(0)
x_cor = timmy.xcor()

for _ in range(10):

    for _ in range(10):
        random_color = random.choice(color_list)
        timmy.dot(20, random_color)
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()

    timmy.penup()
    y_cor = timmy.ycor()
    y_cor += 50
    timmy.goto(x_cor, y_cor)


screen.exitonclick()
