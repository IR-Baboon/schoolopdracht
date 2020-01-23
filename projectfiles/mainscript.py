import RPi.GPIO as GPIO
import time
import datetime
import Adafruit_DHT
from mfrc522 import SimpleMFRC522
from modules.screen import lcddriver
from keypad import keypad

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

DHT11_pin = 12
relay = 18
LRD = 24
PIR = 23
tilt = 16
buzz = 20

kp = keypad(columnCount = 4)
display = lcddriver.lcd()
reader = SimpleMFRC522()
sensor = Adafruit_DHT.DHT11
humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT11_pin)
GPIO.setup(relay, GPIO.OUT)
GPIO.setup(LRD, GPIO.IN)
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(tilt, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzz, GPIO.OUT)

def long_string(display, text = '', num_line = 1, num_cols = 20):
        """ 
        Parameters: (driver, string to print, number of line to print, number of columns of your display)
        Return: This function send to display your scrolling string.
        """
        if(len(text) > num_cols):
            display.lcd_display_string(text[:num_cols],num_line)
            time.sleep(1)
            for i in range(len(text) - num_cols + 1):
                text_to_print = text[i:i+num_cols]
                display.lcd_display_string(text_to_print,num_line)
                time.sleep(0.2)
            time.sleep(1)
        else:
            display.lcd_display_string(text,num_line)

def light():
    if GPIO.input(LRD) == 1:
        GPIO.output(relay, GPIO.LOW)
    elif GPIO.input(LRD) == 0:
        GPIO.output(relay, GPIO.HIGH)

while True:
    long_string(display, '*C={0:0.1f} Hum={1:0.1f}%'.format(temperature, humidity), 1)
    display.lcd_display_string(str(datetime.datetime.now()), 2)
    if GPIO.input(PIR):
        light()
        display.lcd_display_string("Greetings!       ", 1)
        display.lcd_display_string("                     ", 2)
        time.sleep(1)
        display.lcd_display_string("What may I serve", 2)
        time.sleep(0.2)
        display.lcd_display_string("What may I serve",1)  
        time.sleep(0.2)
        display.lcd_display_string("Your Choice:                 ", 2)
        seq = []
        for i in range(2):
            digit = None
            counter = 0
            while digit == None:
                digit = kp.getKey()
                counter += 1
                time.sleep(0.1)
                if counter == 600:
                    break
            if counter == 600:
                break
            seq.append(digit)
            choice = ""
            for i in seq:
                choice = choice + str(i)
            display.lcd_display_string("Your Choice: " + str(choice), 2)
            time.sleep(1)
        display.lcd_display_string("press * for yes   ", 1)
        display.lcd_display_string("press # for no    ", 2)
        confirm = None
        if counter < 600:
            counter = 0
            while confirm == None:
                confirm = kp.getKey()
                time.sleep(0.1)
                counter += 1
                if counter == 600:
                    break
        if confirm == '*':
            ## code voor request, choice = productnummer,
            display.lcd_display_string("press * for cash  ", 1)
            display.lcd_display_string("press # for pin   ", 2)
            digit = None
            while digit == None:
                digit = kp.getKey()
            
        elif confirm == '#':
            display.lcd_display_string("                ", 1)
            display.lcd_display_string("cancled         ", 2)
            time.sleep(3)
            display.lcd_clear()
            GPIO.output(relay, GPIO.HIGH)
            continue
        else:
            display.lcd_clear()
            time.sleep(3)
            GPIO.output(relay, GPIO.HIGH)
        