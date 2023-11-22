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
bits = len(dac)
levels = 2 ** bits
maxv = 3.3
comp = 14
troyka = 13
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT, initial=gpio.LOW)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

try:
    while True:
        value = adc()
        voltage = value / levels * maxv
        print('adc value = ', value, ' -> ', ', input voltage = ', round(voltage, 2), sep='')
except KeyboardInterrupt:
    print('the program was stopped by the keyboard')
else:
    print('no exceptions')
finally:
    gpio.output(dac, gpio.LOW)
    gpio.cleanup()
