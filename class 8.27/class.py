# 字符串s1=‘ABC’，字符串s1=‘ABC’，要求：生成序列 A1 A2 A3 B1 B2 B3 C1 C2 C3
s1 = 'ABC'
s2 = '123'
list1 = []
for i in s1:
    for j in s2:
        list1.append(i + j)
print(list1)

# 打印九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}x{}={}\t'.format(j, i, i*j), end='')
#     print()

s1 = '123456789'
for i in s1:
    num1 = eval(i)
    for k in range(1, num1 + 1):
        print('{} x {} = {}\t'.format(k, i, i*k), end=' ')
    print()
            
        
    










