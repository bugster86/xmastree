from turtle import *

bgcolor("black")
hideturtle()
title("BUON NATALE.....")
color('green','green')
speed(30)
penup()
goto(0,300)
begin_fill()
pendown()
right(30)

for i in range (0,20):
    forward(50)

    #circle(10)
    right(150)
    #circle(10)
    forward(30)
    left(150)

right(150)

p1=xcor()
p2=ycor()


goto(-p1-30,p2)

for i in range (0,19):
    right(150)
    forward(50)
    left(150)
    forward(30)

right(150)
forward(50)

end_fill()


penup()


p1=xcor()
p2=ycor()

goto(p1-20,p2+16)
showturtle()
color('red','red')
pendown()

speed(5)
begin_fill()
color('red','red')
right(30)
right(180-144)
for k in range(5):
		forward(40)
		left(144)
hideturtle()
end_fill()

ts= getscreen()
ts.getcanvas().postscript(file="tree.eps")
done()
