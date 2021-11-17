import RPi.GPIO as GPIO
import time

BUZZER_PIN = 5
LED_PIN = 6
SWITCH_PIN = 26
SWITCH_PIN2= 19
SEGMENT_PINS =[25,20,22,17,4,12,18]
DIGIT_PINS =[24,16,20,23]

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN, GPIO.OUT) 
GPIO.setup(SWITCH_PIN , GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

n1 = 0
n2 = 0
n3 = 0
n4 = 0

for segment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)
for digit in DIGIT_PINS:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, GPIO.HIGH)

def display(digit, number): #자리수, 숫자
    for i in range(len(DIGIT_PINS)): #해당하는 자릿수 핀만 LOW 설정
        if i + 1 == digit:
            GPIO.output(DIGIT_PINS[i], GPIO.LOW)
        else:
            GPIO.output(DIGIT_PINS[i], GPIO.HIGH)

    #숫자 출력
    for i in range(len(SEGMENT_PINS)): 
        GPIO.output(SEGMENT_PINS[i], data[number][i])
    time.sleep(0.001)

pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(10)

melody = [391, 391, 440, 440, 391, 391, 329]
melody2 = [391, 391, 329, 329, 293]
melody3 = [391, 329, 293, 329, 261]




try:
    while GPIO.input(SWITCH_PIN2) == 1:
            now = datetime.now()
            n1 = int(((now.hour+8)%24)/10)
            n2 = ((now.hour+8)%24)%10   
            n3 = int(now.minute/10)
            n4 = now.minute%10
            
            display(1, n1)
            display(2, n2)
            display(3, n3)
            display(4, n4)
            if GPIO.input(SWITCH_PIN2) == 0:
                GPIO.output(digits[3], GPIO.LOW)
                for i in range(7):
                    GPIO.output(segments[i], 0)


    

    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(0.7)
    for i in melody2:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(0.7)
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(0.7)
    for i in melody3:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    while True :
        val = GPIO.input(SWITCH_PIN)
        print (val)
        GPIO.output(LED_PIN, val) 

finally:
    GPIO.cleanup()
    print('cleanup and exit')


