# Chrome-headless 模式， Google 针对 Chrome 浏览器 59版 新增加的一种模式，可以让你不打开UI界面的情况下使用 Chrome 浏览器，所以运行效果与 Chrome 保持完美一致。


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable‐gpu')
# 设置为自己chrome浏览器.exe的系统路径
path = r'C:\Users\99593\AppData\Local\Google\Chrome\Application\chrome.exe'
chrome_options.binary_location = path
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.get('https://www.baidu.com')
# browser.save_screenshot('baidu.jpg')
