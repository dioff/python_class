'''
分支循环:if-else
循环:while - for 
'''
'''
while 条件：
    循环体

for 变量 in 可迭代对象:
    循环体
'''

'''
int  10
str   'nihao'
float 10.1
bool True/False

'''

'''
range(10) --> [0,1,2,3...,9]
for i in range(10):
    print(i)
'''
# a = 0
# while a <= 8:
#     a += 2
#     print(a)


'''for i in range(0, 10, 2):
    print(i)

print('_'*27)

for i in range(1,12,2):
    print(i)
'''
# a=1
# sum = 0
# while a <= 100:
#     sum += a
#     a+=1
# print(sum)

# sum=0
# for a in range(101):
#     sum+=a
# print(sum)

year = 2018
while True:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year)
        break
    year += 1

for a in range(2018,2051):
    if a % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(a)
        break

list1 = [1, 2, 3, 4, 5, 6]
print(type(list1))
# range(0,20)--> [0, 1,2,3,4,5, ... , 19]
for i in list1:
    print(i)


print('_'*27)
list2 = [1, 222, 'niu', 3.14, [1,2,3]]
for i in list2:
    print(i)

print('_'*27)
num = [1, 2, 3]
num.extend([5, 6])
print(num)

num.insert(-1, 0)
print(num)


'''
for 变量 in 可迭代对象:
    循环体
可迭代对象有哪些？ 字符串，列表



'''