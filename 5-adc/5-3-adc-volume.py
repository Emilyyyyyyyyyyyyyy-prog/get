from RPi import GPIO as gpio
import time

def to_bin(x):
    return [int(i) for i in '0' * (8 - len(bin(x)[2:])) + bin(x)[2:]]

def num2dac(x):
    s = to_bin(x)
    gpio.output(dac, s)
    return s

def adc():
    res = 0
    now = 0
    for i in range(bits):
        p = 2 ** (bits - i - 1)
        now = res + p
        s = to_bin(now)
        gpio.output(dac, s)
        time.sleep(0.005)
        comp_value = gpio.input(comp)
        if comp_value == 0:
            res += p

    return res


dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]

bits = len(dac)
levels = 2 ** bits
maxv = 3.3
comp = 14
troyka = 13
gpio.setmode(gpio.BCM)
gpio.setup(leds, gpio.OUT)
gpio.setup(dac, gpio.OUT, initial=gpio.LOW)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

try:
    while True:
        value = adc()
        voltage = value / levels * maxv
        if value / 253 > 1:
            lamps = [1, 1, 1, 1, 1, 1, 1, 1]
        elif value / 224 > 1:
            lamps = [1, 1, 1, 1, 1, 1, 1, 0]
        elif value / 192 > 1:
            lamps = [1, 1, 1, 1, 1, 1, 0, 0]
        elif value / 160 > 1:
            lamps = [1, 1 ,1 ,1, 1, 0, 0, 0]
        elif value / 128 > 1:
            lamps = [1, 1, 1, 1, 0, 0, 0, 0]
        elif value / 96 > 1:
            lamps = [1, 1, 1, 0, 0, 0, 0, 0]
        elif value / 64 > 1:
            lamps = [1, 1, 0, 0, 0, 0, 0, 0]
        elif value / 32 > 1:
            lamps = [1, 0, 0, 0, 0, 0, 0, 0]
        else:
            lamps = [0, 0, 0, 0, 0, 0, 0, 0]
        gpio.output(leds, lamps)
        
        
except KeyboardInterrupt:
    print('the program was stopped by the keyboard')
else:
    print('no exceptions')
finally:
    gpio.output(dac, gpio.LOW)
    gpio.cleanup()
