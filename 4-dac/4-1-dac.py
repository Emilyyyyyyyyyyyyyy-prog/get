import RPi.GPIO as gpio
import sys

def to_bin(x):
    return [int(i) for i in '0' * (8 - len(bin(x)[2:])) + bin(x)[2:]]


dac = [8, 11, 7, 1, 0, 5, 12, 6]
gpio.setmode(gpio.BCM)
[gpio.setup(d, gpio.OUT) for d in dac]

try:
    while True:
        n = input('input integer between 0 and 256: ')
        if n == 'q':
            print('exit')
            sys.exit(0)
        elif n.count('.') > 0:
            print('float, not integer')
            continue
        elif n.count('-') > 0:
            print('integer must be positive')
            continue
        elif not n.isdigit():
            print('string, not integer')
            continue
        elif int(n) > 255:
            print('integer must be < 256')
            continue
        n = int(n)
        n_bin = to_bin(n)
        for i in range(8):
            gpio.output(dac[i], n_bin[i])
        if n_bin.count(1) == 0:
            u = 0
        else:
            u = round(3.3 / (n_bin.count(1)), 3)
        print('u = ', u, 'v', sep='')
finally:
    gpio.cleanup()
