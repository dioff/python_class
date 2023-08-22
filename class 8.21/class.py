eggs = ['鸡蛋', '鸭蛋', '鹅蛋', '翟沁妤']
temp = eggs[1]
eggs[1] = eggs[2]
eggs[2] = temp
print(eggs)

'''
python的精髓是偷懒
偷懒的方法
'''
list1 = [121, 'pig', [2,3]]
a = 0
for i in list1:
    a += 1
    if a == 3:
        b = i
        print(b[0])
        
print(list1[1][1])

'''
str本质是一个类似于列表的东西
他也可以通过索引来得到
'''
a = '你脑子非常好'
print(a[1:3])

'''
向列表里面加入东西:append,extend,insert
向列表里面删除东西:pop(),del,remove()
pop(),remove()都是list的方法

'''
'''
pop():把列表的某个东西弹出来，并且删除他（会先显示以下弹出的东西)
参数为你要弹出东西的索引号，如果没有索引号,默认弹出最后一个
'''
list_wen = ['鱼尾纹', '妊娠纹', '脖子纹']
print(list_wen.pop())
print(list_wen)

'''
remove():把列表中已经存在的东西，给移除，需要传入的参数为列表内的元素，如果列表内没有这个元素，那我们不可以使用remove
'''
list_wen.remove('妊娠纹')
print(list_wen)


'''
remove()和pop()的区别是什么？
一个输入列表的元素，一个是输入列表的位置（索引值)
'''

list_wen.extend(["斑", "痘"])
print(list_wen)
del list_wen[1]
print(list_wen)

'''
append(),extend(),insert()
len , 索引
pop(), remove(), del
'''