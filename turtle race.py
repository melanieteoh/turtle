from turtle import*
from random import randint
exitonclick()

goto(-200,0)
width(500)
color("lightsteelblue")
forward(400)

penup()
goto(150,250)
pendown()
color("navy")
width(5)
goto(150,-250)

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

t1.shape("turtle")
t1.color("forestgreen")
t1.penup()
t1.goto(-150,50)

t2.shape("turtle")
t2.color("paleturquoise")
t2.penup()
t2.goto(-150,0)

t3.shape("turtle")
t3.color("aquamarine")
t3.penup()
t3.goto(-150,-50)

def win(t):
    t.goto(0,0)
    n = 1
    while n <= 30:
        t.forward(10)
        t.left(12)
        n += 1
    t.write("woohoo victory!", font=("Arial", 25))

bet = input("Who do you think will win the race? T1, T2 or T3?")

count = 0
while count <= 20:
    step1 = randint(1,50)
    step2 = randint(1,50)
    step3 = randint(1,50)
    t1.forward(step1)
    t2.forward(step2)
    t3.forward(step3)

    if t1.xcor() >= 150:
        break
    elif t2.xcor() >= 150:
        break
    elif t3.xcor() >= 150:
        break

    count += 1

if t1.xcor() > t2.xcor() and t1.xcor() > t3.xcor():
    win(t1)
    winner = "T1"
elif t2.xcor() > t1.xcor() and t2.xcor() > t3.xcor():
    win(t2)
    winner = "T2"
elif t3.xcor() > t2.xcor() and t3.xcor() > t1.xcor():
    win(t3)
    winner = "T3"

if bet == winner:
    print("Congratulations! You won!")
else:
    print("Unlucky, now pay up!")
