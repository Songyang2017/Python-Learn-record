### 条件判断	
参考来源：[廖雪峰](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431675624710bb20e9734ef343bbb4bd64bcd37d4b52000)
[菜鸟教程](http://www.runoob.com/python3/python3-basic-operators.html)
```pyrhon
age = 5
```
根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。如果判断是else，则去执行else  
####注意不要少写了冒号 :
```pyrhon
if age>30:
	print('your age is', age)
	print('adult')
else:
	print('get out kid!')
```

if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else，不再向下执行了
```pyrhon
if age<10:
	print('little kid')
elif age>20:
	print('new age')
else:
	print('tennager')
```

新式写法，只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
```pyrhon
if 1:
	print('True')
```


结合input学习：
input返回的数据类型是str, 如果和数字比较，需要使用int()或float()将其转为数字（参数必须是数字字符串）
```pyrhon
inp = input('birth is: ')

if int(inp)>2000:
	print('00后')
elif int(inp)>1900:
	print('90后')
else:
	print('不考虑')
```

计算BIM指数
```pyrhon
h = input('身高：')
w = input('体重：')

bim = float(w)/float(h)**2

if bim<=18.5:
	print('BIM指数是：',bim,' 过轻')
elif bim>18.5 and bim<=25:
	print('BIM指数是：',bim,' 正常')
elif bim>25 and bim<=28:
	print('BIM指数是：',bim,' 过重')
elif bim>28 and bim<=32:
	print('BIM指数是：',bim,' 肥胖')
else:
	print('肥胖')
```