import time,random
from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://www.huya.com/shege')
loginBtn=driver.find_element_by_id('nav-login')
loginBtn.click()
time.sleep(10)

while True:
    input_text=driver.find_element_by_id('pub_msg_input')
    test_arr=['666','哈哈哈','???']
    random_index=random.randint(0,len(test_arr)-1)
    input_text.send_keys(test_arr[random_index])
    time.sleep(3)
    send_btn=driver.find_element_by_id('msg_send_bt')
    send_btn.click()
    time.sleep(7)