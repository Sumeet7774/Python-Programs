# Finding cube and modulus using radio button in tkinter

import tkinter as tk 


root = tk.Tk()

var1 = tk.StringVar()
var2 = tk.IntVar()

def cube():
    num1 = int(var1.get())
    num2 = var2.get()
    ans = num1 * num1 * num1
    if (int(num2) == 1):
        print('The cube is: ',ans)    
    var1.set('')


def modulus():
    num1 = int(var1.get())
    num2 = var2.get()
    ans = num1 % 2 
    if (int(num2) == 2):
        print('The modulus is: ',ans)
    var1.set('')    
    
    
label1 = tk.Label(root,text='Enter your first number: ')    


entry1 = tk.Entry(root,textvariable=var1)


rb1 = tk.Radiobutton(root,text = 'Cube', variable=var2, value=1, command=cube)
rb2 = tk.Radiobutton(root,text = 'Modulus', variable=var2, value=2, command=modulus)    



label1.grid(row=0,column=0)

entry1.grid(row=0,column=1)


rb1.grid(row=1,column=0)
rb2.grid(row=1,column=1)


root.mainloop()    
