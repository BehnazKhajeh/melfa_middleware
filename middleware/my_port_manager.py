       
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
