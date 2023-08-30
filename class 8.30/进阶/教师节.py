import turtle as t
import math as m
import random as r
 

 
def drawX(a, i):
    angle = m.radians(i)
    return a * m.cos(angle)
 
 
def drawY(b, i):
    angle = m.radians(i)
    return b * m.sin(angle)
 
 
# 设置背景颜色，窗口位置以及大小
# t.bgcolor("#d3dae8")
# t.setup(width=900, height=600, startx=0, starty=0)
t.title("老师，祝您节日快乐！")
 
t.setup(width=1450, height=1450, startx=0, starty=0)
t.speed(0)
t.rt(-120)
t.up()
t.pensize(6)
t.goto(180, 150)
t.bgcolor('white')
t.down()
t.color('black')
t.circle(190, 100)
t.fd(20)
for i in range(260):
    t.fd(1)
    t.lt(0.5)
for i in range(8):
    t.fd(19)
    t.lt(1)
for i in range(260):
    t.fd(1)
    t.lt(0.5)
t.up()
t.goto(-70, -16)
t.setheading(245)
t.down()
for i in range(35):
    t.fd(1.5)
    t.lt(0.5)
for i in range(5):
    t.fd(1.5)
    t.lt(0.0125)
for i in range(9):
    t.fd(0.75)
    t.lt(1.5)
for i in range(22):
    t.fd(1)
    t.lt(0.3)
for i in range(20):
    t.fd(1)
    t.lt(3)
for i in range(180):
    t.fd(1)
    t.lt(0.20)
for i in range(20):
    t.fd(1)
    t.lt(3)
for i in range(22):
    t.fd(1)
    t.lt(0.3)
for i in range(9):
    t.fd(0.75)
    t.lt(1.5)
for i in range(5):
    t.fd(1.5)
    t.lt(0.0125)
for i in range(25):
    t.fd(1.5)
    t.lt(0.5)
t.up()
t.goto(-65, -119)
t.down()
t.begin_fill()
t.color('black')
t.setheading(280)
t.circle(30, 135)
t.end_fill()
t.up()
t.goto(50, -129)
t.down()
t.begin_fill()
t.color('black')
t.setheading(305)
t.circle(30, 135)
t.end_fill()
t.up()
t.goto(200, 118)
t.down()
t.begin_fill()
t.color('black')
t.setheading(20)
t.circle(50, 210)
t.end_fill()
t.up()
t.goto(-70, 227)
t.down()
t.begin_fill()
t.color('black')
t.setheading(103)
t.circle(50, 230)
t.end_fill()
t.up()
t.goto(117, -40)
t.setheading(25)
t.down()
t.begin_fill()
t.color('black')
for i in range(70):
    t.fd(1)
    t.lt(-0.5)
for i in range(160):
    t.fd(0.25)
    t.lt(-0.9)
for i in range(70):
    t.fd(1)
    t.lt(-0.65)
t.end_fill()
t.up()
t.goto(-75, -25)
t.setheading(155)
t.down()
t.begin_fill()
t.color('black')
for i in range(70):
    t.fd(1)
    t.lt(0.5)
for i in range(160):
    t.fd(0.25)
    t.lt(0.85)
for i in range(70):
    t.fd(1)
    t.lt(0.65)
t.end_fill()
t.up()
t.goto(-45, 80)
t.begin_fill()
t.color('black')
t.down()
t.circle(25.25)
t.end_fill()
t.up()
t.goto(-50.5, 74.5)
t.begin_fill()
t.color('black')
t.down()
t.circle(26.25)
t.end_fill()
t.up()
t.goto(-43, 100)
t.begin_fill()
t.color('white')
t.down()
t.circle(5.5)
t.end_fill()
t.up()
t.goto(100, 67)
t.begin_fill()
t.color('black')
t.down()
t.circle(25.25)
t.end_fill()
t.up()
t.goto(105.5, 63.5)
t.begin_fill()
t.color('black')
t.down()
t.circle(25.25)
t.end_fill()
t.up()
t.goto(96, 92)
t.begin_fill()
t.color('white')
t.down()
t.circle(5.5)
t.end_fill()
t.up()
t.goto(105, 40)
t.begin_fill()
t.color('tomato')
a = 0.45
t.down()
t.setheading(270)
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a+0.045
        t.lt(3)
        t.fd(a)
    else:
        a = a-0.045
        t.lt(3)
        t.fd(a)
t.end_fill()
t.up()
t.goto(-60, 50)
t.begin_fill()
t.color('tomato')
a = 0.4
t.down()
t.setheading(90)
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a+0.04
        t.lt(3)
        t.fd(a)
    else:
        a = a-0.04
        t.lt(3)
        t.fd(a)
t.end_fill()
t.up()
t.goto(20, 75)
t.begin_fill()
t.color('black')
t.setheading(125)
t.down()
for i in range(25):
    t.fd(0.75)
    t.lt(-1)
for i in range(20):
    t.fd(0.25)
    t.lt(-4.5)
for i in range(30):
    t.fd(0.75)
    t.lt(-1)
for i in range(20):
    t.fd(0.25)
    t.lt(-4.5)
for i in range(25):
    t.fd(0.75)
    t.lt(-1)
for i in range(20):
    t.fd(0.25)
    t.lt(-4.5)
t.end_fill()
t.up()
t.setheading(260)
t.goto(23, 75)
t.down()
for i in range(45):
    t.fd(1)
    t.lt(3)
t.up()
t.setheading(260)
t.goto(23, 75)
t.down()
for i in range(45):
    t.fd(1)
    t.lt(-3)
t.color('red')
x = -100
t.up()
 
t.color("red", "yellow")
t.goto(-400, 200)
t.down()
t.begin_fill()
for _ in range(50):
    t.pensize(1)
    t.forward(200)
 
    t.left(170)
t.end_fill()
 
 
# ##随机
color = ["#e28cb9", "#805a8c", "#eaa989", "#6e90b7", "#b8b68f", "#e174b5", "#cf737c", "#7c8782"]
for i in range(80):
    t.pu()
    x = r.randint(-420, 420)
    y = r.randint(-25, 30)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(2, 5), color[r.randint(0, 7)])
for i in range(40):
    t.pu()
    x = r.randint(-190, 190)
    y = r.randint(-35, 10)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(2, 5), color[r.randint(0, 7)])
 
for i in range(40):
    t.pu()
    x = r.randint(-480, 480)
    y = r.randint(60, 90)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(2, 5), color[r.randint(0, 7)])
for i in range(30):
    t.pu()
    x = r.randint(-450, 450)
    y = r.randint(45, 70)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(2, 5), color[r.randint(0, 7)])
for i in range(50):
    t.pu()
    x = r.randint(-500, 500)
    y = r.randint(120, 300)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(3, 5), color[r.randint(0, 7)])
t.seth(90)
t.pu()
t.goto(0, 0)
t.fd(300)
t.left(90)
t.fd(170)
t.pd()
t.write("Happy Teachers' Day", font=("Comic Sans MS", 50))
 
 
t.color('purple')
t.penup()
t.goto(-400, -200)
t.pendown()
t.write('致：敬爱的老师们  ', font=('楷体', 32, 'bold'))
t.color('red')
t.penup()
t.goto(-300, -280)
t.pendown()
t.write('祝 您 节 日 快 乐！桃 李 满 天 下！', font=('楷体', 30, 'bold'))
t.color('purple')
t.done()