import turtle

t = turtle.Turtle()
t.speed(3)

# Fungsi pindah posisi
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Ukuran bendera
lebar = 300
tinggi = 200

# Bagian MERAH (atas)
move(-150, 100)
t.color("red")
t.begin_fill()
for _ in range(2):
    t.forward(lebar)
    t.right(90)
    t.forward(tinggi/2)
    t.right(90)
t.end_fill()

# Bagian PUTIH (bawah)
move(-150, 0)
t.color("white")
t.begin_fill()
for _ in range(2):
    t.forward(lebar)
    t.right(90)
    t.forward(tinggi/2)
    t.right(90)
t.end_fill()

turtle.done()