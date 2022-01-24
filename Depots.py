from tkinter import *

rootDepots = Tk()
rootDepots.title("faire un dépôt où retirer")
rootDepots.geometry("350x150")
rootDepots.resizable(False, False)

#Fonction qui nous permet de separer les .txt a des variables
def read_raw_depots(file):
		global raw
		global account
		account=[]
		raw = open(file).read().splitlines()
		for i in range(len(raw)):
			raw[i] = raw[i].strip()
		for i in range(len(raw)):
			account.append(raw[i].split(", "))
#Fonction qui affiche balance quand necessaire
def display_bal():
		global y 
		read_raw_depots('FichiersInfo/accounts.txt')
		for i in range(len(account)):
			if account[i][0]== username:
				y=i
				balanceDisplay = Label(rootDepots, text=("Balance: " + str(round(float(account[i][2]),2))) + "              ").place(x=120, y=60)
#Fonction qui -/+ balance et modifie sa valeur dans .txt
def transaction(operation):
	global y
	global account
	global amtEntry

	try:
		if (float(amtEntry.get()) <= float(account[y][2])) and (float(amtEntry.get()) > 1) and (float(account[y][2])) > 0:
			sumAdd=float(amtEntry.get())
			with open('FichiersInfo/accounts.txt', 'r') as file :
						filedata = file.read()
						if operation == "+":
							filedata = filedata.replace(account[y][2], str(float(account[y][2])+sumAdd))
						elif operation == "-":
							filedata = filedata.replace(account[y][2], str(float(account[y][2])-sumAdd))
						#try and catch
			with open('FichiersInfo/accounts.txt', 'w') as file:
						file.write(filedata)
			display_bal() # pour update balance
		else:
			errorFunds = Label(root1, text="MAX/MIN non-respectée ou \n fonds insuffisants", bg='#FF0000').place(x=135, y=110)
	except ValueError:
		errorLabel = Label(rootDepots, text="Quantité invalide.").place(x=135,y=110)
		

class solde():

  def __init__(self, compteDepots, argent):
    self.compte = compteDepots
    self.bal = argent
  
  def depot(self, somme):
    self.bal += somme
  
  def retrait(self, somme):
    self.bal -= somme

read_raw_depots('FichiersInfo/loginAttempts.txt')
username = account[len(account)-1][0] 
password = account[len(account)-1][1]

display_bal()

amtEntry = Entry(rootDepots, width=5)
amtEntry.place(x=135, y=80)
despositBtn = Button(rootDepots, text="Depot", command= lambda: transaction("+")).pack() #Bouton de depot
retireBtn = Button(rootDepots, text="Retirer", command= lambda: transaction("-")).pack() #Bouton pour retirer

rootDepots.mainloop()