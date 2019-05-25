from urllib import request
f = open('e:/Python/Python-Learn-record/py基础/输入和输出/3.txt', 'w+', encoding="utf8")
res = request.urlopen(
    'https://photo.qq.com/fcgi-bin/fcg_list_photo?uin=2522450506&albumid=V11uMqwM3dB9pn')
txt = str(res.read())
f.write(txt)
f.close()
