from RPi import GPIO as gpio
import time

def to_bin(x):
    return [int(i) for i in '0' * (8 - len(bin(x)[2:])) + bin(x)[2:]]

def num2dac(x):
    s = to_bin(x)
    gpio.output(dac, s)
    return s

def adc(u):
    return u / levels * maxv


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
        for value in range(256):
            time.sleep(0.00099)
            signal = num2dac(value)
            voltage = adc(value)
            comp_value = gpio.input(comp)
            if comp_value == 1:
                print('adc value = ', value, ' -> ', signal, ', input voltage = ', round(voltage, 2), sep='')
                break
except KeyboardInterrupt:
    print('the program was stopped by the keyboard')
else:
    print('no exceptions')
finally:
    gpio.output(dac, gpio.LOW)
    gpio.cleanup()
