# Radio button selecting gender using tkinter

import tkinter as tk 

root = tk.Tk()

var1 = tk.IntVar()


def gender():
    num1 = var1.get() 
    #print('Your selected option is: ',str(num1))
    if (int(num1) == 1):
        print('You are Male')
    else:
        print('You are Female')



label1 = tk.Label(root,text='Select your gender: ')

rb1 = tk.Radiobutton(root,text = 'Male', variable=var1, value=1, command=gender)
rb2 = tk.Radiobutton(root,text = 'Female', variable=var1, value=2, command=gender)


label1.grid(row=0,column=0)

rb1.grid(row=1,column=0)
rb2.grid(row=1,column=1)


root.mainloop()





