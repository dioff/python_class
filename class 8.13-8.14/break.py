'''
有人说过，一旦进入到了死循环就退出不了了，真的是这样的嘛？
那当然还有break在，可以让程序随时跳出循环的枷锁
break:终止循环体，跳出循环体
'''

bingo = '清蒸'
answer = input('甲鱼是清蒸好吃还是炖了好吃？')

while True:
    if answer == bingo:
        break
    answer = input("错了哟，请重新输入")

print("对了嘛，只有清蒸才是原汁原味的")

'''
请用代码，求出2018年到2050年的以后的第一个闰年(（可以被4整除 and 但不能被100整除），或者可以被400整除，被定为闰年)
'''

for year in range(2018, 2100):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        break
print("2018年后的第一个闰年为{}".format(year))