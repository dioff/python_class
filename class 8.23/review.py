'''
list列表:有非常多的方法
very old:
append():在列表的末尾加上一个元素，只能放一个
extend():将两个列表拼接在一起
insert():有两个参数，分别是：位置和东西，位置可正可负，正表示从左到右按照0开始数
负数的话是指与最后一个元素的距离

列表的索引：
列表名[索引号]
索引号有正有负
正表示从左到右从0开始数
负表示从右到左从-1开始

得到列表的长度-- > len():作用获得列表元素的个数，还可以获取字符串的长度
可以用来索引最后一个东西的位置

如果我们要交换列表中两个元素的位置

删除：
pop():参数是索引号，会显示要删除的东西，并删除
remove():参数是元素，把指定的元素删除
del:python内置的删除手段，不止可以删除列表的元素，甚至可以把列表全部删除
'''
list1 = ['a', 'b', 'c', 'd']
# a = len(list1) - 1
# print(list1[a])

# print(list1[-1])

conut = 0
for i in list1:
    if conut == len(list1) -1:
        print(i)
        break
    conut += 1

# temp = list1[1] # --> 'b'
# list1[1] = list1[2]
# list1[2] = temp

list1[1], list1[2] = list1[2], list1[1]
print(list1)


'''
把列表的每个元素拿出来
判断那个元素为列表
把列表的东西再拿出来
break

'''
list2 = ['a', 'b', ['e', 'f'],'c', 'd']
for i in list2:
    if type(i)==list:
        a = 0
        for e in i:
            a += 1
            if a == len(i):
                print(e)
                
                
list2 = ['a', 'b', ['e', 'f'],'c', 'd']
for i in list2:
    if type(i)==list:
        print(i[len(i) - 1])
        
print(list2[2][1])

                
list_wen = ['鱼尾纹', '脖子纹', '蚊子']
list_wen.pop(2)
print(list_wen)  
list_wen.remove('脖子纹')
print(list_wen)
del list_wen[0]
print(list_wen)



list1 = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
list2 = [list1[0], list1[2], list1[4]]

'''
切片：列表名[索引号:索引号]
'''
print(list1[0:3])