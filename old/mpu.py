from mpu6050 import mpu6050
sensor = mpu6050(0x68)

while True:
    if sensor.get_accel_data()['y'] <=-3:
        print('end')
        break




