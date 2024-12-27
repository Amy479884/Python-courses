from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    messagebox.askquestion("Question Box", "Do you want to scan.")

button = Button(root, text="Click to scan" ,  command=msg)
button.place(x=40, y=80)

root.mainloop()