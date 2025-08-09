import urllib.request

url = 'http://www.baidu.com'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}

reqObj = urllib.request.Request(url=url,headers=headers)
handler = urllib.request.HTTPHandler()
opener = urllib.request.build_opener(handler)
resp = opener.open(reqObj)
context = resp.read().decode("utf-8")
print(context)



import random
import urllib.parse
import urllib.request


#随机代理池
proxies_pool = [
    {"http":'61.163.32.88:312811'},
    {"http":'61.163.32.88:3128222'}
 ]

proxies = random.choice(proxies_pool)
print(proxies)


url = 'http://www.baidu.com/s?wd=ip'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}

reqObj = urllib.request.Request(url=url,headers=headers)
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
resp = opener.open(reqObj)
context = resp.read().decode("utf-8")

with open("代理.html",'w',encoding='utf-8') as fp:
    fp.write(context)
