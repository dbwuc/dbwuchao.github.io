# 基本使用
# import urllib.request
# url="https://www.baidu.com/"
# response = urllib.request.urlopen(url)
# print(response.status)
# print(response.read().decode())


# 请求对象定制
# import urllib.request
# url = 'https://www.baidu.com'
# headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
# }

# requestObj=urllib.request.Request(url, [],headers)

# resp = urllib.request.urlopen(requestObj)
# print(resp.read().decode("utf-8"))


# # 编解码
# import urllib.parse
# import urllib.request

# searchWord = urllib.parse.quote("蝙蝠侠")
# url = 'https://www.sogou.com/web?query='+ searchWord
# headers={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
# }

# print(url)
# requestObj = urllib.request.Request(url=url,headers=headers)
# resp = urllib.request.urlopen(requestObj)
# context = resp.read().decode("utf-8")
# print(context)


# # get请求
# import urllib.parse
# import urllib.request

# data = {
#     'query':'蝙蝠侠',
#     'w':'01019900'
# }

# searchWord = urllib.parse.urlencode(data)
# preUrl = 'https://www.sogou.com/web?'
# url = preUrl+searchWord

# requestObj = urllib.request.Request(url,[],headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"})

# resp = urllib.request.urlopen(requestObj)
# context = resp.read().decode("utf-8")
# print(context)


# # post请求
# #eg:百度翻译  
# 详细翻译https://fanyi.baidu.com/v2transapi

# import urllib.request
# import urllib.parse
# import json
# url = 'https://fanyi.baidu.com/sug'
# headers = {
#     'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
# }
# keyword = input('请输入您要查询的单词')
# data = {
#     'kw':keyword
# }
# data = urllib.parse.urlencode(data).encode('utf-8')
# request = urllib.request.Request(url=url,headers=headers,data=data)
# response = urllib.request.urlopen(request)
# # print(response.read().decode('utf-8'))
# # 遍历输出
# content = response.read().decode('utf-8')
# result = json.loads(content)
# for item in result.get('data', []):
#     print(f"{item['k']} : {item['v']}")


import urllib.parse
import urllib.request
import json

url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Accept':'*/*',
    # 'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection':'keep-alive',
    'Content-Length':'148',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'BIDUPSID=E4EED4AD32F68A0029150518B71E6473; PSTM=1644069814; BAIDUID=E4EED4AD32F68A00C795D774149F4DCE:FG=1; __yjs_duid=1_03f1094640beee76272a007638c459db1644071304166; BDUSS=dsWE1lc0kxbWdZTHNLejFRanNJOVNvZjVQSjJaZnpFWFlIa2t6ZXAyYnhqaWxpSVFBQUFBJCQAAAAAAAAAAAEAAAA0MjAmb285OTU5MzE1NzYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPEBAmLxAQJiR1; BDUSS_BFESS=dsWE1lc0kxbWdZTHNLejFRanNJOVNvZjVQSjJaZnpFWFlIa2t6ZXAyYnhqaWxpSVFBQUFBJCQAAAAAAAAAAAEAAAA0MjAmb285OTU5MzE1NzYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPEBAmLxAQJiR1; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; APPGUIDE_10_0_2=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1644391469,1644461433; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=5; BAIDUID_BFESS=0434881F591F38E40670B2C4E152E2CB:FG=1; H_PS_PSSID=34430_35104_31254_35489_34584_35490_35542_35797_35320_26350_35746; BA_HECTOR=0l0g008g802g8h8ljs1h09avc0r; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1644474869; ab_sr=1.0.1_NjFhODYxOTg3ODkzNmExOThhNGNmZjNkYWQ1MGUyYjgyNWEzMTMzOTcxM2IzY2Q1NDk3ZjE4YzgyZDhlNzIyNTdlYTBhZjY5MTFjOWRiYzgzYTg5ZGExNjQxNGVkM2U1YjQyNzVjMDc4N2M0YTVjYzcyYzAyODMyNjY0MDEyMTM0MTQ4NzllMmFiZTM3MDNlYzY3OTUzMTBmMWE2NzM2YmY5ZDQ5Nzk1NDMzMWI0MWI0ZTg4NDNkNTFmM2M4ZTFm',
    'Host':'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh',
    'sec-ch-ua': '"Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'X-Requested-With': 'XMLHttpRequest'
}
data = {
    'from': 'zh',
    'to': 'en',
    'query': '房子',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '289459.35202',
    'token': '1ee0174682b16644fbbcde79861a56e5',
    'domain': 'common',
}
key = urllib.parse.urlencode(data).encode('utf-8')
requestObj = urllib.request.Request(url,key,headers)
resp = urllib.request.urlopen(requestObj)
context = resp.read().decode('utf-8')
str = json.loads(context)
print(str)

