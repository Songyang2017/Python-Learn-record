# python有很多内置函数，可参见：https://docs.python.org/3/library/functions.html
# abs() 取绝对值，有且只有一个参数

# max()可以接收多个参数，返回最大的那个，相反min()返回最小的
max(1,2,23,54,-534) #54

int('123')
# 123
int(12.34)
# 12
float('12.34')
# 12.34
str(1.23)
# '1.23'
str(100)
# '100'
bool(1)
# True
bool('')
# False

# 函数名就是一个指向一个函数的引用，可以将函数名赋给一个变量
a = abs
a(-34)
# 34


# len(s)
# Return the length (the number of items) of an object. The argument may be a sequence 
# (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, 
# set, or frozen set).
len([1,2,3,4,5,6]) #list
# 6
len((1,2,3,4)) #tuple
# 4
len('dafsfs') #string
# 6

# range(start, end, step)
