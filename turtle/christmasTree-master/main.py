import turtle
from turtle import *
import os
import random as r

# 播放音乐,建议一分二十秒
os.system("Lonely-Christmas.mp3")

# setup(520, 520, startx=None, starty=None)
bgcolor('black')
speed(0)
pencolor("green")
pensize(10)
penup()
hideturtle()
goto(0, 150)
showturtle()
pendown()
shape(name="classic")

# 画第一层树
seth(-120)
for i in range(10):
    fd(12)
    right(2)
penup()
goto(0, 150)
seth(-60)
pendown()
for i in range(10):
    fd(12)
    left(2)
seth(-150)
penup()
fd(10)
pendown()
for i in range(5):
    fd(10)
    right(15)
seth(-150)
penup()
fd(8)
pendown()
for i in range(5):
    fd(10)
    right(15)
seth(-155)
penup()
fd(5)
pendown()
for i in range(5):
    fd(7)
    right(15)
fillcolor("green")
# 画第二层树
penup()
goto(-55, 34)
pendown()
seth(-120)
for i in range(10):
    fd(8)
    right(5)

penup()
goto(50, 35)
seth(-60)
pendown()
for i in range(10):
    fd(8)
    left(5)
seth(-120)
penup()
fd(10)
seth(-145)
pendown()
for i in range(5):
    fd(10)
    right(15)
penup()
fd(10)
seth(-145)
pendown()
for i in range(5):
    fd(12)
    right(15)
penup()
fd(8)
seth(-145)
pendown()
for i in range(5):
    fd(10)
    right(15)
penup()
seth(-155)
fd(8)
pendown()
for i in range(5):
    fd(11)
    right(15)
# 画第三层树
penup()
goto(-100, -40)
seth(-120)
pendown()
for i in range(10):
    fd(6)
    right(3)
penup()
goto(80, -39)
seth(-50)
pendown()
for i in range(10):
    fd(6)
    left(3)
seth(-155)
penup()
fd(10)
pendown()
for i in range(5):
    fd(8)
    right(10)
penup()
fd(8)
seth(-145)
pendown()
for i in range(7):
    fd(8)
    right(10)
penup()
fd(8)
seth(-145)
pendown()
for i in range(7):
    fd(7)
    right(10)
penup()
fd(8)
seth(-145)
pendown()
for i in range(7):
    fd(7)
    right(10)
penup()
fd(8)
seth(-140)
pendown()
for i in range(7):
    fd(6)
    right(10)

# 画第四层树
penup()
goto(-120, -95)
seth(-130)
pendown()
for i in range(7):
    fd(10)
    right(5)
penup()
goto(100, -95)
seth(-50)
pendown()
for i in range(7):
    fd(10)
    left(5)
penup()
seth(-120)
fd(10)
seth(-155)
pendown()
for i in range(6):
    fd(8)
    right(10)
penup()
seth(-160)
fd(10)
seth(-155)
pendown()
for i in range(6):
    fd(8)
    right(10)
penup()
seth(-160)
fd(10)
seth(-155)
pendown()
for i in range(6):
    fd(8)
    right(10)
penup()
seth(-160)
fd(10)
seth(-160)
pendown()
for i in range(6):
    fd(8)
    right(10)
penup()
seth(-160)
fd(10)
seth(-160)
pendown()
for i in range(6):
    fd(8)
    right(10)
penup()
seth(-160)
fd(10)
seth(-165)
pendown()
for i in range(5):
    fd(10)
    right(11)
# 画树墩
penup()
pencolor("#592720")
goto(-70, -165)
seth(-85)
pendown()
for i in range(3):
    fd(5)
    left(3)
penup()
goto(70, -165)
seth(-95)
pendown()
for i in range(3):
    fd(5)
    right(3)
seth(-170)
penup()
fd(10)
pendown()
pendown()
for i in range(10):
    fd(12)
    right(2)


def guest(x, y, z):
    penup()
    goto(x, y)
    seth(-z)
    pendown()
    for angel in range(5):
        fd(10)
        right(10)


def guet(x, y, z):
    penup()
    goto(x, y)
    seth(-z)
    pendown()
    for angel in range(5):
        fd(10)
        left(10)


def qu(x, y, z):
    penup()
    goto(x, y)
    seth(-z)
    pendown()
    for angel in range(5):
        fd(6)
        right(10)
    seth(-150)
    fd(20)


# 树枝
pencolor("#faf0be")
guest(-70, -150, 160)
guest(100, -150, 160)
guet(110, -110, 50)
guest(160, -140, 150)
qu(80, -120, 180)
guest(70, -85, 165)
guest(-40, -85, 165)
guet(90, -50, 50)
guest(130, -80, 150)
pencolor("#faf0be")
qu(-40, -60, 180)
pencolor('#faf0be')
qu(80, -30, 180)
pencolor("#faf0be")
qu(40, 10, 180)
pencolor("#faf0be")
guest(-60, 30, 120)
guest(-20, -20, 150)
guet(45, 40, 60)
guest(-30, 40, 170)
guest(-30, 110, 115)
guet(40, 90, 60)
guest(80, 50, 160)
pencolor("#faf0be")


def hdj(x, y):
    penup()
    goto(x, y)
    seth(80)
    pendown()
    pensize(2)
    circle(5)
    seth(10)
    fd(15)
    seth(120)
    fd(20)
    seth(240)
    fd(20)
    seth(180)
    fd(20)
    seth(-60)
    fd(20)
    seth(50)
    fd(20)
    seth(-40)
    fd(30)
    seth(-130)
    fd(5)
    seth(135)
    fd(30)
    seth(-60)
    fd(30)
    seth(-150)
    fd(6)
    seth(110)
    fd(30)


def uit(x, y):
    penup()
    goto(x, y)
    pendown()
    pensize(2)
    circle(5)
    seth(-10)
    fd(15)
    seth(90)
    fd(15)
    seth(200)
    fd(15)
    seth(160)
    fd(15)
    seth(-90)
    fd(15)
    seth(10)
    fd(15)
    seth(-60)
    fd(20)
    seth(-180)
    fd(5)
    seth(110)
    fd(20)
    seth(-90)
    fd(20)
    seth(-180)
    fd(6)
    seth(70)
    fd(15)
    hideturtle()


def yut(x, y, z):
    penup()
    goto(x, y)
    pendown()
    seth(z)
    for po in range(5):
        fd(4)
        left(36)


def ytu(x, y, z):
    penup()
    goto(x, y)
    pendown()
    seth(z)
    for kk in range(5):
        fd(4)
        left(36)


# 小蝴蝶结
pencolor("pink")
seth(0)
uit(40, -160)
hdj(-80, -120)
yut(-67, -115, 120)
yut(-86, -123, 150)
hdj(40, -50)
yut(52, -45, 130)
yut(34, -55, 160)
seth(0)
uit(-20, -60)
ytu(-4, -60, 100)
ytu(-20, -60, 120)
hdj(-30, 20)
yut(-15, 25, 130)
yut(-40, 20, 180)
uit(30, 70)
ytu(45, 70, 100)
ytu(30, 70, 120)

# 大蝴蝶结
pencolor("#f799e6")
pensize(5)
penup()
seth(0)
goto(0, 150)
pendown()
circle(10)
seth(-15)
fd(40)
seth(90)
fd(40)
seth(200)
fd(40)
seth(160)
fd(40)
seth(-90)
fd(40)
seth(15)
fd(40)
seth(-70)
pencolor("#f799e6")
pensize(4)
fd(40)
seth(-180)
fd(10)
seth(100)
fd(40)
seth(-100)
fd(40)
seth(-180)
fd(10)
seth(70)
fd(40)
penup()
seth(0)
goto(0, 130)
pencolor("pink")
pendown()


def iou(x, y, z):
    penup()
    goto(x, y)
    pencolor("#f799e6")
    pendown()
    seth(z)
    for po in range(10):
        fd(4)
        left(18)


seth(0)
iou(35, 145, 100)
iou(-7, 145, 110)
pencolor("red")
pensize(7)
penup()
goto(-35, 135)
pendown()

# 圣诞帽
seth(-20)
pensize(2)
penup()
goto(-30, -120)
pencolor("#f8f8ff")
pendown()
fillcolor("red")
fd(30)
circle(4, 180)
fd(30)
circle(4, 180)
penup()
goto(-25, -115)
seth(75)
pendown()
begin_fill()
for i in range(5):
    fd(6)
    right(20)
seth(-10)
for i in range(5):
    fd(8)
    right(15)
seth(145)
for i in range(5):
    fd(5)
    left(2)
seth(90)
for i in range(5):
    fd(1)
    left(2)
seth(-90)
for i in range(4):
    fd(4)
    right(6)
seth(161)
fd(30)
end_fill()
pensize(1)
pencolor("black")


def koc(x, y, size):
    pensize(2)
    pencolor("black")
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    fillcolor("yellow")
    for i in range(5):
        left(72)
        fd(size)
        right(144)
        fd(size)
    end_fill()


# 星星
seth(-15)
koc(-120, -70, 10)
seth(10)
koc(100, -20, 10)
seth(-10)
koc(10, 40, 10)
seth(30)
koc(-80, 60, 10)
koc(100, -150, 10)
koc(-140, -150, 10)
koc(20, 120, 10)

# 袜子
seth(-20)
pensize(2)
penup()
goto(-20, 80)
pencolor("black")
pendown()
fillcolor("red")
fd(25)
circle(4, 180)
fd(25)
circle(4, 180)
penup()
goto(-15, 80)
pendown()
begin_fill()
fillcolor("red")
seth(-120)
fd(20)
seth(150)
fd(5)
circle(7, 180)
fd(15)
circle(5, 90)
fd(30)
seth(160)
fd(18)
end_fill()
penup()
seth(0)
goto(100, -230)
pendown()
turtle.color('deep pink')


# 雪花
def drawsnow():  # 定义画雪花的方法
    turtle.ht()  # 隐藏笔头，ht=hideturtle
    turtle.pensize(2)  # 定义笔头大小
    for i in range(200):  # 画多少雪花
        turtle.pencolor("white")  # 定义画笔颜色为白色，其实就是雪花为白色
        turtle.pu()  # 提笔，pu=penupﬁ
        turtle.setx(r.randint(-350, 350))  # 定义x坐标，随机从-350到350之间选择
        turtle.sety(r.randint(-100, 350))  # 定义y坐标，注意雪花一般在地上不会落下，所以不会从太小的纵座轴开始
        turtle.pd()  # 落笔，pd=pendown
        dens = 6  # 雪花瓣数设为6
        snowsize = r.randint(1, 10)  # 定义雪花大小
        for j in range(dens):  # 就是6，那就是画5次，也就是一个雪花五角星
            # t.forward(int(snowsize))  #int（）取整数
            turtle.fd(int(snowsize))
            turtle.backward(int(snowsize))
            # t.bd(int(snowsize))  #注意没有bd=backward，但有fd=forward，小bug
            turtle.right(int(360 / dens))  # 转动角度


penup()
pencolor("#e30022")
goto(200, -300)
pendown()
write("圣诞节快乐", align="right", font=("宋徽宗瘦金体", 25, "italic"))

drawsnow()  # 调用画雪花的方法
done()
