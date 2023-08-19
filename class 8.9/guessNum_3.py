"""
while循环的语法
while 条件:
    条件为真执行的操作
"""

temp = input("猜一猜我现在心里想的数字1-9之内")
guess = int(temp)
while guess != 8:
    if guess > 8:
        print("猜错了，有点猜大了哟")
    else:
        print("猜错了，有点猜小了哟")

    temp = input("再试试吧：")
    guess = int(temp)

print("恭喜你，猜对了")