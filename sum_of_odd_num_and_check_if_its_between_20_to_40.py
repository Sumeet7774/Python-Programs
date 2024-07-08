# Find the sum of n odd numbers and check whether nth given number is between 20 to 40.
# Name button as range and another as odd button

import tkinter as tk

root=tk.Tk() 


var1 = tk.StringVar()



def odd():
    num1 = var1.get()
    count = 0
    for i in range(0,int(num1)+1):
        if int(i) % 2 == 1:
            count = count + i
    print('Sum of odd numbers are :: ',count) 
    label2.config(text='Sum of odd: ' + str(count))
    var1.set('')        
    
    
    
def check():
    num2 = var1.get()
    if int(num2) >= 20 and int(num2) <=40:
        print('The number is between 20 and 40')
        label3.config(text='Yes in range')
    else:
        print('The number is not between 20 and 40')
        label3.config(text='Not in range')
    var1.set('')    



label1 = tk.Label(root, text = 'Enter your number: ')
entry1 = tk.Entry(root,textvariable = var1)

label2 = tk.Label(root)
label3 = tk.Label(root)


button1 = tk.Button(root,text = 'SUM OF ODD',command = odd)
button2 = tk.Button(root,text = 'CHECK',command = check)


label1.grid(row=0,column=0)     
entry1.grid(row=0,column=1)

label2.grid(row=1,column=0)
label3.grid(row=1,column=1)

button1.grid(row=2,column=0) 
button2.grid(row=2,column=1)


root.mainloop()