import random


def setDefaultId():
  DefaultId = random.randint(100000, 9999999)
  return DefaultId

class SiteGsmInterface:
  def __init__(self,Couverture,date_mise_en_service,Localisation):
    self.id = setDefaultId()
    self.Couverture = Couverture
    self.date_mise_en_service = date_mise_en_service
    self.Localisation = Localisation


  def TestInterfaceCreated(self):
    print(self.id,self.Couverture, self.date_mise_en_service,self.Localisation)

#test = AdminInterface("mouna@gmail.com","mouna","chmengui","admin")
#test.TestAdminExisted()



