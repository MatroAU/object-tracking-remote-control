# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-ssd1306-oled-micropython/
import time
from machine import Pin, SoftI2C
import ssd1306

# 4 VCC 5 GND
VCC = Pin(4, Pin.OUT)
GND = Pin(5, Pin.OUT)
VCC.value(1)
GND.value(0)

time.sleep(.2)

#You can choose any other combination of I2C pins
i2c = SoftI2C(scl=Pin(3), sda=Pin(2))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Hello, World 1!', 0, 0)
oled.text('Hello, World 2!', 0, 10)
oled.text('Hello, World 3!', 0, 20)

oled.show()