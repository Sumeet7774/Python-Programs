# Username Password using tkinter

import tkinter as tk
root = tk.Tk()

def login():
    var1 = username.get()
    var2 = password.get()
    print('Your username is: ',var1)
    print('Your password is: ',var2)
    var1 = username.set('')
    var2 = password.set('')
    
    
username = tk.StringVar()
password = tk.StringVar()



label1 = tk.Label(root,text = 'Enter your username: ')
entry1 = tk.Entry(root,textvariable = username)

label2 = tk.Label(root,text = 'Enter your password: ')
entry2 = tk.Entry(root,textvariable = password, show ='*')

button1 = tk.Button(root,text = 'LOGIN', command = login)


label1.grid(row=0,column=0)     #this shows that our label1 will be located at 0,0
entry1.grid(row=0,column=1)     #this shows that our entry1 will be located at 0,1

label2.grid(row=1,column=0)      #this shows that our label1 will be located at 1,0
entry2.grid(row=1,column=1)     #this shows that our label1 will be located at 1,1

button1.grid(row=2,column=1)    #this shows that out button will be located at 2,1

root.mainloop()