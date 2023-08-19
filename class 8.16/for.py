'''
for循环语句的语法如下:
    for 变量 in 可迭代对象:
        循环体
所谓的可迭代对象就是指哪些元素可以呗单独提取出来的对象，如现在熟悉的字符串，像'Fish'就是由四个字符元素构成 10 --> AsII
for循环的作用就是每执行一次就会从该字符串中拿出一个字符，然后存放到变量中
while 条件：
    循环体
'''


for i in 'Fish':
    print(i)

'''
如果想要通过for语句来实现计算1+2+3+……+100的结果
'''

# 下面的代码他能正确的执行嘛？ 100 不可迭代
sum = 0
for i in 100:
    sum += i
print(sum)

'''
要想实现，也并不难，这就要认识一下for的大哥们range(101) == [0, 1, 2, 3, 4, 5, ……, 100]
range()的作用是为指定的整数生成一个数字序列（可迭代对象）
range(stop):从0生成导该参数的数字序列
range(start, stop):从start到stop-1 range(1, 5)
range(start, stop, step):指定步长，可以为负数
'''

sum = 0
for i in range(101):
    sum += i
print(sum)


a = 2
b = 3

a %=( a + b)
a = a % (a + b)  

