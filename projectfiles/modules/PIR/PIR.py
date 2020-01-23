import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIR = 23

GPIO.setup(PIR, GPIO.IN)

print('Starting up the PIR Module (click on STOP to exit)')
time.sleep(1)
print ('Ready')

while True:
  if GPIO.input(PIR):
    print('Motion Detected')
    time.sleep(1)