import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.left(90)
t.penup()
t.goto(0, -250)
t.pendown()

# Fungsi Fibonacci
def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

# Fungsi Fibonacci Tree
def fib_tree(n, length):
    if n == 0:
        return
    
    t.forward(length)
    
    t.left(30)
    fib_tree(n-1, length * 0.7)
    
    t.right(60)
    fib_tree(n-2, length * 0.7)
    
    t.left(30)
    t.backward(length)

# Gambar Fibonacci Tree
fib_tree(8, 80)

turtle.done()