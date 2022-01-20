from tkinter import *

import yfinance as yf

root1 = Tk()


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

def addval():
	global i
	global investEntry
	global BoughtValue
  #store value when bought
	file_object = open('storage.txt', 'a')
	file_object.write("\n"+ BoughtValue + "*" + investEntry.get() + ", ")
	file_object.close()
  #modify account balance

	with open('accounts.txt', 'r') as file :
		filedata = file.read()
	filedata = filedata.replace(account[i][4], str(float(account[i][4])- float(investEntry.get()))
	with open('accounts.txt', 'w') as file:
			file.write(filedata)
	print("Hi")
  
def display_bal():
		global i
		read_raw('accounts.txt')
		for i in range(len(account)):
			if account[i][0]== username:
				balanceDisplay = Label(root1, text=("Balance: " + account[i][4])).pack()
  
#def refresh():

def investment(stock):
	global investEntry
	global BoughtValue

	investLabel = Label(root1, text="Montant a investir ($-$$$$): ").pack()
	investEntry = Entry(root1)
	investEntry.place(x=200, y=200)
	if stock == 'nike':
		BoughtValue = get_current_price('NKE')
	elif stock == 'amazon':
		BoughtValue = get_current_price('AMZN')
	elif stock == 'tesla':
		BoughtValue = get_current_price('TSLA')

	submitInvest = Button(root1, text="Confirmer", command=addval).pack()

read_raw('loginAttempts.txt')
username = account[len(account)-1][0]
password = account[len(account)-1][1]

#buttons + tkinter objects
display_bal()
InvestNKE = Button(root1, text ="INVEST IN NIKE", command =lambda: investment('nike')).pack()
InvestAMZ = Button(root1, text ="INVEST IN AMAZON", command =lambda: investment('amazon')).pack()
InvestTSLA = Button(root1, text ="INVEST IN TESLA", command =lambda: investment('tesla')).pack()



print("Username: ", username, " Password: ", password)

read_raw('accounts.txt') #can remove once files import

root1.title("Investissements")
root1.geometry('700x600')


root1.mainloop()

import main