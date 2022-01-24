
from tkinter import *
from PIL import ImageTk, Image  
import time
import yfinance
import os
import subprocess
from datetime import datetime
from datetime import date
from pytz import timezone

root = Tk()
root.title('Banque Investissements')
root.geometry("700x600")
root.resizable(False, False)

#Add stock info if time allows it.
def login():
	global account
	global userEntryLogin
	now = datetime.now(timezone('EST'))
	for i in range (len(account)):
			read_raw("FichiersInfo/adminAccounts.txt")
			if passEntryLogin.get() == account[i][1] and userEntryLogin.get() == account[i][0]:
						file_object = open('FichiersInfo/loginAttempts.txt', 'a')
						file_object.write("Connexion d'administrateur--" + now.strftime("%d/%m/%Y %H:%M:%S")+ "\n")
						file_object.close()
						root.destroy()
						import manager
			else:
				read_raw("FichiersInfo/accounts.txt")
				for i in range (len(account)):
					if passEntryLogin.get() == account[i][1] and userEntryLogin.get() == account[i][0]:
						file_object = open('FichiersInfo/loginAttempts.txt', 'a')
						file_object.write(userEntryLogin.get() + ", " + passEntryLogin.get()+ str(now.strftime(" -- %d/%m/%Y %H:%M:%S"))+ "\n")
						file_object.close()
						root.destroy()
						import transactions
						rootSign.destroy()
					else:
						errorMessage = Label(root, text="Ton mot de passe est nul!").place(x=200, y=40)

def read_raw(file):
			global raw
			global account
			account=[]
			raw = open(file).read().splitlines()
			for i in range(len(raw)):
				raw[i] = raw[i].strip()
			for i in range(len(raw)):
				account.append(raw[i].split(", "))

global userEntryLogin
userEntryLogin = Entry(root)
userEntryLogin.place(x=285, y=220)

global passEntryLogin
passEntryLogin = Entry(root)
passEntryLogin.place(x=285, y=260)

def openSignup():
			import signup

userLabel = Label(root, text="Utilisateur: ")
userLabel.place(x=190, y=220)
global masterKey			
masterKey = 1234 #change to accounts.txt
passLabel = Label(root, text="Mot de passe: ")
passLabel.place(x=170, y=260)

openSignupPage = Button(root, text="S'inscrire", command=openSignup )
openSignupPage.place(x=30, y=290)
					
loginBtn = Button(root, text="CONNEXION",fg="red", height = 3, width = 20, command=login)
loginBtn.place(x=270, y=120)

read_raw("FichiersInfo/accounts.txt")

now = datetime.now(timezone('EST'))
annonces = Label(root, text=("                                    Aujourd'hui: " + now.strftime("%d/%m/%Y") + ", c'est une belle journée pour investir!"))
annonces.place(x=0, y=330)

root.mainloop()