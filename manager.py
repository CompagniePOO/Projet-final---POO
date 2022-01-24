from tkinter import *
from tkinter import filedialog

#Creation de fenetre
rootMan = Tk()
rootMan.title("Écran du Gérant")
rootMan.geometry("700x600")
rootMan.resizable(False, False)

manText = Text(rootMan, width = 75, height = 18, font = ("Helvetica", 8))
manText.pack(pady = 10)

#Fonction pour ouvrir le dossier et voir les fichier
def openFolder():
  manText.delete('1.0', END)
  fichierCompte = filedialog.askopenfilename(initialdir = "FichiersInfo/", title = "Ouvre un fichier", filetypes = (("Fichiers text", "*.txt"), ))
  fichierCompte = open(fichierCompte, 'r')
  compte = fichierCompte.read()
  manText.insert(END, compte)
  fichierCompte.close()

#Fonction qui sauvegarde les changements au fichier
def sauvegarde():
  fichierText = filedialog.askopenfilename(initialdir = "FichiersInfo/", title = "Ouvre un fichier", filetypes = (("Fichiers text", "*.txt"), ))
  fichierText = open(fichierText, 'w')
  fichierText.write(manText.get(1.0, END))

#Ouvre une autre page qui evalue les profits
def checkProfits():
	import managerBank

def compteGerant():
  import signupAdmin

#GUI
profitsBtn = Button(rootMan, text = "Voire Profits", command=checkProfits).place(x = 30, y = 300)

accountsBtn = Button(rootMan, text = "Ouvre un fichier", command = openFolder)
accountsBtn.place(x = 170, y = 300)

saveBtn = Button(rootMan, text = "Sauvegarde", command = sauvegarde)
saveBtn.place(x = 345, y = 300)

newAccBtn = Button(rootMan, text = "Crée un compte admin", command = compteGerant)
newAccBtn.place(x = 485, y = 300)

rootMan.mainloop()