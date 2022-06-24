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

def get_num_port():
    return  len(find_USB_device())  


#Todo:// Make Port Allocation ........
class _port_manager():
#port getter and setter
  ports_user=""
  ports_melfa=""
  #melfa port
  def set_port_melfa(self,mPort):
    return self.check_port(mPort,self.ports_user)
    
  def get_port_melfa(self):
    return self.ports_melfa
  #user Port
  def set_port_user(self,uPort):
    return self.check_port(self.ports_melfa,uPort)

  def get_port_user(self):
    return self.ports_user

        
  def check_port(self,pMelfa,pUser):

      if (pMelfa==""):
        return "Select Robot Port First!"
      if (pMelfa==pUser):
        
        return "Robot port and Direct-User port cannot \nbe the same ! "
      else:
         self.ports_user=pUser
         self.ports_melfa=pMelfa
         #Here We must check athourization of robot and show the poroper message
         return "ok"