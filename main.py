from tkinter import *
from PIL import ImageTk, Image  
import time
import manager
import yfinance
import os
import subprocess

#Add stock info if time allows it.
class login():
		root = Tk()
		root.title('Banque Crypto')
		root.geometry("700x360")

		def __init__():
			userLabel = Label(root, text="Utulisateur: ")
			userLabel.place(x=200, y=220)
			global masterKey
			masterKey = 1234 #change to accounts.txt

			passLabel = Label(root, text="Mot de passe: ")
			passLabel.place(x=180, y=260)

		def read_raw(file):
			global raw
			global account
			account=[]
			raw = open(file).read().splitlines()
			for i in range(len(raw)):
				raw[i] = raw[i].strip()
			for i in range(len(raw)):
				account.append(raw[i].split(", "))
        
		def loginAuth ():
			global passEntryLogin
			global masterKey
			global userEntryLogin
			global account
			for i in range (len(account)):
				if passEntryLogin.get() == account[i][1] and userEntryLogin.get() == account[i][0]:
					file_object = open('loginAttempts.txt', 'a')
					file_object.write(userEntryLogin.get() + ", " + passEntryLogin.get()+"\n")
					file_object.close()
					import transactions
				else:
					errorMessage = Label(root, text="Ton mot de passe est nul!").place(x=200, y=40)

		global userEntryLogin
		userEntryLogin = Entry(root)
		userEntryLogin.place(x=285, y=220)

		global passEntryLogin
		passEntryLogin = Entry(root)
		passEntryLogin.place(x=285, y=260)

		openSignupPage = Button(root, text="S'inscrire", command=root.destroy)
		openSignupPage.place(x=30, y=290)
					
		loginBtn = Button(root, text="CONNEXION",fg="red", height = 3, width = 20, command=loginAuth)
		loginBtn.place(x=270, y=120)

		annonces = Label(root, text="ANNONCESANNONCESANNONCESANNONCESANNONCESANNONCESANNONCESANNONCESANNONCESANNONCESANNONCES")
		annonces.place(x=0, y=330)

		read_raw("accounts.txt")
		print(account)

import signup

root = Tk()
root.title("Inscrivez-vous")
root.geometry('700x600')

root.mainloop()