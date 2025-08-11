# 爬取星巴克图片案例
from bs4 import BeautifulSoup
import urllib.request


url = 'https://www.starbucks.com.cn/menu/'

resp = urllib.request.urlopen(url)
context = resp.read().decode('utf-8')
soup = BeautifulSoup(context,'lxml')
# obj = soup.select("ul[class='grid padded-3 product'] div[class='preview circle']")
# for item in obj:
#     completePicUrl = 'https://www.starbucks.com.cn'+item.attrs.get('style').split('url("')[1].split('")')[0]
#     print(completePicUrl)

obj =soup.select_one("div[id='nav-overlay'] ul")
a_tag=obj.find_all("a")
for item in a_tag:
    text = item.get_text(strip=True)
    print(text)



# 爬取证券之光板块信息案例
from bs4 import BeautifulSoup
import urllib.request


url = 'http://quote.stockstar.com/'
context = urllib.request.urlopen(url).read().decode('gb2312')
soup = BeautifulSoup(context,'lxml')
list = soup.select('#datalist2 .align_left a')
for item in list:
    print(item.get_text())
