from tkinter import *

from datetime import datetime
from datetime import date
from pytz import timezone

import yfinance as yf

root1 = Tk()

canvas=Canvas(root1, width=500, height=300)
canvas.pack()
canvas.create_line(0,180,700,180, fill="green", width=5)
canvas.create_line(320,500,320,180, fill="green", width=5)



def read_raw(file):
		global raw
		global account
		account=[]
		raw = open(file).read().splitlines()
		for i in range(len(raw)):
			raw[i] = raw[i].strip()
		for i in range(len(raw)):
			account.append(raw[i].split(", "))

def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return str(round(todays_data['Close'][0],2))
    
def get_open_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return str(round(todays_data['Open'][0],2))

def addval():
	global y
	global investEntry
	global BoughtValue
	global stock 
  #store value when bought
	read_raw('accounts.txt')
	if float(investEntry.get()) <= float(account[y][1]) and float(investEntry.get()) > 1:
		file_object = open('storage.txt', 'a')
		errorFunds = Label(root1, text="Investissement completée    ", bg='#00FF00').place(x=430, y=250)
		file_object.write("\n"+ username + ", " + str(float(investEntry.get())/float(BoughtValue)) + ", " + stock )
		#str(float(account[y][2])- float(investEntry.get()))+ '*' + str(BoughtValue) + ", ")
		with open('accounts.txt', 'r') as file :
					filedata = file.read()
					filedata = filedata.replace(account[y][2], str(float(account[y][2])-(float(investEntry.get()))))
		with open('accounts.txt', 'w') as file:
					file.write(filedata)
		display_bal()
		refresh()
	else:
		errorFunds = Label(root1, text="MAX/MIN non-respectée", bg='#FF0000').place(x=430, y=250)
		file_object.close()
		
read_raw('loginAttempts.txt')
username = account[len(account)-1][0]
password = account[len(account)-1][1]

def get_invest():
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
	read_raw("storage.txt")
	for i in range(len(account)):
		if account[i][0]== username:
			for z in range(len(account)):
				if account[z][2]=="Nike":
					inNKE.append(str(float(get_current_price("NKE"))* float(account[z][1])))
				elif account[z][2]=="Amazon":
					inAMZN.append(str(float(get_current_price("NKE"))* float(account[z][1])))
				elif account[z][2]=="Tesla":
					inTSLA.append(str(float(get_current_price("NKE"))* float(account[z][1])))
				for i in range (len(inNKE)):
					investedNike += float(inNKE[i])
				for i in range (len(inAMZN)):
					investedAmazon += float(inAMZN[i])
				for i in range (len(inTSLA)):
					investedTesla += float(inTSLA[i])
	stockTotVal = investedNike + investedAmazon + investedTesla 			
	return stockTotVal

def display_bal():
		global y
		read_raw('accounts.txt')
		for i in range(len(account)):
			if account[i][0]== username:
				y=i
				balanceDisplay = Label(root1, text=("Balance: " + str(round(float(account[i][2]),2))) + "              ").place(x=80, y=20)

def investment(stockName):
	global investEntry
	global BoughtValue
	global stock
	stock=stockName

	investLabel = Label(root1, text="Montant a investir ($-$$$$): ").place(x=425,y=200)
	investEntry = Entry(root1, width=4)
	investEntry.place(x=430, y=220)
	if stock == 'Nike':
		BoughtValue = get_current_price('NKE')
	elif stock == 'Amazon':
		BoughtValue = get_current_price('AMZN')
	elif stock == 'Tesla':
		BoughtValue = get_current_price('TSLA')
	submitInvest = Button(root1, text="Confirmer", command=addval).place(x=475,y=220)

#buttons + tkinter objects
display_bal()
InvestNKE = Button(root1, text ="INVESTIR EN NIKE", command =lambda: investment('Nike')).place(x=75,y=60)
InvestAMZ = Button(root1, text ="INVESTIR EN AMAZON", command =lambda: investment('Amazon')).place(x=250,y=60)
InvestTSLA = Button(root1, text ="INVESTIR EN TESLA", command =lambda: investment('Tesla')).place(x=425,y=60)


def refresh():
	global investedTesla
	global investedAmazon
	global investedNike
	NKEval = Label(root1,text=("Ouverture: " + get_open_price("NKE") + "$")).place(x=75,y=100)
	AMZval = Label(root1,text=("Ouverture: " + get_open_price("AMZN") + "$")).place(x=250, y=100)
	TSLAval = Label(root1,text=("Ouverture: " + get_open_price("TSLA") + "$")).place(x=425,y=100)
	NKEopen = Label(root1,text=("Courant: " + get_current_price("NKE") + "$")).place(x=74,y=130)
	AMZopen = Label(root1,text=("Courant: " + get_current_price("AMZN") + "$")).place(x=250, y=130)
	TSLAopen = Label(root1,text=("Courant: " + get_current_price("TSLA") + "$")).place(x=425,y=130)	
	portfolioLabel = Label(root1, text="Votre portfolio d'investissements:").place(x=50, y=200)
	portfolioStats = Label(root1, text=("-   " + str(round(get_invest(),2)) + "$ investis en totale.            ")).place(x=50, y=235)
	get_invest()
	NKEStats = Label(root1, text=("-   " + str(round(float(investedNike),2)) + "$ investis en Nike.           ")).place(x=50, y=255)
	AMZNStats = Label(root1, text=("-   " + str(round(float(investedAmazon),2)) + "$ investis en Amazon.         ")).place(x=50, y=275)
	TSLAStats = Label(root1, text=("-   " + str(round(float(investedTesla),2)) + "$ investis en Tesla.            ")).place(x=50, y=295)

	now_EST = datetime.now(timezone('EST'))
	timeAndDay = Label(root1, text=now_EST.strftime("%d/%m/%Y %H:%M:%S")).place(x=400,y=10)
refresher = Button(root1, text="Refresh", command=refresh).place(x=580,y=10)
refresh()
global z



read_raw('accounts.txt') #can remove once files import

root1.title("Investissements") 
root1.geometry('700x600')

root1.mainloop()

#sell button right beside stock, for each label
#where are username/password labels on login page?
#We will have to stock buy value for trend percentage in label
#Does totalValStock update on refresh?
#Finish manager page (modify files, view his gains)
#Add more stocks? 
#More info on stocks (clickable link on titles?)