from time import sleep
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.IN)
while True:
    if GPIO.input(12):
        GPIO.output(11,True)
    else:
        GPIO.output(11,False)
    
