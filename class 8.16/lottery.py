'''
这是一个抽奖活动
choice():该方法可以从一个非空的序列（如列表）随机获取一个元素
'''
import random


list1 = ['买一送一', '买二送一', '全场半价']
for i in list1:
    print(i, end=' ')

print("这位客官，您看看您的手气如何")
answer = input("请输入‘好，本大爷就来试试’：")
if answer == "好,本大爷就来试试":
    print(random.choice(list1))
else:
    print('咋滴，这都能输错，走走走')
