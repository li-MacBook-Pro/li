import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print('------欢迎使用翻译小助手--------')
chn = input('请输入需要翻译的英文：')
url = 'https://fanyi.baidu.com/translate#en/zh/' + chn
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
browser = webdriver.Chrome(options=chrome_options)
browser.get(url)
browser.implicitly_wait(10)
d = browser.find_element_by_xpath('//*[@id="main-outer"]/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/p[2]/span').text
print(d)