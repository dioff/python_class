'''
增加：
append() extend() insert()
索引：
列表名[索引号]
删除：
pop():参数为索引号
remove():参数为列表的元素
del: del 列表[索引号]

切片：长的和索引很像，列表[开始:结束 + 1],偷懒方法，就是写一半
切片还有一个参数，和range很像(开始，结束，步长)

'''

# 在一个未知的列表中有1000个元素，请你取出这一千个元素的最后200个元素
old_list = list(range(1000))
new_list = []

# for i in range(-200, 0):  # 为了提供索引号
#     new_list.append(old_list[i])
# print(new_list)

print(old_list[-200:])

test_list = list(range(10))
print(test_list[0:7:2])

# 这个可以实现列表的逆序
print(test_list[::-1])

'''
算术运算符：+ - * / // % **
比较运算符：> < >= <= != ==
如果出现字符串，或者列表之间进行比较，那么不是看和，不是看差，
'''
list11 = [123, 456]
list22 = [156]
print(list11 > list22)

'''
字符串学过一个操作，+：拼接
列表里面有一个拼接extend()
'''
print(list22 + list11)

'''
乘法：重复操作符
'''
print(list11 * 27)

'''
in / not in  也是一个操作符 ：用来判断元素在不再列表内
in / not in 只能判断一层列表内的元素
'''
list_in = ['pig', 'dog', 'fish', ['people']]
print("people" in list_in)
print("people" not in list_in)


list_ig = [1 , 1, 2, 3, 4, 4, 6, 7]

print(list_ig.count(1))

print(list_ig.index(1))

list_ig.reverse()
print(list_ig)

list_sort = [3, 4, 7, 2, 5, 9]
list_sort.sort(reverse=True)
print(list_sort)