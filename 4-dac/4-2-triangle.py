import RPi.GPIO as gpio
import time

def to_bin(x):
    return [int(i) for i in '0' * (8 - len(bin(x)[2:])) + bin(x)[2:]]

dac = [8, 11, 7, 1, 0, 5, 12, 6]
gpio.setmode(gpio.BCM)
[gpio.setup(d, gpio.OUT) for d in dac]

try:
    t = float(input('input period: '))
    k = int(input('input times: '))
    c = 0
    for i in range(k):
        while c < 255:
            n = to_bin(c)
            gpio.output(dac, n)
            c += 1
            u = 3.3 / 256 * int(c)
            print(u)
            time.sleep(t/256/2)
        while c > 0:
            n = to_bin(c)
            gpio.output(dac, n)
            c -= 1
            u = 3.3 / 256 * int(c)
            print(round(u, 3))
            time.sleep(t/256/2) 
finally:
    gpio.output(dac, 0)
    gpio.cleanup()
