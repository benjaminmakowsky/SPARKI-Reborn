#Self Implemented Serial Monitor for Sparki
import serial
import threading



exitFlag = 0

#Define a thread that handles incoming text and displays it to the prompt
class incomingThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name

   def run(self):
      print("Starting " + self.name)
      msg_sender()
      print("Exiting " + self.name)


#Define a thread that handles sending messages to arduino via serial
class outgoingThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name

   def run(self):
      print("Starting " + self.name)
      msg_monitor()
      print("Exiting " + self.name)

#Function used to wait for message
def msg_monitor():
    ser = serial.Serial('/dev/ttyACM0', 9600)   #Serial port to talk to
    ser.flushInput()                            #Flushes input to prevent any strange behavior
    received_quit = False
    while(received_quit == False):
        decoded_bytes = ""
        if(ser.in_waiting > 0):
                ser_bytes = ser.readline()
                decoded_bytes = (ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                print(decoded_bytes)
        if(decoded_bytes == "q"):
            received_quit = True
            

#Function to send msgs via serial            
def msg_sender():
    #Setup
    msg = 'NULL'                                #Character to send
    ser = serial.Serial('/dev/ttyACM0', 9600)   #Serial port to talk to
    ser.flushInput()                            #Flushes input to prevent any strange behavior

    print("Enter a single character: ")
    received_quit = False
    while(received_quit == False):
        #Get input and check length validity	
        msg = input()
        if(str(msg) == "q"):
            received_quit = True
            print("Received Exit Code")	    
        if(len(msg) > 1):	    
            print('Error! Not a single character\n')	       
        else:	   
            ser.write(msg.encode())	        

# Create new threads
thread1 = incomingThread(1, "msg_monitor")
thread2 = outgoingThread(2, "msg_sender")

# Start new Threads
# Start new Threads
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("\nExiting the Program!!!")


