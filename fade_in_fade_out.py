from machine import Pin, PWM, Timer
from time import sleep


# SETUP
from machine import Pin, PWM
from time import sleep

dimmer = PWM(Pin(15))
dimmer.freq(1000)
      
# LOOP

while True:
    for duty in range(76000):
        dimmer.duty_u16(duty)
        sleep(0.0003)
    for duty in range(76000, 0, -1):
        dimmer.duty_u16(duty)
        sleep(0.00005)
