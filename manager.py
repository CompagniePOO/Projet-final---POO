from tkinter import *
from tkinter import filedialog

rootMan = Tk()
rootMan.title("Écran du Gérant")
rootMan.geometry("700x600")

manText = Text(rootMan, width = 75, height = 18, font = ("Helvetica", 8))
manText.pack(pady = 10)

def openAcct():
  manText.delete('1.0', END)
  fichierCompte = open("accounts.txt", 'r')
  compte = fichierCompte.read()
  manText.insert(END, compte)
  fichierCompte.close()

def openLogin():
  manText.delete('1.0', END)
  fichierLogin = open("loginAttempts.txt", 'r')
  login = fichierLogin.read()
  manText.insert(END, login)
  fichierLogin.close()

def openStorage():
  manText.delete('1.0', END)
  fichierStockage = open("storage.txt", 'r')
  storage = fichierStockage.read()
  manText.insert(END, storage)
  fichierStockage.close()

accountsBtn = Button(rootMan, text = "Fichier des comptes", command = openAcct)
accountsBtn.place(x = 450, y = 300)

loginBtn = Button(rootMan, text = "tentatives de connexion", command = openLogin)
loginBtn.place(x = 50, y = 300)

storageBtn = Button(rootMan, text = "stockage", command = openStorage)
storageBtn.place(x = 300, y = 300)


rootMan.mainloop()