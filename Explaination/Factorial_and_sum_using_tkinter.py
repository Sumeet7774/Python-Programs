# Factorial and Sum of a given number using tkinter

import tkinter as tk 
from tkinter import messagebox as msg

root = tk.Tk()

var1 = tk.StringVar()
var2 = tk.StringVar()

def fact():
    num1 = var1.get()
    var1.set('')
    factos = 1
    for i in range(1,int(num1)+1):  #here int((num+1)) is not supported because of StringVar datatype, so we write int((num)+1)
        factos = factos * i
    msg.showinfo('The factorial is: ' , str(factos))  
    print('The factorial is: ',factos)
    
def rangesum():
    num1 = var1.get()
    var1.set('')
    ans = 0
    for i in range(1,int(num1)+1):  #here int((num+1)) is not supported because of StringVar datatype, so we write int((num)+1)
        ans = ans + i
    msg.showinfo('The sum is: ' , str(ans))  
    print('The sum is: ',ans)
    

label1 = tk.Label(root, text = 'Enter your number: ') 
entry1 = tk.Entry(root,textvariable = var1)

button1 = tk.Button(root,text = 'Factorial',command = fact)
button2 = tk.Button(root,text = 'Sum',command = rangesum)

label1.grid(row=0,column=0)
entry1.grid(row=0,column=1)


button1.grid(row=1,column=0)
button2.grid(row=1,column=1)

root.mainloop()