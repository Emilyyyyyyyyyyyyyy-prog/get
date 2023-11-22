import RPi.GPIO as gpio
import time
import matplotlib.pyplot as plt

def to_bin(x):
    return [int(i) for i in '0' * (8 - len(bin(x)[2:])) + bin(x)[2:]]

def adc():
    res, temp = 0, 0
    for i in range(8):
        temp = res + 2 ** (7 - i)
        signal = to_bin(temp)
        gpio.output(dac, signal)
        time.sleep(0.005)
        comp_value = gpio.input(comp)
        if comp_value == 0:
            res += 2 ** (7 - i)
    gpio.output(leds, signal)
    return res


gpio.setmode(gpio.BCM)
leds = [2, 3, 4, 17, 27, 22, 10, 9]
gpio.setup(leds, gpio.OUT)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
bits = len(dac)
levels = 2 ** bits
gpio.setup(dac, gpio.OUT, initial=gpio.LOW)
comp = 14
gpio.setup(comp, gpio.IN)
troyka = 13
gpio.setup(troyka, gpio.OUT, initial=gpio.LOW)


try:
    start = time.time()
    c, u = 0, 0
    data = []
    data2 = []
    
    gpio.output(troyka, 1)
    while u < 200:
        u = adc()
        data2.append(u)
        data.append(u / 256 * 3.3)
        print(u, 'voltage:', u / 256 * 3.3)
        c += 1
        gpio.output(leds, to_bin(u))

    gpio.output(troyka, 0)

    while u >= 167:
        u = adc()
        data2.append(u)
        data.append(u / 256 * 3.3)
        print(u, 'voltage:', u / 256 * 3.3)
        c += 1
        gpio.output(leds, to_bin(u))
    
    finish = time.time()
    time_all = finish - start
    print('All time:', time_all)
    print('Period:', time_all / c)

    with open('data.txt', 'w') as f:
        for i in data2:
            f.write(str(i) + '\n')

    with open('settings.txt', 'w') as f:
        f.write('частота дискретизации: ' + str(c / time_all) + '\n')
        f.write('шаг квантования: ' + str(3.3 / 256) + '\n')
    f.close()
    print(c)
    print('Время эксперимента: ', time_all, ', период: ', time_all / c,
     ', частота: ', round(c / time_all, 4), ', шаг квантования: ', round(3.3 / 256, 4), sep='')

    plt.plot(data)
    plt.xlabel('time')
    plt.ylabel('voltage')
    plt.show()
finally:
    gpio.output(leds, 0)
    gpio.output(dac, 0)
    gpio.output(troyka, 0)
    gpio.cleanup()
