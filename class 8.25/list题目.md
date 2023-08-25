# list题目

**题目一：**

给定一个列表，求最大值，最小值，平均值， 求和：例如l列表为[10, 20, 25, 45, 50, 55, 13, 23]

解析一下这道题：

- 求最大值，最小值，其实就是那列表的元素去和其他元素进行判断即可
- 求和求平均值，太简单了就不说了

```python
ls = [10, 20, 25, 45, 50, 55, 13, 23]

# 最大值
max = ls[0]
for i in ls:
    if i > max:
        max = i
print("最大值为：", max)

# 最小值
min = max
for i in ls:
    if i < min:
        min = i
print("最小值为：", min)

# 平均值
avg = 0
for i in ls:
    avg += i
print("平均值为：", avg/len(ls))

sum = 0
for i in ls:
    sum += i
print("和为：", sum)
```



题目二：

***对列表L=[1,3,5,7,9],利用分片，创建一个新的列表，没有值3，即L2=[1,5,7,9]***

提示：利用切片

```python
L = [1, 3, 5, 7, 9]
L2 = L[0:1] + L[2:]
print(L2)
```

题目三：

**已知一个数字列表[11, 53, 40, 45, 27, 16, 28, 99]，打印列表中所有能被3整除但是不能被2整除的数**

```python
list1 = [11, 53, 40, 45, 27, 16, 28, 99]
list = []
for x in list1:
    if x % 3 == 0 and x % 2 != 0:
        list.append(x)
print(list)
```

题目四：

**已知一个数字列表 [10, 20, 5, 34, 90, 8]，统计列表中十位数是`1`的数的个数**

提示:利用算术操作符得到十位的数字

```python
list1 = [10, 20, 5, 34, 90, 8]
count = 0
for x in nums:
    if x // 10 % 10 == 1:
        count +=1
print(count)

```

