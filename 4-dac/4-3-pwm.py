import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(24, gpio.OUT)

try:
    pers = int(input('input %'))
    p = gpio.PWM(24, 1000)
    p.start(pers)
    input('stoppp: ')
    p.stop()
finally:
    gpio.output(24, 0)
    gpio.cleanup()   
