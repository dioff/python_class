'''
除了break以外,还有什么能跳出循环呢? continue
continue:跳出本轮循环,并开始下一轮循环

那现在我想打印2018年以后的所有闰年份应该怎么改?
'''

for year in range(2018, 2050):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year)
        continue
