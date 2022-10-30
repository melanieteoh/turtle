from turtle import*
penup()
goto(-200, 0)
pendown()
count = 1

#Beginning of the block of commands to be repeated
while count <= 4:
    left(80)
    forward(20)
    right(160)
    forward(20)
    left(80)
    forward(5)
    right(65)
    forward(10)
    left(150)
    forward(90)
    right(170)
    forward(80)
    left(85)
    forward(20)
    left(75)
    forward(25)
    right(150)
    forward(25)
    left(75)
    forward(40)
#End of the block of commands to be repeated
count += 1

exitonclick()
