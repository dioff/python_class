"""第二个小游戏"""
guess = eval(input("猜一猜我现在心里想的数字1-9之内"))
answer = 8
if guess == answer:
    print("猜对了你怎么知道我心里所想的呢")
else:
    if guess > answer:
        print("猜错了，有点猜大了哟")
    else:
        print("猜错了，有点猜小了哟")

