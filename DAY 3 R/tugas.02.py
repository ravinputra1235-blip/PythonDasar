import turtle

t = turtle.Turtle()
t.speed(3)

# Fungsi pindah posisi
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# =========================
# Persegi Panjang - WARNA MERAH
move(-150, 0)
t.color("red")
t.begin_fill()
for _ in range(2):
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
t.end_fill()

# =========================
# Segitiga - WARNA BIRU
move(150, 0)
t.color("blue")
t.begin_fill()
for _ in range(3):
    t.forward(120)
    t.left(120)
t.end_fill()

turtle.done()