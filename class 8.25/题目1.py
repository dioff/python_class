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
