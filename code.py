import time
from machine import Pin, ADC, PWM
from neopixel import NeoPixel

strip = NeoPixel(Pin(28),15)

buzzer = PWM(Pin(13))

buzzer.freq(1000)

buzzer.duty_u16(10000)

time.sleep(1)

buzzer.duty_u16(0)

strip[0] = (255, 0, 0)

strip.write()