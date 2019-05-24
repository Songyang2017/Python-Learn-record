from urllib import request
f = open('e:/Python/Python-Learn-record/py基础/输入和输出/3.txt', 'w+')
res = request.urlopen('https://www.imooc.com/')
txt = str(res.read())
f.write(txt)
f.close()
