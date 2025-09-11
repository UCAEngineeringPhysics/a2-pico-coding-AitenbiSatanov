from machine import Pin, PWM
from time import sleep, ticks_ms

# SETUP

led = PWM(Pin(15, Pin.OUT))
led.freq(1000)

button = Pin(14, Pin.IN, Pin.PULL_UP)

mode = 1  
last_time = 0
debounce_time = 200 

# LOOP

def button_handler(pin):
    global mode, last_time
    now = ticks_ms()
    if now - last_time > debounce_time:
        if button.value() == 1: 
            mode = 2 if mode == 1 else 1
        last_time = now

button.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=button_handler)

def fade_cycle():
    steps = 1000
    step_delay = 2 / steps

    for duty in range(steps + 1):
        if mode != 1:
            return
        led.duty_u16(int(duty * 65535 / steps))
        sleep(step_delay)

    for duty in range(steps, -1, -1):
        if mode != 1:
            return
        led.duty_u16(int(duty * 65535 / steps))
        sleep(step_delay)

while True:
    if mode == 1:
        fade_cycle()
    else:
        led.duty_u16(65535)
        sleep(0.05)
