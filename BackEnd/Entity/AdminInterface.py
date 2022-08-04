import random


def setDefaultId():
  DefaultId = random.randint(100000, 9999999)
  return DefaultId

class AdminInterface:
  def __init__(self,Email,nom,prenom,role):
    self.id = setDefaultId()
    self.Email = Email
    self.nom = nom
    self.prenom = prenom
    self.role = role
  def get_nom(self):
    return self.nom

  def TestInterfaceCreated(self):
    print(self.Email,self.nom, self.prenom,self.role,self.id)

#test = AdminInterface("mouna@gmail.com","mouna","chmengui","admin")
#test.TestAdminExisted()

test = AdminInterface


