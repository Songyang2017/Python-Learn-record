from urllib import request

hua = request.urlopen('https://c.y.qq.com/musichall/fcgi-bin/fcg_yqqhomepagerecommend.fcg?_=1558791812975&g_tk=129102238&uin=1546302993&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1')
f = open('./4.json', 'w+', encoding="utf8")
data = hua.read().decode('utf-8')
print(hua.headers.__dict__)
f.write(data)
f.close()
