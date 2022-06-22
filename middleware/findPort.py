from ast import Break
from tkinter import Y
import serial
import serial.tools.list_ports
from time import sleep, perf_counter
from threading import Thread
import threading
import time

def find_USB_device():
    myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]


    usb_port_list = [p[0] for p in myports]
    
    return usb_port_list

def HMI_cmd():
    list_port=list(range(2))
    ports= find_USB_device()
    portNums=len(ports)
    if portNums==1:
     print("You got this port")
     print(ports)
    
     chy=input("If You one Just use Robot in solo mode press y ...")
     if chy=='y':
         chMelfa=ports[0]
         list_port.append(ports)
         return list_port
    elif portNums==0:
           print("PLease Connect User and Robot Device ")
           return list_port
    elif portNums==2:
      print("You got this ports")
      print(ports)
      chMelfa=input("Choose Robot Port: ")
      chUser=input("Choose UserSystem Port: ")
      list_port.append(chMelfa)
      list_port.append(chUser)
      return list_port
    
