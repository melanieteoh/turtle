from turtle import *
exitonclick()

andro_step = input("How many pixels has the Andromeda gone?")
sir_step = andro_step * 2

penup()
goto(-200,100)
pendown()
forward(sir_step)
