from tkinter import *
from tkdial import Dial

def b1():
    l.config(text=dial1.get())

root = Tk()
root.geometry("600x500")

dial1 = Dial(root,width=120,height=120,unit_color="black",color_gradient=("orange","red"))
dial1.grid(padx=20, pady=20)

l = Label(root, text="")
l.place(x= 120, y = 320)

b = Button(root, text="yay", command=b1)
b.place(x= 120, y = 370)
Key1 = Button(root,)





root.mainloop()
