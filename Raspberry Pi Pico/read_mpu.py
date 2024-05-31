import machine
from machine import Pin
import time
import MPU6050
from machine import Pin, SoftI2C
import ssd1306


# Set up the I2C interface OLED
# 4 VCC 5 GND
VCC = Pin(4, Pin.OUT)
GND = Pin(5, Pin.OUT)
VCC.value(1)
GND.value(0)

time.sleep(.2)

#You can choose any other combination of I2C pins
i2c = SoftI2C(scl=Pin(3), sda=Pin(2))

#oled_width = 128
#oled_height = 64
#oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


# Set up the MPU6050 class 
i2c2 = machine.I2C(1, sda=machine.Pin(10), scl=machine.Pin(11))
mpu = MPU6050.MPU6050(i2c2)


# 13 VCC 12 GND
VCC = Pin(13, Pin.OUT)
GND = Pin(12, Pin.OUT)
VCC.value(1)
GND.value(0)
time.sleep(.2)

# wake up the MPU6050 from sleep
mpu.wake()
smooth = 0
# continuously print the data

    
num_samples = 100  # adjust as required

gyro_sum_x = 0
gyro_sum_y = 0

# continuously print the data
# continuously print the data
while True:
    for i in range (num_samples):
        gyro = mpu.read_accel_data()
        gyro_sum_x += gyro[0]
        gyro_sum_y += gyro[1]
        
    average_gyro_x = gyro_sum_x / num_samples
    average_gyro_y = gyro_sum_y / num_samples
    print(str(average_gyro_x) + "|" + str(average_gyro_y))
    #oled.text(str(average_gyro),0,20)
    #oled.show()
    time.sleep(.5)
    #oled.fill(0)
    gyro_sum_x = 0
    gyro_sum_y = 0
