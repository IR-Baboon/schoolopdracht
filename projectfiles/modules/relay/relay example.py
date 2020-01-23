import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

relay = 18

GPIO.setup(relay, GPIO.OUT)

try:
    GPIO.output(relay, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(relay, GPIO.LOW)
finally:
    GPIO.cleanup()