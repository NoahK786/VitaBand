#include <Wire.h>
#include <Adafruit_Sensor.h>

#define HRV_PIN 32
#define EDA_PIN 33
#define TEMP_PIN 34
#define LED_PIN 5

void setup() {
    pinMode(LED_PIN, OUTPUT);
    Serial.begin(115200);
}

void loop() {
    int HRV = analogRead(HRV_PIN);
    int EDA = analogRead(EDA_PIN);
    int TEMP = analogRead(TEMP_PIN);
    
    if (HRV < 50 && EDA > 300 && TEMP > 90) {
        digitalWrite(LED_PIN, HIGH);
        Serial.println("Stress Detected!");
    } else {
        digitalWrite(LED_PIN, LOW);
    }
    
    delay(1000);
}
