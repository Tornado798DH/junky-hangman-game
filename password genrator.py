#   Tornado DH
#Just saying hi :)
from tkinter import*
import string
import secrets
import random
import pyperclip

def generator():
    upper = list(string.ascii_uppercase)
    lower = list(string.ascii_lowercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)

    all=upper+lower+digits+punctuation
    password_len=int(length_Box.get())
    part1 = round(password_len * (30 / 100))
    part2 = round(password_len * (20 / 100))
    password=""
    for i in range(part1):
        password += secrets.choice(upper)
        password += secrets.choice(digits)

    for i in range(part2):
        password += secrets.choice(punctuation)
        password += secrets.choice(lower)

    passwordField.insert(0,password)

def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)

DH = Tk() 
DH.geometry("220x220")
mycolor='#FFF4E6'
fontcolor='#1D4C6B'
DH.config(bg=mycolor)
choice=IntVar()
Font=('arial',13,'bold')

passwordlabel=Label(DH,text='Password Generator',font=('Times',18,'bold'),bg=mycolor,fg=fontcolor)
passwordlabel.grid(pady=10)

lengthlabel=Label(DH,text="Passowrd Length",font=('cairo',13,'bold'),bg=mycolor,fg=fontcolor)
lengthlabel.grid()

length_Box=Spinbox(DH,from_=8,to_=32,font=Font,width=5,wrap=True)
length_Box.grid()

generateButton=Button(DH,text='Generate',font=(Font,10,'bold'),bg=mycolor,command=generator)
generateButton.grid(pady=5)

passwordField=Entry(DH,width=20,bd=2,font=Font)
passwordField.grid()

copyButton=Button(DH,text='Copy to Clipboard',font=(Font,10,'bold'),bg=mycolor,command=copy)
copyButton.grid(pady=5)

DH.mainloop()