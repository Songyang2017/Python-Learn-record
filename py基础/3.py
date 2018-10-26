# python的保留字（关键字），不能用做任何标识符名称
# python标准库提供了一个keyword模块，可以输出当前版本所有关键字

import keyword

print(keyword.kwlist)

'''
以下为输出内容
['False', 'None', 'True', 'and', 'as', 
'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''

# 行与缩进
'''
python的特色是使用缩进来表示代码块，不需要使用{}，缩进的空格数是可变的，
但同一个代码块必须具有相同的空格数
'''

# 多行语句可以使用反斜杠（\）来实现，例如
total = 1 + 2 + \
		3 + 4+ \
		5
print('total：',total)	#totla：15

# 在[], {}, ()中多行语句不需要反斜杠（\）

#数字Number类型：整数，布尔值，浮点数，复数
#int(整数) 1
#bool(布尔) True，False；True为1，False为0；可直接与数字进行加减乘除计算
#float(浮点数) 1.23
#complex(复数) 如1+2j，2+4i

#我们把形如z=a+bi（a,b均为实数）的数称为复数，其中a称为实部，b称为虚部，i称为虚数单位。
# 当虚部等于零时，这个复数可以视为实数；当z的虚部不等于零时，实部等于零时，常称z为纯虚数

# 同行显示多条语句使用分号 ; 隔开
import sys; str = 'hello'


# print输入 默认是换行的，若要不换行需在末尾加上end = ''
print(3, end=' '); print(4,, end=' ')  #3 4
# end='' 引号中可以加上任意想使它们隔开的字符，比如end='-'；则输出'3-4'


# import 和 from...import导入模块
# 将整个模块导入	import someModel
# 将模块中某个函数导入	from someModel import someFunction
# 将模块中多个函数导入	from someModel import someFunction1, someFunction2, someFunction3
# 将模块中全部函数导入	from someModel import *
from sys import argv, path

print('================python from import===================================')
print('path ', path)	#已经引入了path，所以不需要sys.path了

# 查看各参数信息：python -h