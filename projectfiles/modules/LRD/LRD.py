import RPi.GPIO as GPIO
import time
import Adafruit_DHT


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LRD = 24
relay = 18
DHT11_pin = 12
sensor = Adafruit_DHT.DHT11

GPIO.setup(relay, GPIO.OUT)
GPIO.setup(LRD, GPIO.IN)


def light():
    old_value = not GPIO.input(LRD)
    while True:
        try:
          if GPIO.input(LRD) != old_value:
            if GPIO.input(LRD):
              print ('\u263e')
              GPIO.output(relay, GPIO.LOW)
            else:
              print ('\u263c')
              GPIO.output(relay, GPIO.HIGH)
          old_value = GPIO.input(LRD)
          time.sleep(3)
        except KeyboardInterrupt:
            GPIO.cleanup()

def temp():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT11_pin)
    if humidity is not None and temperature is not None:
        print('Temperature={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading from the sensor. Try again!')
    
light()