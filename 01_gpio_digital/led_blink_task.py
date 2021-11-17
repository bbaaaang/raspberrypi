import RPi.GPIO as GPIO
import time

LED_PIN_1 = 4
LED_PIN_2 = 17
LED_PIN_3 = 26
GPIO.setmode(GPIO.BCM) # GPIO.BCM or GPIO.BOARD
GPIO.setup(LED_PIN_1, GPIO.OUT) # GPIO.OUT or GPIO.IN
GPIO.setup(LED_PIN_2, GPIO.OUT)
GPIO.setup(LED_PIN_3, GPIO.OUT)

GPIO.output(LED_PIN_1, GPIO.HIGH) #1
print("led on")
time.sleep(2)
GPIO.output(LED_PIN_1, GPIO.LOW) #0
print("led off")
GPIO.output(LED_PIN_2, GPIO.HIGH) #1
print("led on")
time.sleep(2)
GPIO.output(LED_PIN_2, GPIO.LOW) #0
print("led off")
GPIO.output(LED_PIN_3, GPIO.HIGH) #1
print("led on")
time.sleep(2)
GPIO.output(LED_PIN_3, GPIO.LOW) #0
print("led off")
    
GPIO.cleanup() #GPIO 핀 상태 초기화