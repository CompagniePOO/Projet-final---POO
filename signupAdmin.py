from tkinter import *
import random
import re

#Classe pour créer utilisateur
class signup():

  def __init__(self, userEntrySign = "", nameEntrySign = "", emailEntrySign = "", passEntrySign = "", acctNumSign = 0):
    self.userEntry = userEntrySign
    self.nameEntry = nameEntrySign
    self.emailEntry = emailEntrySign
    self.passEntry = passEntrySign
    self.acctNum = acctNumSign

  def name(self):
    labelName = Label(rootSignAdm, text = "Entrez votre nom complet")
    labelName.place(x = 250 ,y = 0)
    self.nameEntry = Entry(rootSignAdm);self.nameEntry.place(x = 250 ,y = 20)
    self.nameEntry

  def username(self):
    labelUserName = Label(rootSignAdm, text = "Entrez votre nom d'utilisateur")
    labelUserName.place(x = 250, y = 40)
    self.userEntry = Entry(rootSignAdm);self.userEntry.place(x = 250 ,y = 60)

  def email(self):
    labelemail = Label(rootSignAdm, text = "Entrez votre courriel")
    labelemail.place(x = 250 ,y = 80)
    self.emailEntry = Entry(rootSignAdm);self.emailEntry.place(x = 250, y = 100)
  
  def password(self):
    labelPass = Label(rootSignAdm, text = "Entrez votre mot de passe")
    labelPass.place(x = 250, y = 120)
    self.passEntry = Entry(rootSignAdm);self.passEntry.place(x = 250 ,y = 140)
  
  def acctNumGen(self):
    self.acctNum = random.randint(10000, 99999)

  def signBtn(self):
    signupBtn = Button(rootSignAdm, text = "Suivant", command = lambda: confirm())
    signupBtn.place(x = 300, y = 160)

#Création de fenetre
rootSignAdm = Tk()
canvasSign = Canvas()
rootSignAdm.title("Inscrivez-vous")
rootSignAdm.geometry('700x600')
rootSignAdm.resizable(False, False)

#Défini variables de classe
newUser = signup()
newUser.name()
newUser.username()
newUser.email()
newUser.password()
newUser.acctNumGen()

#Fonction pour lire les fichiers
def read_raw_signup(file):
		global raw
		global account
		account=[]
		raw = open(file).read().splitlines()
		for i in range(len(raw)):
			raw[i] = raw[i].strip()
		for i in range(len(raw)):
			account.append(raw[i].split(", "))
			
#Lis le fichier
read_raw_signup('FichiersInfo/adminAccounts.txt')

#Crée une liste de nom d'utilisateurs pris
takenUser = []
for i in range(len(account)):
  takenUser.append(account[i][0])

#Crée une liste de courriels pris
takenEmail = []
for i in range(len(account)):
  takenEmail.append(account[i][3])

#Défini un format de courriel valid
validEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

#Confirme que signup est bien remplis et si oui, ajoute le compte à le fichier
def confirm():		
  if newUser.nameEntry.get() == '' or newUser.userEntry.get() == '' or newUser.emailEntry.get() == '' or newUser.passEntry.get() == '':
    invalid = Label(rootSignAdm, text = "           Manque d'information                 \n                                   \n                           \n                     \n                                \n                      ")
    invalid.config(fg = "red")
    invalid.place(x = 210, y = 200)
  elif newUser.userEntry.get() in takenUser:
    takenUserLabel = Label(rootSignAdm, text = "  Ce nom d'utilisateur est déjà occupé    \n                                   \n                           \n                     \n                                \n                      ")
    takenUserLabel.config(fg = "red")
    takenUserLabel.place(x = 210, y = 200)
  elif not re.fullmatch(validEmail, newUser.emailEntry.get()):
    invalidEmail = Label(rootSignAdm, text = "          Ce courriel est invalide                 \n                                   \n                           \n                     \n                                \n                      ")
    invalidEmail.config(fg = "red")
    invalidEmail.place(x = 210, y = 200)
  elif newUser.emailEntry.get() in takenEmail:
    takenEmailLabel = Label(rootSignAdm, text = "Ce courriel est déjà associé à un compte\n                                   \n                           \n                     \n                                \n                      ")
    takenEmailLabel.config(fg = "red")
    takenEmailLabel.place(x = 210, y = 200)  
  else:
    file_object = open('FichiersInfo/adminAccounts.txt', 'a')
    newAccount = str(newUser.userEntry.get()) +", "+ str(newUser.passEntry.get()) +", "+ str(0) +", "+ str(newUser.emailEntry.get()) +", "+ "Account#"+ str(newUser.acctNum) + ", " + str(newUser.nameEntry.get())
    file_object.write("\n"+newAccount)
    file_object.close()
    import main
    rootSignAdm.destroy()

#Boutton signup
newUser.signBtn()

def returnLogin():
  rootSignAdm.destroy()

#Boutton retour
returnBtn = Button(rootSignAdm, text = "Retour", command = returnLogin)
returnBtn.place(x = 30, y = 290)