#!/usr/bin/env python3
import serial

#Setup
char_read = " "
received_response = True;
ser = serial.Serial('/dev/ttyACM0', 9600)
ser.flushInput()    #Flushes input to prevent any strange behavior

#Read user input until q
while(char_read != "q"):

    #Check if anything is in bufffer
    char_read = input("Enter a single character: ")
    if(len(char_read) > 1):
        print('Error! Not a single character\n')
    else:
        #You have to encode the write as a byte to transmit over serial to arduino
        ser.write(char_read.encode())

        #Flag used signal the wait for a response
        received_response = False
        print('Sent\n') #Debug line not really needed just useful

    #Wait until a response is received before looping again
    #NOTE: Slows down program by requiring waiting for input but useful for debugging
    while(received_response == False):

        #Do nothing until there are bytes waiting in the serial buffer
        if(ser.in_waiting > 0):
            ser_bytes = ser.readline()
            
            #parses the string cutting off the last characters from the return key from the keyboard
            #and converts it to utf-8 the arduino standrard encoding
            decoded_bytes = (ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            print(decoded_bytes)
            received_response = True

    
