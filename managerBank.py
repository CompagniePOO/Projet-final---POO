#Evalue les profits du jour et totale
from tkinter import *
from datetime import datetime
from datetime import date
from pytz import timezone

#Creation de fenetre
rootManB = Tk()
rootManB.title("Écran du Gérant")
rootManB.geometry("700x600")
rootManB.resizable(False, False)

#Fonction qui evalue les profits, utulisant des valeurs de storage.txt
def get_profits(file):
		global account
		global tdyProfits
		global allProfits
		now = datetime.now(timezone('EST'))
		account=[]
		tdyProfits=0
		allProfits=0
		raw = open(file).read().splitlines()
		for i in range(len(raw)):
			raw[i] = raw[i].strip()
		for i in range(len(raw)):
			account.append(raw[i].split(", "))
		for i in range(len(account)):
			allProfits +=float(account[i][3])
			if account[i][4] == now.strftime("%d/%m/%Y"):
				tdyProfits += float(account[i][3])

global tdyProfits
global allProfits

get_profits("FichiersInfo/storage.txt") #appel a la fonction

#Affichage
manLabel = Label(rootManB, text="PAGE PROFITS - GÉRANTS").pack()
manLabel = Label(rootManB, text=("Profits d'aujourd'hui:  " + str(round(tdyProfits,2)) + "$")).pack()
manLabel1 = Label(rootManB, text=("Profits totale:  " + str(round(allProfits,2)) + "$")).pack()

rootManB.mainloop()