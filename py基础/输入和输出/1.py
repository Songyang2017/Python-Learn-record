# str() 返回用户易读
# repr() 返回解释器易读

import math
s = 'Hello Shasha!'
print('str():', str(s))
print('repr():', repr(s))

x = 1.25 * 10
y = 100 * 300
s = "x的值为：" + str(x)+", y的值为："+repr(y)+"...."
print(s)

# range(start, stop, step) 用于创建整数列表，一般用于for循环中
# start 计数开始，默认从0开始，range(5)等价range(0, 5)
# stop 结束，不包含stop
# step 步数，默认为1
s2 = range(1, 11)
print(s2[-1])

for x in s2:
    print('s2：', x)

print('-----------')

s3 = range(0, 20, 3)
for x in s3:
    print('s3：', x)

print('-----------平方表-立方表-1')

for x in range(1, 15):
    print(str(x).rjust(2), str(x*x).rjust(5), repr(x*x*x).rjust(5))

print('-----------平方表-立方表-2')
for x in range(1, 15):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# str.format()方法
# {}及里面的字符会被format()中参数替换，{}中数字用于指向传入对象在format()中位置
print('-----------format()---1')
print('{0} 和 {1}'.format(1, 2))

# 若传入format中的对象使用了关键字，则值会指向使用该名字的参数
print('-----------format()---2')
print('名字：{name} 年龄：{age}'.format(name='莎拉', age=29))

# 位置和关键字参数可混用
print('-----------format()---2')
print('{desc}：{0} {1}'.format(105, 179, desc='体重身高'))

print('-----------math--pi-')
print('常量PI近似值：{}.'.format(math.pi))
print('常量PI近似值：{!r}.'.format(math.pi))
# 冒号:和格式标识符可以跟字段名，对值进行更好的格式化
print('-----------冒号:-')
print('常量PI保留3位小数：{0:.3f}'.format(math.pi))  # 保留3位小数

# 冒号:传入整数可以保证区域宽度，用于美化表格
table = {'name': '张三', 'sort': 3, 'score': 92}
print(table.items())

print('name: {0[name]}, sort: {0[sort]}, score: {0[score]}'.format(table))
# 在 table 变量前使用 '**'
print('name: {name:2}, sort: {sort:2} ,score: {score:2}'.format(**table))
for key, value in table.items():
    # print(key, value)
    print('{0:5} ===> {1:5}'.format(key, value))

# 读取键盘
print('--------读取键盘----')
str1 = input('请输入：')
print('您输入的值是', str1)
