# illustration of icon - Info
from tkinter import *
from tkinter import messagebox
 
main = Tk()
 
def check():
   object = messagebox.askquestion("Form",
                          "do you want to continue",
                          icon ='warning')
   print(object)
 
main.geometry("100x100")
B1 = Button(main, text = "check", command = check)
B1.pack()
 
main.mainloop()