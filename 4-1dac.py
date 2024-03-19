import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = [6, 12, 5, 0, 1, 7, 11, 8]
GPIO.setup(dac, GPIO.OUT)
def db(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]
try:
    while True:
        num = input()
        if num == 'q':
            break
        if int(num)==False or int(num) > 255 or int(num) < 0:
            print('Неверный ввод')
        val = db(int(num))
        GPIO.output(dac[::-1], val)
        print(val)
        voltage = 0
        for i in range(len(val)):
            voltage += val[i]/(2**(i+1))*3.3
        print(voltage)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()