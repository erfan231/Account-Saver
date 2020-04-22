import tkinter as tk
from tkinter import *

window = tk.Tk() #creates the window
window.title("Saving Accounts")
window.geometry('300x110')
window['bg'] = '#49A'



tk.Label(window, text="Account for: ").grid(row=0)
tk.Label(window, text="Account Username: ").grid(row=1)
tk.Label(window, text="Password: ").grid(row=2)
tk.Label(window, text="Confirm Password: ").grid(row=3)

Account = tk.Entry(window)
UserName = tk.Entry(window)
Password = tk.Entry(window)
Confirm_Password = tk.Entry(window)

Account.insert(10,"") #this for if you want to put demo/dummy data in the account field
UserName.insert(10, "")  #this for if you want to put demo/dummy data in the UserName field


Account.grid(row=0, column=1)
UserName.grid(row=1, column=1)
Password.grid(row=2, column=1)
Confirm_Password.grid(row=3, column=1)


def SaveText():
    
    if Confirm_Password.get() == Password.get():
         file = open("Accounts.txt","a")
         file.write("Account for: ")
         file.write(Account.get())
         file.write("\n")
         file.write("UserName: ")
         file.write(UserName.get())
         file.write("\n")
         file.write("Password: ")
         file.write(Password.get())
         file.write("\n")
         file.write("\n")
         file.close()
         print("Password Saved!")
    if Confirm_Password.get() != Password.get():
        print("Password don't match")

tk.Button(window, 
          text='Save', 
          command=SaveText).grid(row=5, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=2)
tk.Button(window, 
          text='Quit', 
          command=window.destroy).grid(row=5, 
                                    column=1, 
                                    sticky=tk.W, 
                                    pady=1)


window.mainloop()


