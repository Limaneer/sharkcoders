from tkinter import *




root = Tk()

def blue():
    root.configure(background="#0000FF")
def red():
    root.configure(background="#FF0000")
def black():
    root.configure(background="#000000")
def green():
    root.configure(background="#00FF00")

root.title("colour changer")
root.geometry("500x400+400+100")
root.wm_resizable(width=False,height=False)

button1 = Button(root, command=blue, text="Azul",font="arial 14 bold")
button1.place(width=200, height= 160, x=40, y = 20)

button2 = Button(root, command=red,text="Vermelho",font="arial 14 bold")
button2.place(width=200, height= 160, x=260, y = 20)

button3 = Button(root, command=green,text="Verde",font="arial 14 bold")
button3.place(width=200, height= 160, x=40, y = 200)

button4 = Button(root, command=black,text="Preto",font="arial 14 bold")
button4.place(width=200, height= 160, x=260, y = 200)

root.mainloop()
