'''
??? 纳尼 ??? 
按道理来说else和if应该是一对
怎么回事 else怎么和循环挂钩了?
hold on
while 和 for后面其实也可以加一个else语句,表示当条件不成立时执行该程序

语法如下:

while 条件:
    循环体
else:
    条件不成立的时候执行的内容

for 变量 in 可迭代对象:
    循环体
else:
    条件不成立时执行的内容

maybe你认为没有必要这么做,当条件不成立时，自然要结束循环并执行接下来的语句
'''
sum = 0
for i in range(101):
    sum += 1
else:
    print(sum)

# 如果遇到break则大不相同
for year in range(2018, 2100):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        break
else:
    print("2018年后的第一个闰年为{}".format(year))
# 由于break语句会跳出循环，所以else不执行