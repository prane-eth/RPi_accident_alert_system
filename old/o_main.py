from os import system

from selenium import webdriver
from time import sleep

import gpiozero

from mpu6050 import mpu6050
sensor = mpu6050(0x68)

import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def log(a_txt):
    system("echo '"+str(a_txt)+"' >> log.txt")

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

def accel():
    accelerometer_data = sensor.get_accel_data()
    return accelerometer_data['y']


def ultr():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def g_log():
    while True:
        log(accel())

def g_log_2():
    x1 = accel()
    x2 = accel()
    return x2-x1


def main():
	start=time.time()
	while True:
	    if time.time()-start>=1:
		print('end')
		break
	    if ultr()>=30 or accel()>4:
		print('danger')
		send_sms('0')
		break
	g_log()
		
		    

main()
