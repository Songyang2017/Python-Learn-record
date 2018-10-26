# 循环
# python中两种循环，一种for in循环，遍历list和tuple
a = ['M', 'B', 'K'];
for x in a:
	print(x)
# M
# B
# K

# for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句
sum = 0
for j in [1,2,3,4,5,6,7,8,9,10]:
	sum+=j
print('1到10相加：', sum)

# 若要计算1到100的和可以使用python提供的range()函数，再使用list()将其转换为list
# range()可以生成一个整数序列；range(5)生成的序列是从0开始小于5的整数
list(range(5))	#[0, 1, 2, 3, 4]

sum = 0
for k in list(range(101)):
	sum+=k
print('1到100相加：', sum)


# while循环 只要条件满足，就不断循环，条件不满足时退出循环
sum = 0
n = 99
while n > 0:
	sum+=n
	n-=2
print('100以内所有奇数之和', sum)

# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
for x in L:
	print('Hello ', x)


# break 退出循环，提前结束循环
n = 1
while n<=100:
	n = n + 1
	print(n)
	if n > 15:
		break
print('End ', n)


# continue 提前结束本轮循环，进入下一轮循环
n = 0
while n<20:
	n = n + 1
	if n%2 == 0:	# 如果n为偶数，则不再向下执行，直接进入下一轮循环
		continue
	print(n)	#打印出20内的奇数


# 死循环
n = 1
while n>0:
	n = n + 1
	print(n)