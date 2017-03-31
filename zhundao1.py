import requests
import re
import time

headers = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Content-Length':'169',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'User=userid=131948',  # change your id 
    'Host':'m.zhundao.net',
    'Origin':'http://m.zhundao.net',
    'Referer':'http://m.zhundao.net/Activity/SubmitActivity/9769',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
    }

data = {
    'ActivityId':'9769',  # date
    'UserName':'1',  # your name
    'Mobile':'11111111111',  # your mobile
    'Company':'3',  # school
    'Depart':'4',  # college
    'Remark':'',  # class
    'ExtraInfo':'',
    'X-Requested-With':'XMLHttpRequest',
    }

url = 'http://m.zhundao.net/Activity/PstSumitActivity'

r1 = r'操作成功'
r2 = r'人数已经达到!'

while 1:
    html = requests.post(url,headers=headers,data=data,timeout=5)
    if re.findall(r1,html.text):
        print(html.text)
        break
    else:
        print('尚未开始')
        time.sleep(0.5)


        
