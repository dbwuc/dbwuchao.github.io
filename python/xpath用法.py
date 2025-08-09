# @Author: Achang
# @Time: 2022/2/11 16:27
# @File: lxml_解析站长素材图片
# @Project: 爬虫基础

# https://sc.chinaz.com/tupian/shuaigetupian.html

import urllib.request
import lxml.etree



headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}


def create_request(page):
    if page == 1:
        url = "https://sc.chinaz.com/tupian/shuaigetupian.html"
    else:
        url = "https://sc.chinaz.com/tupian/shuaigetupian_"+str(page)+".html"

    print(url)
    requestObj = urllib.request.Request(headers=headers,url=url)
    return requestObj


def get_context(requestObj):
    context = urllib.request.urlopen(requestObj)
    result = context.read().decode('utf-8')
    return result


def down_load(context):
    tree = lxml.etree.HTML(context)
    name_list = tree.xpath("//div[@id='container']//a/img/@alt")
    pic_url_list = tree.xpath("//div[@id='container']//a/img/@src2")
    for index in range(len(name_list)):
        urllib.request.urlretrieve(url="https:"+pic_url_list[index],filename="./img/"+name_list[index]+'.jpg')


if __name__ == '__main__':
    start_page = int(input("请输入起始页"))
    end_page = int(input("请输入结束页"))

    for page in range(start_page,end_page+1):
        requestObj = create_request(page)
        context = get_context(requestObj)
        down_load(context)
