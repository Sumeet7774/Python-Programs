# Program to make a simple
# addition

import tkinter as tk

root=tk.Tk()        # initializing tkinter as a root

def add():
    num1 = var1.get()       #we are getting the value of var1 into num1
    num2 = var2.get()       #we are getting the value of var2 into num2
    var1.set('')            #this will clear the values from textbox after Submit
    var2.set('')
    
    expression = str(num1)+'+'+str(num2)
    print(eval(expression)) #we are evaluating the expression using eval function
    
    addition = int(num1) + int(num2)    # here we are converting the value of num1 and num2 from string to int
    print(addition)  
    

var1=tk.StringVar()     #we are declaring the datatype of var1
var2=tk.StringVar()     #we are declaring the datatype of var2


label1 = tk.Label(root, text = 'Enter your first number: ')   #we are creating a label here
entry1 = tk.Entry(root,textvariable = var1)                 #we are taking value from the textbox1 by using entry function

label2 = tk.Label(root, text = 'Enter your second number: ')      #we are creating a label here
entry2=tk.Entry(root, textvariable = var2)                  #we are taking value from the textbox1 by using entry function

#show = '*' #this will print * when we write some text means it will hide our text for eg our password

button1=tk.Button(root,text = 'Submit',command = add)       #we are creating a button and we are calling the function add by writing command = add


label1.grid(row=0,column=0)     #this shows that our label1 will be located at 0,0
entry1.grid(row=0,column=1)     #this shows that our entry1 will be located at 0,1

label2.grid(row=1,column=0)      #this shows that our label1 will be located at 1,0
entry2.grid(row=1,column=1)     #this shows that our label1 will be located at 1,1

button1.grid(row=2,column=1)    #this shows that our button will be located at 2,1

root.mainloop()
