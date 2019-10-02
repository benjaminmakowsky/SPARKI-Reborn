#!/usr/bin/env python3
import serial

#Setup
char_read = " "
received_response = True;
ser = serial.Serial('/dev/ttyACM0', 9600)
ser.flushInput()

#Read user input until q
while(char_read != "q"):

    #Check if anything is in bufffer
    char_read = input("Enter a single character: ")
    if(len(char_read) > 1):
        print('Error! Not a single character\n')
    else:
        ser.write(char_read.encode())
        received_response = False
        print('Sent\n')

    while(received_response == False):
        if(ser.in_waiting > 0):
            ser_bytes = ser.readline()
            decoded_bytes = (ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            print(decoded_bytes)
            received_response = True

    
