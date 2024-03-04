#include <Servo.h>

Servo myservo; // Create a servo object

void setup()
{
    Serial.begin(9600); // Initialize the serial communication
    myservo.attach(10); // Attach the servo to pin 10
}

void loop()
{
    if (Serial.available()){
        
        char command = Serial.read(); // Read the incoming command

        if (command == '0'){
            myservo.write(0); // Rotate the servo to ø degrees
        }
        else if (command == '1'){
            myservo.write(90); // Rotate the servo to 90 degrees
        }
        else if (command == '2'){
            myservo.write(180); // Rotate the servo to 180 degrees
        }
    }
}
