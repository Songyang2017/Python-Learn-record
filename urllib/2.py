from urllib import request, parse
import csv
import re

headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}
data = {
	'itemId': 570360894700,
	'sellerId':772687801,
	'order':3,
	'currentPage':1,
	'pageSize': 100,
	'callback': '_DLP_2548_der_3_currentPage_1_pageSize_100_'
}
data = parse.urlencode(data)

req = request.Request('https://rate.tmall.com/list_detail_rate.htm?'+data, headers = headers)

res = request.urlopen(req)

dat = res.read().decode('utf-8')

with open('./data/data.csv', 'w', encoding='utf-8') as f:
    # writer = csv.writer(f)
    # writer.writerow(dat)
    f.write(dat)