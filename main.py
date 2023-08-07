from machine import Pin, I2C, UART
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import time

relay_1 = Pin(2, Pin.OUT)
relay_2 = Pin(3, Pin.OUT)
relay_3 = Pin(4, Pin.OUT)
relay_4 = Pin(5, Pin.OUT)

I2C_ADDR = 0x3E
Row_no = 2
Column_no = 16

i2c = I2C(id = 1, sda = Pin(14), scl = Pin(15), freq = 400000)
lcd = I2cLcd(i2c, I2C_ADDR, Row_no, Column_no)
uart = UART(0, 9600, tx = Pin(0), rx = Pin(1))

lcd.move_to(0, 0)
lcd.putstr("Hello world!")
time.sleep(1)
lcd.clear()
lcd.move_to(0 , 0)
lcd.putstr("BULB:")
lcd.putstr("off")
lcd.move_to(9, 0)
lcd.putstr("FAN:")
lcd.putstr("off")
lcd.move_to(0, 1)
lcd.putstr("Tube:")
lcd.putstr("off")
lcd.move_to(9, 1)
lcd.putstr("Col:")
lcd.putstr("off")

while True:
    if uart.any() > 1:
        data = uart.readline(1)
        print(data)
        if 'B' in data:
            relay_1.value(False)
            lcd.move_to(5, 0)
            lcd.putstr("on ")
        if 'b' in data:
            relay_1.value(True)
            lcd.move_to(5, 0)
            lcd.putstr("off")
        if 'T' in data:
            relay_2.value(False)
            lcd.move_to(5, 1)
            lcd.putstr("on ")
        if 't'in data:
            relay_2.value(True)
            lcd.move_to(5, 1)
            lcd.putstr("off")
        if 'F' in data:
            relay_3.value(False)
            lcd.move_to(13, 0)
            lcd.putstr("on ")
        if 'f' in data:
            relay_3.value(True)
            lcd.move_to(13, 0)
            lcd.putstr("off")
        if 'C' in data:
            relay_4.value(False)
            lcd.move_to(13, 1)
            lcd.putstr("on ")
        if 'c' in data:
            relay_4.value(True)
            lcd.move_to(13, 1)
            lcd.putstr("off")
    
   
    
  
    
    
