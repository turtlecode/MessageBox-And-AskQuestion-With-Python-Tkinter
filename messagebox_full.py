
from tkinter import * 
from tkinter import messagebox
  
root = Tk()
root.geometry("300x200")
  
w = Label(root, text ='Turtle Code', font = "50") 
w.pack()
  
messagebox.showinfo("showinfo", "Information")
  
messagebox.showwarning("showwarning", "Warning")
  
messagebox.showerror("showerror", "Error")
  
messagebox.askquestion("askquestion", "Are you sure?")
  
messagebox.askokcancel("askokcancel", "Want to continue?")
  
messagebox.askyesno("askyesno", "Find the value?")
  
  
messagebox.askretrycancel("askretrycancel", "Try again?")  
  
root.mainloop() 

