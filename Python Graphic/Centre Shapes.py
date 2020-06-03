import turtle
import math

#填充形状 begin_fill 告知开始 end_fill 告知结束 
#turtle.begin_fill()将当前位置作为起点，并告知程序开始启动填充图形。
#turtle.end_fill()将当前位置作为重点，并告知程序关闭填充图形。
#当开始和结束没有形成闭合区域会默认开始和结束点连接在一起

#判断当前是否正在填充 filling
#turtle.filling()
#不在填充为false
#正在填充为True

#重新开始作画  reset 和 clear
#turtle.clear() 只消除作画痕迹，画布的属性还在
#turtle.reset() 全部重来，参数也变为默认

#写文本text write()
#turtle.write(arg, move=False, align="left", font=("Arial", 8, "normal"))
#arg 为要写的字符串 move 为False 则箭头不移动 为True 则移动

turtle.title("Richard's turtle")
turtle.setup(900,600,0,0)
turtle.fillcolor("#FF7799")

m = int(input("Enter a number: "))
n = int(input("Length of each side: "))  

i = 180/m
u = n/2 
pi = math.pi
h = math.sin(pi/m)
l = u/h

turtle.pencolor("#FF0000")
turtle.left(90-i)
turtle.forward(l)
turtle.left(90+i)
turtle.pencolor("#000000")
A = 360/m

turtle.begin_fill()

for f in range (m):
    turtle.forward(n)
    if f <= m-1:
        turtle.left(A)
        
turtle.end_fill()

turtle.penup()
turtle.fd(u)
turtle.left(90)
k = math.cos(pi/(2*m))
turtle.fd(n*k)
turtle.fd(40)
turtle.left(90)
turtle.write("This is Richard's work! Impressive, right?",move=True,align="left", font=("Comic Sans MS", 18, "normal"))
turtle.hideturtle()

turtle.exitonclick()
