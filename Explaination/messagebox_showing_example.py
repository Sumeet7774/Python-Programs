# Example of message box 


import tkinter as tk 
from tkinter import messagebox as msg

root = tk.Tk()

def show(): 
    msg.showinfo('Name ','My name is Sumeet')      
    # Here Name is title and my name is sumeet is a message
    

button1=tk.Button(root,text = 'Read', command = show)
button1.grid(row=0,column=0)


root.mainloop()