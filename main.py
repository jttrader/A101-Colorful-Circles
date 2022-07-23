import turtle as t

t.width(3)
t.speed(0)
t.screensize(1200, 1200)

i=0

t.begin_fill()
t.color("red")
while i<36:
    t.circle(210,360)
    t.rt(10)
    i += 1
t.end_fill()

t.color("violet")
while i<36*2:
    t.circle(210,360)
    t.rt(10)
    i += 1

t.color("blue")
while i<36*3:
    t.circle(180,360)
    t.rt(10)
    i += 1

t.color("light blue")
while i<36*4:
    t.circle(150,360)
    t.rt(10)
    i += 1

t.color("green")
while i<36*5:
    t.circle(120,360)
    t.rt(10)
    i += 1

t.color("yellow")
while i<36*6:
    t.circle(90,360)
    t.rt(10)
    i += 1

t.color("orange")
while i<36*7:
    t.circle(60,360)
    t.rt(10)
    i += 1

t.color("red")
while i<36*8:
    t.circle(30,360)
    t.rt(10)
    i += 1

t.color("white")
while i<36*9:
    t.circle(5,360)
    t.rt(10)
    i += 1

t.done()