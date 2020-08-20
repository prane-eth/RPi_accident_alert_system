from selenium import webdriver
from time import sleep

print('started to send sms')
ch_op = webdriver.ChromeOptions()
# ch_op.add_argument('--headless')
driver = webdriver.Chrome( '/usr/lib/chromium-browser/chromedriver',
    chrome_options=ch_op )
driver.get("https://www.way2sms.com/")
driver.find_element_by_id('mobileNo').send_keys('6302523157')
driver.find_element_by_id('password').send_keys('C2484R')
driver.find_element_by_class_name('btn-theme-sm').click()
sleep(2)
driver.find_element_by_id('mobile').send_keys('8367458273')
driver.find_element_by_id('message').send_keys("Accident alert")
driver.find_element_by_id('sendButton').click()
driver.get("https://www.way2sms.com/Logout")
print("Sent")
#driver.quit()
