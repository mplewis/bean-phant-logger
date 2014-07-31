#define FOREVER 4294967295

void setup()
{
    // initialize serial communication
    Serial.begin(57600);
    Bean.sleep(FOREVER);
}

// the loop routine runs over and over again forever:
void loop()
{
    Bean.setLed(255, 0, 0);

    Serial.print(Bean.getBatteryVoltage());
    Serial.print('\t');
    Serial.print(Bean.getTemperature());
    Serial.print('\t');
    Serial.print(analogRead(A0));
    Serial.print('\t');
    Serial.print(analogRead(A1));
    Serial.print('\n');

    Bean.setLed(0, 0, 0);
    Bean.sleep(FOREVER);
}
