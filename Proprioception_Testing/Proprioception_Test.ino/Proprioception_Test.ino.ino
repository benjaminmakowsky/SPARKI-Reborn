/*
 * AUTHOR: MAKSTUDIOS
 * DATE: 10/1/2019
 * 
 * NOTES: MAKE SURE WHEN USING SERIAL MOINTOR TO TURN OFF LINE ENDING OR IT WILL 
 * RECEIVE MORE THAN INTENDED.
 */

//includes
#include <stdio.h>
#include "CurieIMU.h"

//Defines
#define BUFF_SIZE 4
#define ONBOARD_LED 13

//Variables
char charRead = '\0'; // for incoming serial data

void setup() {
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  pinMode(ONBOARD_LED, OUTPUT);
  while (!Serial);    // wait for the serial port to open
  CurieIMU.begin();

  // Set the accelerometer range to 2G
  CurieIMU.setAccelerometerRange(2);
}

void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    
    // read the incoming byte:
    charRead = Serial.read();
    char buff[BUFF_SIZE];
    
    // say what you got:
    sprintf(buff, "R:%c",charRead);
    Serial.write(buff, BUFF_SIZE);
    Serial.println("\n");

    //Blink if a certain char is read
    switch(charRead){
      
      case 'l':
        for(int i=0; i<3;i++){
          digitalWrite(ONBOARD_LED, HIGH);
          delay(1000);
          digitalWrite(ONBOARD_LED, LOW);
          delay(1000);
        }
        break;

      case 'a':
        float ax, ay, az;   //scaled accelerometer values

        // read accelerometer measurements from device, scaled to the configured range
        CurieIMU.readAccelerometerScaled(ax, ay, az);
      
        // display tab-separated accelerometer x/y/z values
        Serial.print("a:\t");
        Serial.print(ax);
        Serial.print("\t");
        Serial.print(ay);
        Serial.print("\t");
        Serial.print(az);
        Serial.println();
        break;
    }
    

  }
}
