# 定义函数
# Python中定义函数使用def，依次函数名，括号（参数）和冒号，在缩进块中编写函数体，最后返回用 return
# 函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回

def add(x, y):
	return x + y
r = add(3,4)
print('3加4等于：', r)
# 3加4等于：7

def my_abs(x):
	if x>0:
		return x
	else:
		return -x
q = my_abs(-34)
print('q的绝对值：', q)

def x():
	return
print('x()：', x())
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None，return None可以简写为return