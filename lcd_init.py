from utime import sleep_ms
from machine import Pin, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

I2C_ADDR, *_ = i2c.scan()

lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
