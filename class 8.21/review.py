'''
review 
for 变量 in range():  生成一个列表（可迭代）
    循环体
    
range():
range(10) -- > [0 , ... , 9]
range(1,10)
range(2,8,2)  -- > ?[2, 4, 6]
list : 列表
list(什么东西都可以存放,还可以行列表)
数据类型：
int ,float, bool, str
list 他有很多方法
比如说：
添加，
append():只能传入一个东西，不可以多个
extend():把一个新列表拼接在老列表的后面
insert():随便加在列表的哪个位置，（位置，东西）位置：可正可负
序数词是从0开始数的,就说第几个就是从第0个开始
基数词还是从1开始数

'''
# list1 = ['pig', 'pigger', 'gerpi']
# list1.insert(0, 'people')
# list1.insert(4, 'human')
# print(list1)

# 如果我要拿出一个列表的第三个数字我该怎么做
list2 = [1,2,3,4,5,6,7,8]
a = 0
for i in list2:
   a += 1
   if a == 3:
       print(i)
'''
索引:list2[索引号]
len():获取列表元素的个数，获取字符串的长度（包括标点符号）
'''
print(list2[2])
a = len(list2) - 1
print(list2[a])
print(list2[-1])

