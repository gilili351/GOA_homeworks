from turtle import*

#we want paint to house

#we want paint to square


color("yellow")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
forward(66)
end_fill()

#we want paint to door
color("black")
begin_fill()
left(90)
forward(100)
right(90)
forward(66)
right(90)
forward(100)
end_fill()


penup()
goto(200,200)
color("red")
begin_fill()
pendown()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(80,125)
pendown()
color("dark blue")
begin_fill()
right(60)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()
penup()
goto(120,125)
pendown()
color("dark blue")
begin_fill()
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()



exitonclick()