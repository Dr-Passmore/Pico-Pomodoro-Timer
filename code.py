#imports
import time
from machine import Pin, PWM
from neopixel import NeoPixel

#Pin definitions
strip = NeoPixel(Pin(28),15)
buzzer = PWM(Pin(13))
buzzer_led_on = Pin(17, Pin.OUT)
buzzer_led_off = Pin(18, Pin.OUT)
switch_off = Pin(14, Pin.IN)
switch_mute = Pin(15, Pin.IN)
switch_start = Pin(16, Pin.IN)
switch_meeting = Pin(12, Pin.IN)

buzzer_status = True

def mute():
    '''
    Function mutes the buzzer. 
    buzzer_status is checked and set as opposite the current value.
    '''
    global buzzer_status
    if buzzer_status == True:
        buzzer_status = False
        time.sleep(1)
    else:
        buzzer_status = True
        buzzer.freq(1000)
        buzzer.duty_u16(10000)
        time.sleep(1)
        buzzer.duty_u16(0)
    
    
def off():
    '''Switches off the Pomodoro timer, switching off all leds'''
    strip.fill((0, 0, 0))
    strip.write()
    buzzer.duty_u16(0)
    time.sleep(1)
    
def pomodoro():
    '''
    Pomodoro timer 
    '''
    working_mode = True
    work = 15
    rest = 3
    countdown = work
    while switch_off.value() != 1 or switch_meeting.value() != 0:
        if working_mode == True:
            strip.fill((255, 0, 0))
            strip.write()
            if countdown != 0:
                countdown -= 1
                time.sleep(1)
            else:
                working_mode = False
                countdown = rest
                buzzer.freq(1000)
                buzzer.duty_u16(10000)
                time.sleep(0.5)
                buzzer.duty_u16(0)
        else:
            strip.fill((0, 255, 0))
            strip.write()
            if countdown != 0:
                countdown -= 1
                time.sleep(1)
            else:
                working_mode = True
                countdown = work
                buzzer.freq(500)
                buzzer.duty_u16(10000)
                time.sleep(0.5)
                buzzer.duty_u16(0)
    if switch_off.value() == 1:
        off()
    if switch_meeting.value() == 1:
        meeting()            
                
            #work / 16
        

def meeting():
    print("test")

while True:
    
    if switch_off.value() == 1:
        print("off switch")
    if switch_mute.value() == 1:
        print("mute")
    if switch_start.value() == 1:
        print("start switch")
    
    if buzzer_status == True:
        buzzer_led_on.value(1)
        buzzer_led_off.value(0)
    elif buzzer_status == False:
        buzzer_led_on.value(0)
        buzzer_led_off.value(1)
    while switch_mute.value() == 1:
        mute()
    while switch_start.value() == 1:
        pomodoro()
    while switch_off.value() == 1:
        off()
    time.sleep(0.1)
        
'''
buzzer.freq(1000)


buzzer.duty_u16(10000)

time.sleep(1)

buzzer.duty_u16(0)

strip[0] = (255, 0, 0)

strip.write()

buzzer_led_on.value(1)
buzzer_led_off.value(1)'''

