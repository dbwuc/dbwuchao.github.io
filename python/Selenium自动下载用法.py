##################chrome
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager

# # 配置Chrome启动参数
# chrome_options = Options()
# chrome_options.add_argument("--headless")        # 无头模式
# chrome_options.add_argument("--disable-gpu")     # 禁用GPU（Windows下无头模式建议）
# chrome_options.add_argument("--window-size=1920,1080")

# # 自动下载ChromeDriver，返回可执行文件路径
# driver_path = ChromeDriverManager().install()

# # Selenium 3.x 写法，指定executable_path和options
# browser = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

# try:
#     browser.get("https://www.baidu.com")
#     print("网页标题:", browser.title)
# finally:
#     browser.quit()

#####################Edge  selenum 4版本

# from selenium import webdriver
# from selenium.webdriver.edge.options import Options

# edge_options = Options()
# edge_options.add_argument("--headless")        # 无头模式
# edge_options.add_argument("--disable-gpu")     # 禁用GPU

# driver_path = r"msedgedriver.exe"

# browser = webdriver.Edge(executable_path=driver_path, options=edge_options)

# try:
#     browser.get("https://www.baidu.com")
#     print("网页标题:", browser.title)
# finally:
#     browser.quit()

#######简单用法

# from selenium import webdriver

# edge_driver_path = r"D:\code\dbwuchao.github.io\python\msedgedriver.exe"

# capabilities = {
#     "ms:edgeOptions": {
#         "args": ["--headless", "--disable-gpu"]
#     }
# }

# browser = webdriver.Edge(executable_path=edge_driver_path, capabilities=capabilities)

# browser.get("https://www.baidu.com")
# print(browser.title)
# browser.quit()


###################复杂用法
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

edge_driver_path = r"D:\code\dbwuchao.github.io\python\msedgedriver.exe"
capabilities = {
    "ms:edgeOptions": {
        "args": [
            # "--headless",
            "--disable-gpu",
            "--window-size=1920,1080"
        ]
    }
}

browser = webdriver.Edge(executable_path=edge_driver_path, capabilities=capabilities)

try:
    browser.get("https://www.baidu.com")

    wait = WebDriverWait(browser, 10)  # 最长等10秒

    # 等待搜索框可见且可点击
    input_box = wait.until(
        EC.element_to_be_clickable((By.ID, "kw"))
    )

    # 如果有“同意”按钮之类，可以尝试点击关闭弹窗
    try:
        consent_btn = browser.find_element(By.ID, "s-btn")
        if consent_btn.is_displayed():
            consent_btn.click()
    except:
        pass

    search_keyword = "Python selenium 教程"
    input_box.clear()
    input_box.send_keys(search_keyword)
    input_box.send_keys(Keys.RETURN)

    # 等待搜索结果加载
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.result.c-container h3 a")))

    time.sleep(1)  # 稍微等一会滚动更流畅

    # 滚动到底部
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # 抓取前5条结果
    results = browser.find_elements(By.CSS_SELECTOR, "div.result.c-container h3 a")[:5]

    for i, elem in enumerate(results, 1):
        print(f"{i}. {elem.text}\n   {elem.get_attribute('href')}")

finally:
    browser.quit()

