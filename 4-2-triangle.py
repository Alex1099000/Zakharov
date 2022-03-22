import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac=[26,19,13,6,5,11,9,10]
GPIO.setup(dac, GPIO.OUT)
def decimal2binary(value):
    return [int(e) for e in bin(value)[2:].zfill(8)]
i=0
try:
    t=int(input())
    while True:
        time.sleep(t/(2*256))
        GPIO.output(dac,decimal2binary(int(i)))
        if i==255:
            for j in range(255,-1,-1):
                time.sleep(t/(2*256))
                GPIO.output(dac,decimal2binary(int(j)))
            i=0
        else:
            i+=1
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()
