# ajax的get请求
import urllib.parse
import urllib.request
import json

# url = 'https://movie.douban.com/j/chart/top_list?type=19&interval_id=100%3A90&action=&start='+page+'&limit=20'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}


def getjson(page):
    url = 'https://movie.douban.com/j/chart/top_list?type=19&interval_id=100%3A90&action=&start=' + str(
        (page - 1) * 20) + '&limit=20'
    requestObj = urllib.request.Request(url=url, headers=headers)
    resp = urllib.request.urlopen(requestObj)
    context = resp.read().decode('utf-8')
    return context


def download(page, context):
    with open("豆瓣电影_第" + str(page) + "页.json", 'w', encoding='utf-8') as fp:
        fp.write(context)


if __name__ == '__main__':
    start_page = int(input("开始页"))
    end_page = int(input("结束页"))
    for page in range(start_page, end_page + 1):
        context = getjson(page)
        if context != '[]':
            download(page, context)


# ajax的post请求
import urllib.parse
import urllib.request


# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'


def getSearchParams(page,city):
    data = {
        'cname': city,
        'pageIndex': page,
        'pageSize': '10'
    }
    searchParams = urllib.parse.urlencode(data).encode("utf-8")
    return searchParams


def getContext(searchParams):
    reqObj = urllib.request.Request(url=url, headers=headers, data=searchParams)
    resp = urllib.request.urlopen(reqObj)
    context = resp.read().decode('utf-8')
    return context


def download(city,index,context):
    with open("肯德基门店信息_" + city + "_" + str(index)+'.json', 'w', encoding='utf-8') as fp:
        fp.write(context)


if __name__ == '__main__':
    page = int(input("爬取第几页？"))
    city = input("什么城市？")
    for index in range(1,page+1):
        searchParams = getSearchParams(index,city)
        context = getContext(searchParams)
        if context != '[]':
            download(city,index,context)

# URLError\HTTPError


import urllib.request
import urllib.error
url = 'https://blog.csdn.net/ityard/article/details/102646738'
# url = 'http://www.goudan11111.com'
headers = {
        # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed‐exchange;v=b3',
        # 'Accept‐Encoding': 'gzip, deflate, br',
        # 'Accept‐Language': 'zh‐CN,zh;q=0.9',
        # 'Cache‐Control': 'max‐age=0',
        # 'Connection': 'keep‐alive',
        'Cookie': 'uuid_tt_dd=10_19284691370‐1530006813444‐566189;smidV2=2018091619443662be2b30145de89bbb07f3f93a3167b80002b53e7acc61420;ga=GA1.2.1823123463.1543288103; dc_session_id=10_1550457613466.265727;acw_tc=2760821d15710446036596250e10a1a7c89c3593e79928b22b3e3e2bc98b89;Hm_lvt_e5ef47b9f471504959267fd614d579cd=1571329184;Hm_ct_e5ef47b9f471504959267fd614d579cd=6525*1*10_19284691370‐1530006813444‐566189;__yadk_uid=r0LSXrcNYgymXooFiLaCGt1ahSCSxMCb;Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1571329199,1571329223,1571713144,1571799968;acw_sc__v2=5dafc3b3bc5fad549cbdea513e330fbbbee00e25; firstDie=1; SESSION=396bc85c‐556b‐42bd‐890c‐c20adaaa1e47; UserName=weixin_42565646; UserInfo=d34ab5352bfa4f21b1eb68cdacd74768;UserToken=d34ab5352bfa4f21b1eb68cdacd74768;UserNick=weixin_42565646;AU=7A5;UN=weixin_42565646;BT=1571800370777;p_uid=U000000;dc_tos=pzt4xf;Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1571800372;Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=1788*1*PC_VC!6525*1*10_192846913701530006813444566189!5744*1*weixin_42565646;announcement=%257B%2522isLogin%2522%253Atrue%252C%2522announcementUrl%2522%253A%2522https%253A%252F%252Fblogdev.blog.csdn.net%252Farticle%252Fdetails%252F102605809%2522%252C%2522announcementCount%2522%253A0%252C%2522announcementExpire%2522%253A3600000%257D',
        # 'Host': 'blog.csdn.net',
        # 'Referer': 'https://passport.csdn.net/login?code=public',
        # 'Sec‐Fetch‐Mode': 'navigate',
        # 'Sec‐Fetch‐Site': 'same‐site',
        # 'Sec‐Fetch‐User': '?1',
        # 'Upgrade‐Insecure‐Requests': '1',
        'User‐Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/77.0.3865.120 Safari/537.36',
    }
    
try:
    request = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf‐8')
    print(content)
except urllib.error.HTTPError:
    print(1111)
except urllib.error.URLError:
    print(2222)


