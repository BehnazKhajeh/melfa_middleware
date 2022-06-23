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

    
class _port_manager():

  ports_user=""
  ports_melfa=""
  def set_port_melfa(self,mPort):
    self.ports_melfa=mPort
  def set_port_user(self,uPort):
    self.ports_user=uPort
        
  def check_port(self):
      if (self.ports_melfa==self.ports_user and self.ports_melfa!=""):
        print("com == com")
      else:
        print("Robot Port :"+self.ports_melfa)
        print("user Port :"+self.ports_user)
