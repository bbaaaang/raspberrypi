import RPi.GPIO as GPIO
import time
from datetime import datetime


SEGMENT_PINS =[25,21,22,17,4,12,18] # SEGMENT핀 번호 
DIGIT_PINS =[24,16,20,23]
BUZZER_PIN = 5
LED_PIN = 6
SWITCH_PIN = 26

GPIO.setwarnings (False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT) 
GPIO.setup(SWITCH_PIN , GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

for segment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

for digit in DIGIT_PINS:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, GPIO.HIGH)


data = [[1,1,1,1,1,1,0], # 0
        [0,1,1,0,0,0,0], # 1
        [1,1,0,1,1,0,1], # 2
        [1,1,1,1,0,0,1], # 3
        [0,1,1,0,0,1,1], # 4
        [1,0,1,1,0,1,1], # 5
        [1,0,1,1,1,1,1], # 6
        [1,1,1,0,0,0,0], # 7
        [1,1,1,1,1,1,1], # 8
        [1,1,1,0,0,1,1]] # 9

n1 = 0 # 4-digits FND 처음값 0000
n2 = 0
n3 = 0
n4 = 0


def display(digit, number): # 자리수, 숫자
    # 해당하는 자릿수의 핀만 LOW로 설정
        for i in range(len(DIGIT_PINS)):
            if i + 1 == digit:
                GPIO.output(DIGIT_PINS[i],GPIO.LOW)
            else:
                GPIO.output(DIGIT_PINS[i],GPIO.HIGH)

        #숫자 출력
        for i in range(len(SEGMENT_PINS)): # 0~6
            GPIO.output(SEGMENT_PINS[i], data[number][i])
        time.sleep(0.001)

pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(10)

melody = [330, 294, 262, 294, 330, 330, 330] # 마스크 쓰기 알림 노래  
melody2 = [294, 294, 294, 330, 392, 392]
melody3 = [294, 294, 330, 294, 262]

try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
        print("melody1 Playing") #노래 재생중 

    time.sleep(0.7)
    for i in melody2:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
        print("melody2 Playing") #노래 재생중 

    time.sleep(0.7)
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
        print("melody1-2 Playing") #노래 재생중 

    time.sleep(0.7)
    for i in melody3:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
        print("melody4 Playing") #노래 재생중 

    pwm.stop()

    while True :
        now = datetime.now()
        n1 = int(((now.hour+8)%24)/10) # 현재 시간
        n2 = ((now.hour+8)%24)%10   
        n3 = int(now.minute/10) # 현재 분 
        n4 = now.minute%10
            
        display(1, n1)
        display(2, n2)
        display(3, n3)
        display(4, n4)

        val = GPIO.input(SWITCH_PIN)
        print (val)
        GPIO.output(LED_PIN, val) 

    
    

finally:
    GPIO.cleanup()
    print('cleanup and exit') #종료후 나가기 