from tkinter import * 
from tkinter import messagebox
  
root = Tk()
root.geometry("300x200")
  
w = Label(root, text ='Turtle Code', font = "50") 
w.pack()

  
askyesno = messagebox.askyesno("askyesno", "Find the value?")

if askyesno:
  print("Yes")
else:
  print("No")

  
root.mainloop() 