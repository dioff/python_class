"""
在游戏开始之前我们先学一些新东西
1、比较操作符:
    >, <, ==, >=, <=, !=
    (两个等于号代表等于，一个等于号代表赋值)
2、逻辑操作符:
    and, or 
    and:用于连接两个条件,只有在两个条件都为'True'时，整个表达式才会返回'True',否则返回'False'
    or:用于连接两个条件，只要有一个条件为'True'则为'True',全部为'False'才为'False'
    详见and_or.py
"""

import random 

answer = random.randint(1, 100)
# answer = 30

guess = eval(input("请猜猜1-100以内的数字"))
times = 1

while (guess != answer) and (times < 3):    # times < 3 == times <= 2
    if guess > answer:
        print("大了一点,再猜猜")
    else:
        print("小了！往大猜猜")
    guess = eval(input("再猜猜吧"))
    times = times + 1  

if (times <= 3) and (guess == answer):
    print("才{}次就猜对了，真棒！".format(times))
else:
    print("呜，三次都猜不对！！！")