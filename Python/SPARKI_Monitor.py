#Self Implemented Serial Monitor for Sparki
import serial
import threading
import sys


#Function used to listen for message
def msg_monitor():
    print('Starting monitor\n')
    ser = serial.Serial('/dev/ttyACM0', 9600)   #Serial port to talk to
    ser.flushInput()                            #Flushes input to prevent any strange behavior
    decoded_bytes = ""

    while(True):
        global stop_threads
        if stop_threads: 
            break
        elif(ser.in_waiting > 0):
                ser_bytes = ser.readline()
                decoded_bytes = (ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                #Debug line can be removed
                print(decoded_bytes)




#Function to send msgs via serial            
def msg_sender():
    #Setup
    print('Starting Sender\n')
    msg = 'NULL'                                #Character to send
    ser = serial.Serial('/dev/ttyACM0', 9600)   #Serial port to talk to
    ser.flushInput()                            #Flushes input to prevent any strange behavior

    print("Enter a single character: ")
    while(True):
        global stop_threads
        if stop_threads: 
            break
        else:
            #Get input and check length validity	
            msg = input()

            if(len(msg) > 1):	    
                  print('Error! Not a single character\n')
            
            if(str(msg) == "q"):
               stop_threads = True	
            else:
               ser.write(msg[0].encode())	 
        


#Gloabl Variable to stop Threads
stop_threads = False     

# Create new threads
thread1 = threading.Thread(target = msg_sender)
thread2 = threading.Thread(target = msg_monitor)

# Start new Threads
thread1.start()
thread2.start()

print("Exiting Initialization Thread")