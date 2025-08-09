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


# -------------------ALL------------------------------------

import urllib.request
import http.cookiejar

# 1. 代理服务器配置
proxy = {"http": "http://127.0.0.1:8080", "https": "https://127.0.0.1:8080"}
proxy_handler = urllib.request.ProxyHandler(proxy)

# 2. Cookies 支持，自动管理 Cookies
cookie_jar = http.cookiejar.CookieJar()
cookie_handler = urllib.request.HTTPCookieProcessor(cookie_jar)

# 3. HTTP Basic 认证（需要用户名密码）
auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm=None,
                          uri='http://httpbin.org/basic-auth/user/passwd',
                          user='user',
                          passwd='passwd')

# 4. 自定义重定向处理器（演示用，可不写，因为默认支持）
class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        print(f"重定向被禁止，尝试跳转到: {newurl}")
        return None  # 禁止重定向

redirect_handler = NoRedirectHandler()

# 5. 构建 opener，组合所有 handler
opener = urllib.request.build_opener(
    proxy_handler,
    cookie_handler,
    auth_handler,
    redirect_handler
)

# 6. 构造请求
url = 'http://httpbin.org/basic-auth/user/passwd'
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0')

# 7. 使用 opener 发送请求
try:
    response = opener.open(req)
    print("状态码:", response.status)
    content = response.read().decode('utf-8')
    print("内容:\n", content)
except urllib.error.HTTPError as e:
    print("HTTP错误:", e.code, e.reason)
except urllib.error.URLError as e:
    print("URL错误:", e.reason)

# 8. 打印当前Cookies
print("Cookies:", list(cookie_jar))
