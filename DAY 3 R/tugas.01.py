import turtle

t = turtle.Turtle()
t.speed(3)

# Fungsi bantu
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# 1. Gambar bangun datar (tanpa warna)

# Persegi panjang
move(-300, 100)
for _ in range(2):
    t.forward(120)
    t.right(90)
    t.forward(60)
    t.right(90)

# Segitiga
move(-100, 100)
for _ in range(3):
    t.forward(100)
    t.left(120)

# Trapesium
move(100, 100)
t.forward(120)
t.right(120)
t.forward(60)
t.right(60)
t.forward(60)
t.right(60)
t.forward(60)

# Jajar genjang
move(-300, -100)
t.forward(120)
t.right(60)
t.forward(60)
t.right(120)
t.forward(120)
t.right(60)
t.forward(60)

# Belah ketupat
move(-100, -120)
t.forward(80)
t.right(60)
t.forward(80)
t.right(120)
t.forward(80)
t.right(60)
t.forward(80)