from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

FLED_PIN = 4
SLED_PIN = 17
GPIO.setmode(GPIO.BCM) #GPIO.BCM or GPIO.BOARD
GPIO.setup(FLED_PIN, GPIO.OUT)
GPIO.setup(SLED_PIN, GPIO.OUT)

# 0.0.0.0/5000/hello
@app.route("/")
def hello():
    return render_template("led2.html")

@app.route("/<led>/<value>")
def first(led, value):
    if led == 'Fled' and value == 'on':
        print('aa')
        GPIO.output(FLED_PIN, GPIO.HIGH)
        return "Red LED ON"
    elif led == 'Fled' and value == 'off' :
        GPIO.output(FLED_PIN, GPIO.LOW)
        return "Red LED OFF"
    elif led == 'Sled' and value == 'on':
        GPIO.output(SLED_PIN, GPIO.HIGH)
        return "Blue LED ON"
    elif led == 'Sled' and value == 'off' :
        GPIO.output(SLED_PIN, GPIO.LOW)
        return "Blue LED OFF"
    else:
        return "ERROR"

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()