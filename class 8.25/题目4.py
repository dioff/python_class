list1 = [10, 20, 5, 34, 90, 8]
count = 0
for i in list1:
    if i // 10 % 10 == 1:
        count += 1
        print(i)
print(count) 