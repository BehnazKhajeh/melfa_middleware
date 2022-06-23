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

import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import *

#inherient from my_port_manager :Check not to take same port
from my_port_manager import _port_manager
import my_port_manager
class mWindow(QMainWindow,_port_manager):  
    

    def __init__(self):
        title="Melfa Middleware V1"

        super(mWindow,self).__init__()

        #Window Size Here
        self.setFixedSize(640,480)
        # self.setFixedSize(320,240)
        # self.setGeometry(200,200,300,300)
        self.setWindowTitle(title)
        self.initUI()
    def initUI(self):


          #Refresh button
          lists_ports=my_port_manager.find_USB_device()
          self.btn_refresh=QtWidgets.QPushButton(self)
          self.btn_refresh.setText("Refresh Middleware")
          self.btn_refresh.setGeometry(200, 150, 120, 50)
          self.btn_refresh.move(260,30)
          self.btn_refresh.setStyleSheet("background-color : #F9D923")
          #Start button
          lists_ports=my_port_manager.find_USB_device()
          self.btn_start=QtWidgets.QPushButton(self)
          self.btn_start.setText("Start Middleware")
          self.btn_start.setGeometry(200, 150, 120, 50)
          self.btn_start.move(260,90)
          self.btn_start.setStyleSheet("background-color : #76BA99")
          #Stop button
          lists_ports=my_port_manager.find_USB_device()
          self.btn_stop=QtWidgets.QPushButton(self)
          self.btn_stop.setText("Stop Middleware")
          self.btn_stop.setGeometry(200, 150, 120, 50)
          self.btn_stop.move(260,150)
          self.btn_stop.setStyleSheet("background-color : #DA1212")
          # Middleware state label
          self.label_portr=QtWidgets.QLabel(self)
          self.label_portr.setText("Middleware State")
          self.label_portr.move(275,5)
          #Check state and the choose color of state 
          # Robo label
          self.label_portr=QtWidgets.QLabel(self)
          self.label_portr.setText("Select Robo Port")
          self.label_portr.move(30,10)
          # Robo Port
          self.list_portsr=QtWidgets.QListWidget(self)
          self.list_portsr.move(30,40)
          self.list_portsr.addItems(lists_ports)
          self.list_portsr.clicked.connect(self.clickedr)
          # Robo label port name <---------------- Here
          self.label_portr_name=QtWidgets.QLabel(self)
          self.label_portr_name.setText("Robo Port")
          self.label_portr_name.move(30,70)
          # user label
          self.label_portu=QtWidgets.QLabel(self)
          self.label_portu.setText("Select User Port")
          self.label_portu.move(500,10)
          #User CheckBox
          self.check_user=QtWidgets.QCheckBox("direct user?",self)
          self.check_user.stateChanged.connect(self.btnstate)
          self.check_user.move(410,40)
          # User Port
          self.list_portsu=QtWidgets.QListWidget(self)
          self.list_portsu.move(500,40)
          self.list_portsu.addItems(lists_ports)
          self.list_portsu.clicked.connect(self.clickedu)
          self.list_portsu.setEnabled(False)
          # User label port name <---------------- Here
          self.label_portr_name=QtWidgets.QLabel(self)
          self.label_portr_name.setText("User Port")
          self.label_portr_name.move(500,70)
          #Connection ListVIew
          self.list_connection_command=QtWidgets.QListWidget(self)
          self.list_connection_command.setGeometry(50, 220, 550, 250)

    def show_selected_port(self):
        self.label_portr_name.setText(self.get_port_melfa())      
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
    def btnstate(self,state):
    
         if state == QtCore.Qt.Checked:
            print (" is selected")
            self.list_portsu.setEnabled(True)
         else:
            print (" is deselected")
            self.list_portsu.setEnabled(False)


 

def window():

    app=QApplication(sys.argv)
    win=mWindow()
    

  

    win.show()
    sys.exit(app.exec())



if __name__ == "__main__":

   window()


