#!/usr/bin/python
import smbus
import math
 
# Register
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c
 
def read_byte(reg):
    return bus.read_byte_data(address, reg)
 
def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg+1)
    value = (h << 8) + l
    return value
 
def read_word_2c(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val
 
def dist(a,b):
    return math.sqrt((a*a)+(b*b))
 
def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)
 
def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)
 
bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
address = 0x68       # via i2cdetect
 

bus.write_byte_data(address, power_mgmt_1, 0)
 
print("Gyroscope")
print("--------")
 
G_xout = read_word_2c(0x43)
G_yout = read_word_2c(0x45)
G_zout = read_word_2c(0x47)
 
print("G_xout: ", ("%5d" % G_xout), " skaliert: ", (G_xout / 131))
print("G_yout: ", ("%5d" % G_yout), " skaliert: ", (G_yout / 131))
print("G_zout: ", ("%5d" % G_zout), " skaliert: ", (G_zout / 131))
 
print("")
print("Accelerometer sensor")
print("---------------------")

A_xout = read_word_2c(0x3b)
A_yout = read_word_2c(0x3d)
A_zout = read_word_2c(0x3f)

A_xout_s = 9.81 * A_xout / 16384.0
A_yout_s = 9.81 * A_yout / 16384.0
A_zout_s = 9.81 * A_zout / 16384.0

"""
print("A_xout: ", ("%6d" % A_xout), " skaliert: ", A_xout_skaliert)
print("A_yout: ", ("%6d" % A_yout), " skaliert: ", A_yout_skaliert)
print("A_zout: ", ("%6d" % A_zout), " skaliert: ", A_zout_skaliert)

print("X Rotation: " , get_x_rotation(A_xout_skaliert, A_yout_skaliert, A_zout_skaliert))
print("Y Rotation: " , get_y_rotation(A_xout_skaliert, A_yout_skaliert, A_zout_skaliert))
"""

print("x : "+ str(A_xout_s))
print("y : "+ str(A_yout_s))
print("z : "+ str(A_zout_s))

