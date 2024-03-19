import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
p = GPIO.PWM(24, 1000)
p.start(0)
try:
    while True:
        a = float(input())
        p.start(a)
        voltage = a*3.3/100
        print(voltage)
    
finally:
    GPIO.output(24, 0)
    GPIO.cleanup()