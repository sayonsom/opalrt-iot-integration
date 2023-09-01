# OPAL-RT Technologies Inc.
#This script is provided 'as is', without warranty of any kind.

# Python version used is 3.7.3

##Import Libraries
import array
from ServerRP import Ethernet
import socket
import time

##Initiate Communications with the simulator
## CHANGE THE IP ADDRESS ACCORDINGLY
## (The IP address is the one from the raspberry PI)
comm = Ethernet(50000,'10.168.11.43')

time.sleep(1)
counter = 0

# This script will run indefinitely
while True:
    
    ##Obtain measurements from Simulator
    Meas = comm.status()
    
    # Display the received value
    print (Meas)
    time.sleep(1)
    counter = counter + 1
    
    ##Send commands to the simulator
    comm.send([12, 24, 45, counter])
    print('commands:', end="")
    print(str([12, 24, 45, counter]))
		
    time.sleep(1)
