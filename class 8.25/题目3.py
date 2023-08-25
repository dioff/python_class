list1 = [11, 53, 40, 45, 27, 16, 28, 99]
list2 = []
for i in list1:
    if i % 3 == 0 and i % 2 != 0:
        list2.append(i)
print(list2)