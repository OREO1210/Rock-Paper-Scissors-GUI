#coded by chandu
from tkinter import *
import random
import os

cs=0
ps=0

def R():
    ci=random.randint(1,3)
    global cs
    global ps
    if(ci==1):
        cs=cs+1
        l2.configure(text="\nYour move: Rock\t\t Computer's move: Paper\n\nComputer gets a point\n")
    elif(ci==2):
        ps=ps+1
        l2.configure(text="\nYour move: Rock\t\t Computer's move: Scissors\n\nYou get a point\n")
    elif(ci==0):
        l2.configure(text="\nYour move: Rock\t\t Computer's move: Rock\n\nNo points\n")
    l1.configure(text=f'Your Score = {ps}\t Computer Score = {cs}\n')
    if(cs==5):
        l2.configure(text='Computer wins. Better luck next time.\n')
        l2.grid_configure(column=0,row=2,columnspan=3)
        bR.grid_forget()
        bP.grid_forget()
        bS.grid_forget()
        Retry.grid(column=0,row=3,pady="20")
        Close.grid(column=2,row=3,pady="20")
    if(ps==5):
        l2.configure(text='Congratulations. You win!\n')
        l2.grid_configure(column=0,row=2,columnspan=3)
        bR.grid_forget()
        bP.grid_forget()
        bS.grid_forget()
        Retry.grid(column=0,row=3,pady="20")
        Close.grid(column=2,row=3,pady="20")
        
    

def P():
    ci=random.randint(1,3)
    global cs
    global ps
    if(ci==1):
        l2.configure(text="\nYour move: Paper\t\t Computer's move: Paper\n\nNo points\n")
    elif(ci==2):
        cs=cs+1
        l2.configure(text="\nYour move: Paper\t\t Computer's move: Scissors\n\nComputer gets a point\n")
    elif(ci==0):
        ps=ps+1
        l2.configure(text="\nYour move: Paper\t\t Computer's move: Rock\n\nYou get a point\n")
    l1.configure(text=f'Your Score = {ps}\t Computer Score = {cs}\n')
    if(cs==5):
        l2.configure(text='Computer wins. Better luck next time.\n')
        l2.grid_configure(column=0,row=2,columnspan=3)
        bR.grid_forget()
        bP.grid_forget()
        bS.grid_forget()
        Retry.grid(column=0,row=3,pady="20")
        Close.grid(column=2,row=3,pady="20")
    if(ps==5):
        l2.configure(text='Congratulations. You win!\n')
        l2.grid_configure(column=0,row=2,columnspan=3)
        bR.grid_forget()
        bP.grid_forget()
        bS.grid_forget()
        Retry.grid(column=0,row=3,pady="20")
        Close.grid(column=2,row=3,pady="20")

def X2():
    ci=random.randint(1,3)
    global cs
    global ps
    if(ci==1):
        ps=ps+1
        l2.configure(text="\nYour move: Scissors\t\t Computer's move: Paper\n\nYou get a point\n")
    elif(ci==2):
        l2.configure(text="\nYour move: Scissors\t\t Computer's move: Scissors\n\nNo points\n")
    elif(ci==0):
        cs=cs+1
        l2.configure(text="\nYour move: Scissors\t\t Computer's move: Rock\n\nComputer gets a point\n")
    l1.configure(text=f'Your Score = {ps}\t Computer Score = {cs}\n')
    if(cs==5):
        l2.configure(text='Computer wins. Better luck next time.\n')
        l2.grid_configure(column=0,row=2,columnspan=3)
        bR.grid_forget()
        bP.grid_forget()
        bS.grid_forget()
        Retry.grid(column=0,row=3,pady="20")
        Close.grid(column=2,row=3,pady="20")
    if(ps==5):
        l2.configure(text='Congratulations. You win!\n')
        l2.grid_configure(column=0,row=2,columnspan=3)
        bR.grid_forget()
        bP.grid_forget()
        bS.grid_forget()
        Retry.grid(column=0,row=3,pady="20")
        Close.grid(column=2,row=3,pady="20")


def restart():
    global cs
    global ps
    cs=0
    ps=0
    Retry.grid_forget()
    Close.grid_forget()
    l1.configure(text=f'Your Score = {ps}\t Computer Score = {cs}\n')
    l2.configure(text="\nMax score = 5\n",fg="white",bg="#1f1f1f",padx="16",pady="10",font=('Cabin',12))
    l0.grid(column=0,row=0,columnspan=3,pady="16")
    l1.grid(column=0,row=1,columnspan=3)
    bR.grid(column=0,row=2)
    bP.grid(column=1,row=2)
    bS.grid(column=2,row=2)
    l2.grid(column=0,row=3,columnspan=3)
    
    
    
def XY():
    w.destroy()
    

w=Tk()
w.configure(bg="#1f1f1f")
w.title("ROCK PAPER SCISSORS")

l0=Label(text="ROCK PAPER SCISSORS",font=('Harry P',30),fg="white",bg="#1f1f1f",padx="16",pady="10")
l1=Label(text=f'Your Score = {ps}\t Computer Score = {cs}\n',fg="white",bg="#1f1f1f",font=('Cabin',12))
l2=Label(text="\nMax score = 5\n\nClick on a button to start\n",fg="white",bg="#1f1f1f",padx="16",pady="10",font=('Cabin',12))

bR=Button(w, text="ROCK",font=('Crimes of Grindelwald',12), command=R,pady="15",padx="16",bd=0,bg="#131313",fg="white",activebackground="brown3",activeforeground="white")
bP=Button(w, text="PAPER",font=('Crimes of Grindelwald',12),pady="15",padx="16", command=P,bd=0,bg="#131313",fg="white",activebackground="slate gray",activeforeground="white")
bS=Button(w, text="SCISSORS",font=('Crimes of Grindelwald',12),pady="15",padx="16", command=X2,bd=0,bg="#131313",fg="white",activebackground="green4",activeforeground="white")
Retry=Button(w, text="Retry",font=('Cabin',12), command=restart,pady="10",padx="16",bd=0,bg="#1e1d3a",fg="white",activebackground="#1d1b63",activeforeground="white")
Close=Button(w, text="Close",font=('Cabin',12), command=XY,pady="10",padx="16",bd=0,bg="#131313",fg="white",activebackground="#f1707a",activeforeground="white")

l0.grid(column=0,row=0,columnspan=3,pady="16")
l1.grid(column=0,row=1,columnspan=3)
bR.grid(column=0,row=2)
bP.grid(column=1,row=2)
bS.grid(column=2,row=2)
l2.grid(column=0,row=3,columnspan=3)

def oe(e):
    bR.config(background='firebrick4')
def ol(e):
    bR.config(background= '#131313')
bR.bind('<Enter>',oe)
bR.bind('<Leave>',ol)

def oe2(e):
    bP.config(background='dark slate gray')
def ol2(e):
    bP.config(background= '#131313')
bP.bind('<Enter>',oe2)
bP.bind('<Leave>',ol2)

def oe1(e):
    bS.config(background='darkgreen')
def ol1(e):
    bS.config(background= '#131313')
bS.bind('<Enter>',oe1)
bS.bind('<Leave>',ol1)

def oe3(e):
    Retry.config(background='#1d1b5c')
def ol3(e):
    Retry.config(background= '#1e1d3a')
Retry.bind('<Enter>',oe3)
Retry.bind('<Leave>',ol3)

def oe4(e):
    Close.config(background='#e81123')
def ol4(e):
    Close.config(background= '#131313')
Close.bind('<Enter>',oe4)
Close.bind('<Leave>',ol4)

w.geometry("600x375")
w.resizable(False, False)
w.grid_rowconfigure(0,weight=1)
w.grid_rowconfigure(1,weight=1)
w.grid_rowconfigure(2,weight=1)
w.grid_rowconfigure(3,weight=1)
w.grid_columnconfigure(0,weight=1)
w.grid_columnconfigure(1,weight=1)
w.grid_columnconfigure(2,weight=1)

w.mainloop()