'''
for 变量 in 可迭代对象:
    循环体
可迭代对象有哪些？ 字符串，列表

range():三种用法
range(10): 0-9
range(1, 8):1 - 7         -----> 列表（可迭代对象）
range(1,10,2):13579

'''
for i in range(1, 10):
    if i == 5:
        break
    print(i)
    
'''
continue:结束本次循环
break:直接推出循环
'''
'''
数组：存放一个数据类型的东西，只能存放同一种数据类型
列表:存放很多东西的小黑屋,整型、浮点型、字符串、bool、列表

'''
# 手搓法
list1 = [1, 2, 34]

list1.append("pigger")

print(list1)

list1.extend(['zhu', 'zhuzhu'])
# what is append ?
print(list1)

'''
append:是一个方法，列表的方法，作用是追加，在列表后面追加一个元素
“你为什么{}好阿？”.format("不")
那我们want many 元素
extend():是列表的表的另一个方法，作用是传入一个列表，把传入的列表放在最后
'''

'''
新的方法：！
无他，唯手熟尔
insert(位置，东西):
插入到相应的位置

'''

dogs = ['dog', 'ddog', 'doog', 'dogg']

dogs.insert(-2, 'pigger')
print(dogs)


# 在没有学过取出单个元素的情况下，我们该怎么把列表中的某个元素给取出来？
'''
如果我们想从一个列表中取出一个元素，那么我们肯定需要
元素的位置
我们还要想办法，能让每个元素都单独拿出来
(for循环能够解决把每个元素单独拿出来)
'dog', 'ddog', 'doog', 'dogg'
这个顺序就是取出的位置
所以我们想要取出第几个我们就在第几次把东西print出来即可
'''

index = 0
for i in ['dog', 'ddog', 'doog', 'dogg']:
    # 循环体
    index += 1
    if index == 2:
        print(i)
        
eggs = ['鸡蛋', '鸭蛋', '鹅蛋', '翟沁妤']
last_one = len(eggs) - 1
# print(eggs[last_one]) 
print(eggs[-1]) 

print(len('震惊！！！99%都不知道，翟沁妤是一个非常牛逼的人'))
