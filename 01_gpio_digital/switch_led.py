import RPi.GPIO as GPIO

LED_PIN = 5
SWITCH_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN , GPIO.OUT)
GPIO.setup(SWITCH_PIN , GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try : 
    while True : 
        val = GPIO.input(SWITCH_PIN) #누르지 않았을때 0 눌었을때 1
        print (val)
        GPIO.output(LED_PIN, val) #GPIO.HIGH = 1
finally : 
    GPIO.cleanup()
    print('cleanup and exit')