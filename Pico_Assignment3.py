from machine import Pin, PWM
from time import sleep
import time

# Initilization Setup
led_red = Pin(15, Pin.OUT)
led_green = Pin(14, Pin.OUT)
led_blue = Pin(13, Pin.OUT)

button = Pin(12, Pin.IN, Pin.PULL_DOWN)

duration_ms = 2000  # 5 seconds
start_time = time.ticks_ms()

# Initilization Loop
def initilization(pin):
    while time.ticks_diff(time.ticks_ms(), start_time) < duration_ms:
        if button.value() == 0:
            led_red.toggle()
            led_green.toggle()
            led_blue.toggle()
        sleep(0.2)
        time.sleep_ms(100)

led_red_PWM = PWM(Pin(15, Pin.OUT))
led_red_PWM.freq(1000)

led_green_PWM = PWM(Pin(14, Pin.OUT))
led_green_PWM.freq(1000)

led_blue_PWM = PWM(Pin(13, Pin.OUT))
led_blue_PWM.freq(1000)

button = Pin(12, Pin.IN, Pin.PULL_DOWN)

pause_mode = 1
work_mode = 0

def loop(pin):
    while True:
        current_button_state = button
        
        if pause_mode == True and work_mode == False:
            for duty in range(65536):
                led_green_PWM.duty_u16(duty)
                sleep(0.0001)
            for duty in range(65536, 0, -1):
                led_green_PWM.duty_u16(duty)
                sleep(0.0001)
        time.sleep_ms(50)
        current_button_state = button
    


    
