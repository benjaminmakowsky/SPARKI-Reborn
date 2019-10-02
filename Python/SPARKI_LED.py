#!/usr/bin/env python3
import serial

#Setup
char_read = " "
ser = serial.Serial('/dev/ttyACM0', 9600)

#Read user input until q
while(char_read != "q"):
    #Get input and check length validity
    char_read = input("Enter a single character: ")
    if(len(char_read) > 1):
        print('Error! Not a single character\n')
    else:
        ser.write(char_read.encode())
        print('Sent\n')
