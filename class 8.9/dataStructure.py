"""
在之前我们都知道，带了引号的是字符串类型，那么没带引号的呢？
就是数字！
字符串相加称作拼接，数字的相加
下面我们介绍一下数据类型：
整型，浮点型，布尔型，复数型
"""

# 整型就不用解释了，123456789这样不带小数点的数字都是整型

# 浮点型：就是所谓的小数，例如圆周率是3.1415926535；例如光速是3.0 x 10^8  E = mc²

'''
那我们在这里就不得不谈及一下E记法(也就是科学计数法)
'''

a = 0.00000000000000000000025
print(a)
# 会输出2.5e-22，再这里e就表示10

'''
布尔类型： 在python中bool类型只有True和Fasle两种, 例如 1 + 1 > 3是错的,不仅我们知道,程序也知道 
在python中也可以使用1/0来表示True和False，所以我们也可以用来做运算
'''
print(1 + 1 > 3)
# 他会输出False

print(True + True)  
print(True * False)
print("________________________________")

"""
介绍几个与数据类型紧密相关的函数: int(), str(), float()
int():将一个字符串或者浮点数转换成一个整数
str():将一个数或者其他任何类型转换成一个字符串
float():将一个字符串或者一个整数转换成浮点数
"""
num = 1
string = "1"
float1 = 3.141

print(type(num))
print(type(string))
print(type(float1))

print(type(float(num)))
print(type(int(string)))
print(type(str(float1)))

"""
除了使用type来判断数据类型,我们还可以使用什么来判断呢？
isintance()
"""
print("________________________________")
print(isinstance(num, str))
print(isinstance(num, int))
print(isinstance(num, float))
