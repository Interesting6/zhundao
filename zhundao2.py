# cancel

import requests
import re
import time

headers = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Content-Length':'0',
    'Cookie':'User=userid=131948',  # change your id 
    'Host':'m.zhundao.net',
    'Origin':'http://m.zhundao.net',
    'Referer':'http://m.zhundao.net/Activity/JoinActivityDetail/10843', # change
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
    }

url = 'http://m.zhundao.net/activity/cancelJoin/10843'
wb_data = requests.post(url,headers=headers,timeout=5)
print(wb_data.text)
