from tkinter import *

window = Tk()
window.title('Tkinter Sample Window')
window.geometry('400x400')

greeting = Label(text="Hello User", fg='red', bg='light blue')
button = Button(text="Click me", bg='pink', fg='purple')
entry = Entry(fg="yellow", bg="blue", width=50)
greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED,borderwidth=5 )
frame.pack()
label = Label(master=frame, text='Sample Frame')
label.pack()

textbox = Text(fg= 'orange',bg='brown')
textbox.pack()
window.mainloop()