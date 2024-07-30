from turtle import *

speed(6)
width(6)
color("purple")

#I tried to make my house as realistic as possible with the knowledge I obtained throughout listening to lessons. I hope I did well.


#walls
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)

#cieling
right(30)
forward(200)
right(120)
forward(200)

#door
right(30)
forward(200)    
right(90)
forward(66)
right(90)
color("green")
begin_fill()
forward(88)
left(90)
forward(66)
left(90)
forward(88)
end_fill()

color("purple")


#cieling 2
penup()
goto(200, 0)
pendown()
left(135)
forward(111)
penup()
goto(200, -200)
pendown()
forward(111)
left(45)
forward(200)
left(62)
forward(200)

#window 1
color("orange")
penup()
goto(22, -44)
pendown()

left(115)
forward(44)
left(90)
forward(44)
left(90)
forward(44)
left(90)
forward(44)
left(90)
forward(22)
left(90)
forward(44)
left(90)
forward(22)
left(90)
forward(22)
left(90)
forward(44)

#window 2
penup()
goto(133, -44)
pendown()
forward(44)
left(90)
forward(44)
left(90)
forward(44)
left(90)
forward(44)
left(90)
forward(22)
left(90)
forward(44)
left(90)
forward(22)
left(90)
forward(22)
left(90)
forward(44)




exitonclick()