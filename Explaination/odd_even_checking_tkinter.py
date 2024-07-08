# Program to find number is even or odd using tkinter
# addition

import tkinter as tk

root=tk.Tk()        # initializing tkinter as a root

def odd():
    num1 = var1.get()       #we are getting the value of var1 into num1
    if int(num1) % 2 == 1:
        var2.set(num1+' is odd')
    else:
        var2.set(num1+' is even')
    var1.set('')            #this will clear the values from textbox after Submit
    
def even():
    num2 = var1.get()
    if int(num2) % 2 == 0:
        var2.set(num2+ ' is even' )
    else:
        var2.set(num2+' is odd')
    var1.set('')


var1 = tk.StringVar()     #we are declaring the datatype of var1
var2 = tk.StringVar()


label1 = tk.Label(root, text = 'Enter your number: ')   #we are creating a label here
entry1 = tk.Entry(root,textvariable = var1)                 #we are taking value from the textbox1 by using entry function

label2 = tk.Label(root, textvariable = var2)      #we are creating a label here
           

button1=tk.Button(root,text = 'ODD',command = odd)       #we are creating a button and we are calling the function add by writing command = add
button2=tk.Button(root,text = 'EVEN',command = even)

label1.grid(row=0,column=0)     #this shows that our label1 will be located at 0,0
entry1.grid(row=0,column=1)     #this shows that our entry1 will be located at 0,1

label2.grid(row=1,column=0)      #this shows that our label1 will be located at 1,0

button1.grid(row=2,column=0)    #this shows that our button will be located at 2,1
button2.grid(row=2,column=1)

root.mainloop()
