from ast import Num
from asyncio.windows_events import NULL
from operator import itemgetter
from tkinter import Y
import click
from importlib_metadata import List
import serial
import serial.tools.list_ports
from time import sleep, perf_counter
from threading import Thread
import threading
import time
import findPort
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import *

#inherient from my_port_manager :Check not to take same port
from my_port_manager import _port_manager

class mWindow(QMainWindow,_port_manager):  
    

    def __init__(self):
        title="Melfa Middleware V1"

        super(mWindow,self).__init__()
        self.setGeometry(200,200,300,300)
        self.setWindowTitle(title)
        self.initUI()
    def initUI(self):
          lists_ports=findPort.find_USB_device()
          # Robo label
          self.label_portr=QtWidgets.QLabel(self)
          self.label_portr.setText("Select Robo Port")
          self.label_portr.move(10,10)
          # Robo Port
          self.list_portsr=QtWidgets.QListWidget(self)
          self.list_portsr.move(10,40)
        
   
          self.list_portsr.addItems(lists_ports)

          self.list_portsr.clicked.connect(self.clickedr)
          # user label
          self.label_portu=QtWidgets.QLabel(self)
          self.label_portu.setText("Select User Port")
          self.label_portu.move(150,10)
          # User Port
          self.list_portsu=QtWidgets.QListWidget(self)
          self.list_portsu.move(150,40)
   
          self.list_portsu.addItems(lists_ports)

          self.list_portsu.clicked.connect(self.clickedu)
    def clickedr(self, qmodelindex):
      
      item = self.list_portsr.currentItem()
    
      self.set_port_melfa(item.text())
      self.check_port()
      # print("Robot Port :"+item.text())
    def clickedu(self, qmodelindex):
      item = self.list_portsu.currentItem()
      # print("User Port :"+item.text())
     
      self.set_port_user(item.text())
      self.check_port()
   
 

def window():

    app=QApplication(sys.argv)
    win=mWindow()
    

  

    win.show()
    sys.exit(app.exec())



if __name__ == "__main__":

   window()


