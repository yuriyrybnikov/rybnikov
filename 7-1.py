import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
GPIO.setmode(GPIO.BCM)
def decimal2binary(chislo):
    return [int(element) for element in bin(chislo)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

bits= len(dac)

levels = 2**bits

maxVoltage = 3.3

troyka_module = 13

begin_time = time.time()
comp = 14
GPIO.setup(comp,GPIO.IN)
GPIO.setup(troyka_module, GPIO.OUT, initial = GPIO.HIGH)


leds=[9, 10, 22, 27, 17, 4, 3, 2]


GPIO.setup(leds, GPIO.OUT)
cond_voltage = []
time_array = []
time_array.append(0)

def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac,signal)
    return signal
now_time = time.time()
print(now_time)
previous_time = now_time + 0.02
voltage = 0
try:
    while voltage < 2.66:
        now_time = time.time()
        while time.time() - previous_time < 0:
        
            value = 0
            for i in range(8):
                num = int( 2**(7-i))
                value+= num
                signal = num2dac(value)
            
                time.sleep(0.004)
                Comp_val= GPIO.input(comp)
                value-= Comp_val*num
            voltage = value/levels*maxVoltage
            print(value, voltage)
            GPIO.output(leds, decimal2binary(value))
            

        previous_time = time.time() + 0.035
        cond_voltage.append(voltage)
    print(cond_voltage)
    
    data = ['0.001', '5']
    GPIO.setup(troyka_module, GPIO.OUT, initial = GPIO.LOW)
    
    while voltage > 2.17:
        now_time = time.time()
        while time.time() - previous_time < 0:
        
            value = 0
            for i in range(8):
                num = int( 2**(7-i))
                value+= num
                signal = num2dac(value)
            
                time.sleep(0.004)
                Comp_val= GPIO.input(comp)
                value-= Comp_val*num
            voltage = value/levels*maxVoltage
            print(value, voltage)
            GPIO.output(leds, decimal2binary(value))
        previous_time = time.time() + 0.035
        cond_voltage.append(voltage)
    str_arr = [str(items) for items in cond_voltage]
    with open("data1.txt", 'w') as outfile:
        outfile.write('\n'.join(str_arr))        

       


finally:
    
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup(dac)
    GPIO.cleanup(leds)
    t = round(time.time() - begin_time, 2)
    print('Период - 0.01 с')
    print('Частота дискретизации - 0.002 с')
    print('Шаг квантования - 0.013 В')
    print(f'Общее время эксперимента - {t} c')
    str1_arr = ['Период - 0.01 с', 'Частота дискретизации - 0.002 с', 'Шаг квантования - 0.013 В', 't']
    with open("data3.txt", 'w') as outfile:
        outfile.write('\n'.join(str1_arr)) 
    k = 0 
    x = []
    for i in range(len(cond_voltage)):
        x.append(k)
        k += 0.07
    plt.plot(x, cond_voltage)
    plt.show()
    plt.savefig('1.png')
    print(len(cond_voltage))
