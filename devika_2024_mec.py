import turtle
t = turtle.Turtle()
t.hideturtle()
w=turtle.Screen()
w.bgcolor((0.7, 0.6, 0.5))
t.color("yellow")
t.speed(0)
list=["red", "yellow", "red", "yellow"]
for i in range (240):
    t.color(list[i%4])
    t.pensize(i/10+1)
    t.forward(i)
    t.left (45)


t.up()
t.goto(0,-170)
t.down()
t.pencolor("purple")
t.begin_fill()
t.fillcolor("purple")
t.circle(190)
t.end_fill()


t.up()
t.goto(0,-155)
t.down()
t.pencolor("white")
t.pensize(15)
t.circle(170)



t.up()
t.goto(0,-125)
t.down()
t.pencolor("green")
t.begin_fill()
t.fillcolor("green")
t.circle(140)
t.end_fill()

t.up()
t.goto(0,-125)
t.down()
t.pencolor("orange")
t.begin_fill()
t.fillcolor("orange")
t.circle(140,steps=4)
t.end_fill()

t.up()
t.goto(0,-55)
t.down()
t.pencolor("red")
t.begin_fill()
t.fillcolor("red")
t.circle(70,steps=4)
t.end_fill()


t.pencolor("brown")
t.pensize(15)
t.up()
t.goto(0,-15)
t.down()
t.circle(30)


t.up()
t.goto(0,-5)
t.down()
t.begin_fill()
t.fillcolor("yellow")
t.pencolor("yellow")
t.circle(20)

t.end_fill()

t.up()
t.goto(0,110)
t.down()
t.pencolor("blue")
t.pensize(5)
t.begin_fill()
t.fillcolor("white")
t.circle(10)
t.end_fill()

t.up()
t.goto(0,-90)
t.down()
t.pencolor("blue")
t.pensize(5)
t.begin_fill()
t.fillcolor("white")
t.circle(10)
t.end_fill()

t.up()
t.goto(-100,5)
t.down()
t.pencolor("blue")
t.pensize(5)
t.begin_fill()
t.fillcolor("white")
t.circle(10)
t.end_fill()

t.up()
t.goto(100,5)
t.down()
t.pencolor("blue")
t.pensize(5)
t.begin_fill()
t.fillcolor("white")
t.circle(10)
t.end_fill()







