import turtle

t = turtle.Turtle()
t.speed(0)
t.left(90)
t.penup()
t.goto(0, -250)
t.pendown()

def pohon_fibonacci(n, panjang):
    if n <= 0:
        return
    
    t.forward(panjang)
    
    t.left(30)
    pohon_fibonacci(n-1, panjang*0.7)
    
    t.right(60)
    pohon_fibonacci(n-2, panjang*0.7)
    
    t.left(30)
    t.backward(panjang)

# Gambar pohon fibonacci
pohon_fibonacci(8, 80)

turtle.done()