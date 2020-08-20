from os import system
### import gpiozero

from mpu6050 import mpu6050
sensor = mpu6050(0x68)

def accel():
    accelerometer_data = sensor.get_accel_data()
    return accelerometer_data['y']

def read():
        f= open("./cont.txt")
        return f.read()

while True:
    print(accel())
    if accel() < -15:
        system("echo 1 > ./acc.txt")
        print("accident accel")
        break
    if '1' not in read():
        #print("exit")
        break
        #exit()
