from tkinter import *
from transactions import *
from PIL import ImageTk, Image  
import time
import yfinance
import os

#Add stock info if time allows it.

class Main():
  def __init__():
    pass


root = Tk()
Titre = Label(root, text = "Banque Crypto")
Titre.pack()

logo = Canvas(root, width = 150, height = 130)
logo.pack(side=TOP, anchor = NW)
logoImg = ImageTk.PhotoImage(Image.open("images (1).png"))
logo.create_image(20, 20, anchor = NW, image = logoImg)

loginBtn = Button(text="LOGIN",fg="red", height = 3, width = 20, command=lambda:print("Hello"))
loginBtn.place(x=230, y=150)


root.geometry("700x360")

root.mainloop()

