#When called this scrips sends character to turn on the LED on the arduino
import serial

#Setup
char_read = 'a'                          #Character to send
ser = serial.Serial('/dev/ttyACM0', 9600)#Serial port to talk to
ser.flushInput()                         #Flushes input to prevent any strange behavior
ser.write(char_read.encode())            #Sends character
