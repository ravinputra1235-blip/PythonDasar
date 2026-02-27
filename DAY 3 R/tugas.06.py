import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def circle(x,y,r,c):
    t.penup(); t.goto(x,y-r); t.pendown()
    t.color(c,c); t.begin_fill(); t.circle(r); t.end_fill()

# Lingkaran logo
circle(0,0,220,"black")
circle(0,0,200,"white")
circle(0,0,150,"#243b75")

# Tombol klik
circle(0,110,20,"white")
circle(0,110,12,"black")

# Tangan merah (ikon)
t.penup(); t.goto(-25,-40); t.pendown()
t.color("red","red"); t.begin_fill()
for _ in range(2):
    t.forward(50); t.left(90); t.forward(70); t.left(90)
t.end_fill()

turtle.done()