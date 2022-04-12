import RPI.GPIO as GPIO
a=100
f=50
out_pin=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(out_pin, GPIO.OUT)
try:
    p = GPIO.PWM(out_pin, f)
    p.start(a)
    while True:
        a=int(input())
        print("Voltage:",3.3*a/100)


finally:
    GPIO.output(out_pin, 0)
    GPIO.cleanup()
