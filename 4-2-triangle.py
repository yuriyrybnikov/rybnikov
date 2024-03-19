import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [6, 12, 5, 0, 1, 7, 11, 8]
GPIO.setup(dac, GPIO.OUT)
def db(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]
try:
    T = int(input())
    while True:
        for i in range(255):
            val = db(int(i))
            GPIO.output(dac[::-1], val)
            time.sleep(T/510)
        for i in range(0, 255, -1):
            val = db(int(i))
            GPIO.output(dac[::-1], val)
            time.sleep(T/510)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()