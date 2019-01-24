from turtle import *
penup()
goto(-140,140)

for step in range(6):
    write(step)
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
