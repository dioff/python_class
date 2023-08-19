"""
python的发明者为了使我们能够快乐的使用好这一门语言，再发布python的时候带了非常多的实用模块，其中random就是生成一个随机数的模块
这个模块里有一个函数为randint(),他会返回一个随机的整数
"""

import random

answer = random.randint(1, 9)
temp = input("猜一猜我现在心里想的数字1-9之内")
guess = int(temp)
while guess != answer:
    if guess > answer:
        print("猜错了，有点猜大了哟")
    else:
        print("猜错了，有点猜小了哟")

    temp = input("再试试吧：")
    guess = int(temp)

print("恭喜你，猜对了")