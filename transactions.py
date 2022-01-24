from tkinter import *

from datetime import datetime
from datetime import date
from pytz import timezone
import time

import yfinance as yf #important dans get_invest, apporte données du marché

root1 = Tk()

canvas=Canvas(root1, width=500, height=300)
canvas.pack()
canvas.create_line(0,180,700,180, fill="green", width=5)
canvas.create_line(340,600,340,180, fill="green", width=5)

def read_raw(file): #divise les doc txt dans des arrays par ligne et virgule
		global raw
		global account
		account=[]
		raw = open(file).read().splitlines()
		for i in range(len(raw)):
			raw[i] = raw[i].strip()
		for i in range(len(raw)):
			account.append(raw[i].split(", "))

def get_current_price(symbol): #valeur d'un stock courant
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return str(round(todays_data['Close'][0],2))
    
def get_open_price(symbol): #valeur d'un stock au début de la journée
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return str(round(todays_data['Open'][0],2))

def addval():# "achète" un stock et modifie les données de texts pour correspondre à cette transaction
	global y
	global investEntry
	global BoughtValue
	global stock 
	read_raw('FichiersInfo/accounts.txt') #maintenant nous lisons accounts.txt
  
	try:
		#float(investEntry.get())
			if (float(investEntry.get()) <= float(account[y][2])) and (float(investEntry.get()) > 1) and (float(account[y][2])) > 0:
				file_object = open('FichiersInfo/storage.txt', 'a')
				errorFunds = Label(root1, text="Investissement completée \n                   ", bg='#00FF00').place(x=430, y=250)
				now = datetime.now(timezone('EST'))
				file_object.write("\n"+ username + ", " + str(float(investEntry.get())/float(BoughtValue)) + ", " + stock + ", " + str(float(investEntry.get())*0.007) + ", " +str(now.strftime("%d/%m/%Y")))
			#str(float(account[y][2])- float(investEntry.get()))+ '*' + str(BoughtValue) + ", ")
				with open('FichiersInfo/accounts.txt', 'r') as file :
							filedata = file.read()
							filedata = filedata.replace(account[y][2], str(float(account[y][2])-(float(investEntry.get())*1.007)))
				with open('FichiersInfo/accounts.txt', 'w') as file:
							file.write(filedata)
				file_object.close()
				with open('FichiersInfo/accounts.txt', 'r') as file :
							filedata1 = file.read()
							filedata1 = filedata1.replace(account[0][2], str(float(account[0][2])+0.007*float(investEntry.get())))
				with open('FichiersInfo/accounts.txt', 'w') as file:
							file.write(filedata1)
				file_object.close()
				display_bal()
				refresh()
			else:
				errorFunds = Label(root1, text="MAX/MIN non-respectée ou \n fonds insuffisants", bg='#FF0000').place(x=430, y=250)
				file_object.close()
	except ValueError:
		errorFunds = Label(root1, text="Entrez un nombre SVP      \n                        ", bg='#FF0000').place(x=430, y=250)
	#only run if no error

def depot(): 
  import Depots

def get_invest(): #cherche dans storage et multiplie le montant du stock que l'utili. possède par le valeur courant
	global z
	global investedTesla
	global investedAmazon
	global investedNike
	inTSLA=[]
	inAMZN=[]
	inNKE=[]
	investedTesla=0
	investedAmazon=0
	investedNike=0
	stockTotVal=0
	read_raw("FichiersInfo/storage.txt")
	for z in range(len(account)):
		if account[z][0]== username:
				if account[z][2]=="Nike":
					inNKE.append(str(float(get_current_price("NKE"))* float(account[z][1])))
				elif account[z][2]=="Amazon":
					inAMZN.append(str(float(get_current_price("AMZN"))* float(account[z][1])))
				elif account[z][2]=="Tesla":
					inTSLA.append(str(float(get_current_price("TSLA"))* float(account[z][1])))
	for i in range (len(inNKE)):
		investedNike += float(inNKE[i])
	for i in range (len(inAMZN)):
		investedAmazon += float(inAMZN[i])
	for i in range (len(inTSLA)):
		investedTesla += float(inTSLA[i])
	stockTotVal = investedNike + investedAmazon + investedTesla 			
	return stockTotVal

def display_bal(): # lit du compte pour montrer balance de l'utilisateur
		global y
		read_raw('FichiersInfo/accounts.txt')
		for i in range(len(account)):
			if account[i][0]== username:
				y=i
				balanceDisplay = Label(root1, text=("Balance: " + str(round(float(account[i][2]),2))) + "              ").place(x=120, y=10)

def investment(stockName): # indique le montant désirez
	global investEntry
	global BoughtValue
	global stock
	stock=stockName

	investLabel = Label(root1, text="Montant a investir ($-$$$$): ").place(x=450,y=200)
	investEntry = Entry(root1, width=4)
	investEntry.place(x=590, y=225)
	if stock == 'Nike':
		BoughtValue = get_current_price('NKE')
	elif stock == 'Amazon':
		BoughtValue = get_current_price('AMZN')
	elif stock == 'Tesla':
		BoughtValue = get_current_price('TSLA')
	submitInvest = Button(root1, text="Confirmer", command=addval).place(x=475,y=220)

def refresh():
	global investedTesla
	global investedAmazon
	global investedNike

	NKEval = Label(root1,text=("Ouverture: " + get_open_price("NKE") + "$")).place(x=100,y=100)
	AMZval = Label(root1,text=("Ouverture: " + get_open_price("AMZN") + "$")).place(x=250, y=100)
	TSLAval = Label(root1,text=("Ouverture: " + get_open_price("TSLA") + "$")).place(x=425,y=100)
	NKEopen = Label(root1,text=("Courant: " + get_current_price("NKE") + "$")).place(x=100,y=130)
	AMZopen = Label(root1,text=("Courant: " + get_current_price("AMZN") + "$")).place(x=250, y=130)
	TSLAopen = Label(root1,text=("Courant: " + get_current_price("TSLA") + "$")).place(x=425,y=130)	
	portfolioLabel = Label(root1, text="Votre portfolio d'investissements:").place(x=50, y=200)
	portfolioStats = Label(root1, text=("-   " + str(round(get_invest(),3)) + "$ investis en totale.    ")).place(x=30, y=235)
	get_invest()
	display_bal()
	NKEStats = Label(root1, text=("-   " + str(round(float(investedNike),3)) + "$ investis en Nike.      ")).place(x=30, y=255)
	AMZNStats = Label(root1, text=("-   " + str(round(float(investedAmazon),3)) + "$ investis en Amazon.   ")).place(x=30, y=275)
	TSLAStats = Label(root1, text=("-   " + str(round(float(investedTesla),3)) + "$ investis en Tesla.      ")).place(x=30, y=295)
	now_EST = datetime.now(timezone('EST'))
	timeAndDay = Label(root1, text=now_EST.strftime("%d/%m/%Y %H:%M:%S")).place(x=400,y=10)

	time_string = time.strftime('%H')
	if 9 > int(time_string) > 17 or datetime.today().weekday() > 4 :
		closedMarkets = Label(root1, text="---FERMÉ---", bg="#FF0000").place(x=275,y=155)
	else:
		openMarkets = Label(root1, text="---OUVERT---", bg="#00FF00").place(x=275,y=155)

def sell(sellStock):
	global y
	investedTotal=0
	abbreviation=''

	if sellStock == 'Tesla':
		investedTotal = investedTesla
		abbreviation = 'TSLA'
	if sellStock == 'Amazon':
		investedTotal = investedAmazon
		abbreviation = 'AMZN'
	if sellStock == 'Nike':
		investedTotal = investedNike
		abbreviation = 'NKE'

	read_raw('FichiersInfo/accounts.txt')
	if  (float(account[y][2])) > 0:
		print(float(account[y][1]))
		file_object = open('FichiersInfo/storage.txt', 'a')
		plsRefresh = Label(root1, text="Vendu avec succès (SVP REFRESH)", bg='#00FF00').place(x=100, y=330)
		now = datetime.now(timezone('EST'))
		file_object.write("\n"+ username + ", -" + str(investedTotal/float(get_current_price(abbreviation))) + ", " + sellStock + ", 0, " + now.strftime("%d/%m/%Y"))
		with open('FichiersInfo/accounts.txt', 'r') as file :
					filedata = file.read()
					filedata = filedata.replace(account[y][2], str(float(account[y][2])+(investedTotal)))
		with open('FichiersInfo/accounts.txt', 'w') as file:
					file.write(filedata)
		display_bal()
		refresh()
	else:
		errorFunds = Label(root1, text="MAX/MIN non-respectée ou \n fonds insuffisants", bg='#FF0000').place(x=430, y=250)
		file_object.close()

def revealInfo():
	import infoPage

def logout():
	import main.py
	root1.destroy()

read_raw('FichiersInfo/loginAttempts.txt')
username = account[len(account)-1][0]
password = account[len(account)-1][1]

display_bal()
InvestNKE = Button(root1, text ="INVESTIR EN NIKE", command =lambda: investment('Nike')).place(x=90,y=60)
InvestAMZ = Button(root1, text ="INVESTIR EN AMAZON", command =lambda: investment('Amazon')).place(x=250,y=60)
InvestTSLA = Button(root1, text ="INVESTIR EN TESLA", command =lambda: investment('Tesla')).place(x=435,y=60)

sellNKE = Button(root1, text="Vendre NKE",command= lambda:sell('Nike'), bg='#00FF00', height=1).place(x=290,y=235)
sellAMZ = Button(root1, text="Vendre AMZN",command= lambda: sell('Amazon'), bg='#00FF00').place(x=290,y=265)
sellTSLA = Button(root1, text="Vendre TSLA",command= lambda: sell('Tesla'), bg='#00FF00').place(x=290,y=295)

refresher = Button(root1, text="Refresh", command= refresh).place(x=595,y=10)

logout = Button(root1, text="Logout", command= logout).place(x=610,y=35)


infoBtn = Button(root1, text="Information\nimportante", bg='#FF0000', command=revealInfo).place(x=1,y=10)

depositBtn = Button(root1, text = "faire un dépôt\noù retirer", command = depot)
depositBtn.place(x = 500, y = 300)

refresh()

root1.title("Investissements") 
root1.geometry('700x600')
root1.resizable(False, False)

root1.mainloop()