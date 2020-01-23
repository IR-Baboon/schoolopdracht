import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

tilt = 16
buzz = 20

GPIO.setup(tilt, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzz, GPIO.OUT)

def alert(ev=None):
    print("Tilt Detected")
    GPIO.output(buzz, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(buzz, GPIO.LOW)
    time.sleep(1)

def loop():
    GPIO.add_event_detect(tilt, GPIO.BOTH, callback=alert, bouncetime=100) 
    while True:
        pass   

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt: 
        GPIO.cleanup()