from time import sleep
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    while True:
        print("Silahkan dekatkan kartu anda")
        id, text=reader.read()
        print("ID: %s\nText: %s" % (id,text))
        sleep(5)
finally:
    GPIO.cleanup()
