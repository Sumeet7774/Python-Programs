# User information using tkinter

import tkinter as tk

root = tk.Tk()

def information():
    var1 = name.get()
    var2 = surname.get()
    var3 = phone.get()
    print('Your name is: ',var1)
    print('Your surname is: ',var2)
    print('Your phone number is: +91',var3)
    
def renew(): 
    name.set('')
    surname.set('')
    phone.set('')
    

name = tk.StringVar()
surname = tk.StringVar()
phone = tk.StringVar()


label1 = tk.Label(root,text ='Enter your name: ')
entry1 = tk.Entry(root,textvariable = name)

label2 = tk.Label(root,text = 'Enter your surname: ')
entry2 = tk.Entry(root,textvariable = surname)

label3 = tk.Label(root,text = 'Enter your phone number: ')
entry3 = tk.Entry(root,textvariable = phone)

button1 = tk.Button(root,text = 'SUBMIT', command = information)
button2 = tk.Button(root,text = 'CLEAR',command = renew)

label1.grid(row=0,column=0)
entry1.grid(row=0,column=1)

label2.grid(row=1,column=0)
entry2.grid(row=1,column=1)

label3.grid(row=2,column=0)
entry3.grid(row=2,column=1)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)

root.mainloop()

