from selenium import webdriver

path = 'phantomjs.exe'
browser = webdriver.PhantomJS(path)

url = 'https://www.baidu.com'
browser.get(url)

# browser.save_screenshot('baidu.jpg')
