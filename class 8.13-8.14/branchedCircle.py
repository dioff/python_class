'''
我们小时候可能都玩过或者听过，飞机大战这个游戏，
进入游戏我们很容易发现其实就是进入了一个大循环，因为游戏的套路基本上都是这么一回事
只要没有撞到敌机触发死亡机制，那么敌机就会不断的生成，这足以证明整个游戏都是在循环中执行的
'''


'''
我们先来了解一下什么是分支？
分支也就是习惯使用的if判断条件,在条件持续保持成立或者不成立的情况下，都执行固定的流程。
一旦条件发生改变，原来成立的条件为不成立，程序就走另一条路了
'''

'''
其实飞机大战这个小游戏就是简单的几个循环和if判断就写出来了!!!
当然要达到自己可以手动写一个界面小游戏的水平，还需要掌握更多知识
但是我们可以把游戏的框架提出来
'''

# loading BGM
# player BGM
# creat my_plane

# while True:
#     if clock exit:
#         exit()
#     if time:
#         creat many enemy_planes
#         enemy_planes.move()
#         screnn.refresh()
#     if clock():
#         my_plant_pose = clock.pose()
#         screnn.refresh()
#     if my_plant_pose == enemy_planes.pose():
#         game_over()
#         stop BGM

        

'''
上面的代码的要领就是：分支和循环
分支：只有符合条件，才回去做某件事
循环：只要符合条件，就持续做某件事
现在来靠靠你：成绩按照分数划分等级，90分以上为A，80~90分为B，60~80分为C，60分一下为D
现在有一个需求，当用户输入分数，自动转换为A,B,C,D
'''

score = eval(input('请输入一个分数'))

if 100 >= score >= 90:
    print('A')
if 90 > score >= 80:
    print('B')
if 80 > score >= 60:
    print('C')
if 60 > score >= 0:
    print('D')
if score < 0 or score > 100:
    print('输入错误！')

# 当然还可以写成
score = eval(input('请输入一个分数'))

if 100 >= score >= 90:
    print('A')
elif 90 > score >= 80:
        print('B')
elif 80 > score >= 60:
        print('C')
elif 60 > score >= 0:
        print('D')
else:
    print('输入错误！')

# 当然上面的代码还有该进方式
score = eval(input('请输入一个分数'))

if 100 >= score >= 90:
    print('A')
elif 90 > score >= 80:
    print('B')
elif 80 > score >= 60:
    print('C')
elif 60 > score >= 0:
    print('D')
else:
    print('输入错误！')
'''
我们有这么多方式可以执行，但是对于第一种方式而言，当我们输入98以后进入print('A')，并没有结束程序
但是后两种方式而言，当判断完以后会立刻退出
'''



