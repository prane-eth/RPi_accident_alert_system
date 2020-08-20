'''from easyprocess import EasyProcess
from pyvirtualdisplay import Display
import pyautogui as pg
from time import sleep

if __name__ == "__main__":
    # start Xephyr
    Display(visible=1, size=(500, 500)).start()
    # start Gnumeric
    EasyProcess('firefox --private-window https://www.way2sms.com/Logout').start()
    while pg.pixel(100,100)[0] != 42 :
        sleep(0.1)
    sleep(1)
    pg.typewrite('6302523157')
    pg.press('tab')
    pg.typewrite('C2484R')
    pg.press('enter')
    while pg.pixel(300,200)[0] != 255 :
        sleep(0.1)
    sleep(2)
    pg.typewrite('8367458273')
    pg.press('tab')
    pg.press('esc')
    pg.typewrite('hello message')
    pg.press('tab')
    #pg.press('enter')'''

from selenium import webdriver
def send_sms(s_txt):
    print('started to send sms')
    ch_op = webdriver.ChromeOptions()
    #ch_op.add_argument('--headless')
    driver = webdriver.Chrome( '/usr/lib/chromium-browser/chromedriver',
        chrome_options=ch_op )
    driver.get("https://www.way2sms.com/")
    driver.find_element_by_id('mobileNo').send_keys('6302863776')
    driver.find_element_by_id('password').send_keys('W5364F')
    driver.find_element_by_class_name('btn-theme-sm').click()
    sleep(2)
    driver.find_element_by_id('mobile').send_keys('7702889979')
    driver.find_element_by_id('message').send_keys("Accident alert here")
    driver.find_element_by_id('sendButton').click()
    sleep(1)
    driver.get("https://www.way2sms.com/Logout")
    print("Sent")
    #driver.quit()
