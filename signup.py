from tkinter import *
import random

class signup():

  def __init__(self, userEntrySign = "", nameEntrySign = "", emailEntrySign = "", passEntrySign = "", acctNumSign = 0):
    self.userEntry = userEntrySign
    self.nameEntry = nameEntrySign
    self.emailEntry = emailEntrySign
    self.passEntry = passEntrySign
    self.acctNum = acctNumSign

  def name(self):
    labelName = Label(rootSign, text = "Entrez votre nom complet")
    labelName.place(x = 250 ,y = 0)
    self.nameEntry = Entry(rootSign);self.nameEntry.place(x = 250 ,y = 20)
    self.nameEntry

  def username(self):
    labelUserName = Label(rootSign, text = "Entrez votre nom d'utilisateur")
    labelUserName.place(x = 250, y = 40)
    self.userEntry = Entry(rootSign);self.userEntry.place(x = 250 ,y = 60)

  def email(self):
    labelemail = Label(rootSign, text = "Entrez votre courriel")
    labelemail.place(x = 250 ,y = 80)
    self.emailEntry = Entry(rootSign);self.emailEntry.place(x = 250, y = 100)
  
  def password(self):
    labelPass = Label(rootSign, text = "Entrez votre mot de passe")
    labelPass.place(x = 250, y = 120)
    self.passEntry = Entry(rootSign);self.passEntry.place(x = 250 ,y = 140)
  
  def acctNumGen(self):
    self.acctNum = random.randint(10000, 99999)

  def signBtn(self):
    signupBtn = Button(rootSign, text = "Suivant", command = lambda: confirm())
    signupBtn.place(x = 300, y = 160)

rootSign = Tk()
canvasSign = Canvas()
rootSign.title("Inscrivez-vous")
rootSign.geometry('700x600')

newUser = signup()
newUser.name()
newUser.username()
newUser.email()
newUser.password()
newUser.acctNumGen()

def confirm():		
  if newUser.nameEntry.get() == '' or newUser.userEntry.get() == '' or newUser.emailEntry.get() == '' or newUser.passEntry.get() == '':
    invalid = Label(rootSign, text = "Manque d'information")
    invalid.config(fg = "red")
    invalid.place(x = 250, y = 180)
  else:
    file_object = open('accounts.txt', 'a')
    newAccount = str(newUser.userEntry.get()) +", "+ str(newUser.passEntry.get()) +", "+ str(0) +", "+ str(newUser.emailEntry.get()) +", "+ "Account#"+ str(newUser.acctNum) + ", " + str(newUser.nameEntry.get())
    file_object.write("\n"+newAccount)
    file_object.close()
    import main
    rootSign.destroy()

newUser.signBtn()     