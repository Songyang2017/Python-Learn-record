f = open('e:/Python/Python-Learn-record/py基础/输入和输出/2.txt', 'r+', encoding="utf8")
# read()读取文件中的内容
# print(f.read())

# readline() 会从文件中读取单独的一行
# print(f.readline())
print('--------1----------')
# readlines() 将返回该文件中包含的所有行。
print(f.readlines())

print('--------2----------')
# 另一种方式是迭代一个文件对象然后读取每行
# for lines in f:
#     print(lines, end='')

print('--------3----------')
# f.write('测试') 返回要写入的字符数
# print(f.write('测试'))

print('--------4----------')
# 如果要写入非字符串，则需现将其转为字符串
# val = ['123', 56]
# num = f.write(str(val))
# print(num)

print('--------5----------')
# print(f.tell())
f.seek(5)
f.close()
