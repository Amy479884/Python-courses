from tkinter import *
from PIL import Image , ImageTk

root = Tk()
root.title( 'image')
root.geometry('400x400')

upload = Image.open("img.jpg")

image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, height=350 , width=300)

root.geometry('40x400')

upload = Image.open("https://th.bing.com/th/id/R.1a1f10b6714487c2ce8f56baf90f3c15?rik=YaLjGFUF5m5ZcQ&riu=http%3a%2f%2fupload.wikimedia.org%2fwikipedia%2fcommons%2f9%2f9b%2fPhoto_of_a_kitten.jpg&ehk=D%2bCxp6dPLSkHfYa8JvraOQ0MScRDCwP95fuL7yMpZ7E%3d&risl=&pid=ImgRaw&r=0")

image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, height=350, width=300)
label.place(x= 50, y=0)
label2 = Label(root, text="This is how you add image in Tkinter Window")
label2.place(x=40, y=360 )

root.mainloop()