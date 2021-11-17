#include <wiringPi.h>
#define LED_PIN_a 7
#define LED_PIN_b 5
#define LED_PIN_c 3

int main() {
    wiringPiSetup();
    pinMode(LED_PIN_a, OUTPUT);
    pinMode(LED_PIN_b, OUTPUT);
    pinMode(LED_PIN_c, OUTPUT);

    for(int i=0; i<5; i++) {
        digitalWrite(LED_PIN_a, HIGH); delay(2000);
        digitalWrite(LED_PIN_a,  LOW);

        digitalWrite(LED_PIN_b, HIGH); delay(2000);
        digitalWrite(LED_PIN_b,  LOW);

        digitalWrite(LED_PIN_c, HIGH); delay(2000);
        digitalWrite(LED_PIN_c,  LOW);
    }
    return 0;
}