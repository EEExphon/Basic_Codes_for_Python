from turtle import *
speed(0)

r = 1.0
g = 1.0
b = 1.0
q = 0.0
w = 0.0
e = 0.0

pencolor((r, g, b))
width(3)
bgcolor((q,w,e))

up()

rt(30)
fd(100)
rt(120)

down()

n = 0

while n < 450:
    
    g = g - 0.001
    b = b - 0.001
    if q <= 1:
        q = q + 0.01
        w = w + 0.01
        e = e + 0.01
        bgcolor(q,w,e)
    pencolor((r, g, b))
    fd(160+n)
    rt(72+(n/10))
    
    g = g - 0.001
    b = b - 0.001
    if q <= 1:
        q = q + 0.01
        w = w + 0.01
        e = e + 0.01
        bgcolor(q,w,e)
    pencolor((r, g, b))
    fd(160+n)
    rt(72+(n/10))
    
    n = n+1
    
while n >= 450 and n <= 900:
    
    g = g + 0.001
    b = b + 0.001
    if q <= 1:
        q = q + 0.01
        w = w + 0.01
        e = e + 0.01
        bgcolor(q,w,e)
    pencolor((r, g, b))
    fd(160+n)
    rt(72+(n/10))
    
    g = g + 0.001
    b = b + 0.001
    if q <= 1:
        q = q + 0.01
        w = w + 0.01
        e = e + 0.01
        bgcolor(q,w,e)
    pencolor((r, g, b))
    fd(160+n)
    rt(72+(n/10))
    
    n = n+1
    
turtle.hideturtle()
