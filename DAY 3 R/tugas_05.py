import turtle

t = turtle.Turtle()
t.speed(0)
t.bgcolor("skyblue")

# Pindah ke tengah
t.penup()
t.goto(0, 0)
t.pendown()

# Warna matahari
t.color("orange", "yellow")

# Lingkaran matahari
t.begin_fill()
t.circle(80)
t.end_fill()

# Sinar matahari
t.penup()
t.goto(0, 0)
t.setheading(0)
t.pendown()

t.color("orange")
for _ in range(36):
    t.forward(100)
    t.backward(100)
    t.right(10)

# Matahari kecil di tengah
t.penup()
t.goto(0, -20)
t.pendown()
t.color("gold", "gold")
t.begin_fill()
t.circle(40)
t.end_fill()

turtle.done()