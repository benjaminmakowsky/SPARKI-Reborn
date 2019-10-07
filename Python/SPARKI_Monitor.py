#Self Implemented Serial Monitor for Sparki
import serial
import threading


#Setup
msg = 'NULL'                             #Character to send
ser = serial.Serial('/dev/ttyACM0', 9600)#Serial port to talk to
ser.flushInput()                         #Flushes input to prevent any strange behavior

while(msg != "\q")